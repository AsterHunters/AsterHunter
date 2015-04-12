#include <iostream>
#include <fstream>
#include <sys/time.h>
#include <string.h>
#include <math.h>
#include <memory>
#include <time.h>

#include "simplescope.h"
#include "simpleccd.h"
#include "indicom.h"

// autopointer to a "SimpleScope" structure that will rapresent our telescope
std::auto_ptr<SimpleScope> simpleScope(0);

// connect with out telescope
bool SimpleScope::Connect()
{
    DEBUG(INDI::Logger::DBG_SESSION, "Simple Scope connected successfully!");
    return true;
}

// slew the telescope to the new coordinates (RA/DEC)
bool SimpleScope::Goto(double ra, double dec)
{
    time_t     now = time(0);
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    std::ofstream myfile;

    targetRA = ra;
    targetDEC = dec;
    char RAStr[64], DecStr[64], cordStr[64];

    // Parse the RA/DEC coordinates into strings
    fs_sexa(RAStr, targetRA, 2, 3600);
    fs_sexa(DecStr, targetDEC, 2, 3600);

    // Here there will be a function to call a Python script that will divide the designed space portion
    // into little one that will be pointed and captured by Raspberry
    /* Python_function(parameters) */

    // Update the telescope's status to "SLEWING"
    TrackState = SCOPE_SLEWING;

    // Slewing the telescope to the new coordinates
    DEBUGF(INDI::Logger::DBG_SESSION, "Slewing to RA: %s - DEC: %s", RAStr, DecStr)

    myfile.open("coordinates.txt", std::ios_base::app);
    strftime(buf, sizeof(buf), "%Y-%m-%d %X ", &tstruct);
    myfile << buff << RAStr << " " << DecStr << "\n";

    return true;
}

bool SimpleCCD::StartExposure(float duration)
{
    ExposureRequest = duration;

    // set the CCD's exposure duration
    PrimaryCCD.setExposureDuration(duration);
    gettimeofday(&ExpStart,NULL);

    // update the telescope's status
    InExposure = true;
    return true;
}

void SimpleCCD::grabImage()
{
    // Let's get a pointer to the frame buffer
    char * image = PrimaryCCD.getFrameBuffer();
 
    // Get width and height
    int width = PrimaryCCD.getSubW() / PrimaryCCD.getBinX() * PrimaryCCD.getBPP()/8;
    int height = PrimaryCCD.getSubH() / PrimaryCCD.getBinY();
 
    // Fill buffer (this time we will use random data)
    for (int i=0; i < height ; i++)
        for (int j=0; j < width; j++)
            image[i*width+j] = rand() % 255;
    
    IDMessage(getDeviceName(), "Download complete.");

    // Let INDI::CCD know we're done filling the image buffer
    ExposureComplete(&PrimaryCCD);
}

// disconnect with the telescope
bool SimpleScope::Disconnect()
{
    DEBUG(INDI::Logger::DBG_SESSION, "Simple Scope disconnected successfully!");
    return true;
}