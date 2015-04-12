__author__ = 'federico'
from astropy import units as u
from astropy.coordinates import SkyCoord
import math

def fov_calculus(pixel_size,pixel_numb_h,pixel_numb_l,focal_length):
    l_sensor = pixel_size / 1000 * pixel_numb_l
    h_sensor = pixel_size / 1000 * pixel_numb_h
    fov_h = math.degrees(2 * math.atan((h_sensor/2)/focal_length))
    fov_l = math.degrees(2 * math.atan((l_sensor/2)/focal_length))
    return [fov_h,fov_l]


def main(ra_hms, dec, ol_fact,n_image,pixel_size,pixel_numb_h,pixel_numb_l,focal_length):
    """
    The purpose of this function is to calculate an array of the coordinates (hms,deg) of the centre of sectors.
    These sectors are the subdivision of the image centered in the "ra_hms" and "dec" coordinates.
    The image will be considered a perfect square.
    :rtype : array
    :param ra_hms: ra coordinate (hms)
    :param dec: dec coordinate in degree
    :param ol_fact: overlap factor in percentage (useful for overlapping)
    :param n_image: total number of sector in which the image will be subdivided
    :param pixel_size: size of the pixel of the image
    :param pixel_numb_h: number of pixel on the height
    :param pixel_numb_l: number of pixel on the length
    :param focal_length: focal length of the observatory
    """

    fov = fov_calculus(pixel_size,pixel_numb_h,pixel_numb_l,focal_length)

    center = SkyCoord(ra_hms,dec)
    ra_deg = center.ra.degree
    dec_deg = center.dec.degree
    side = round(math.sqrt(n_image),0)

    fov_h = fov[0]
    fov_l = fov[0]

    # plt.plot(ra_deg,dec_deg)
    # plt.plot(ra_deg+fov_h,dec_deg+fov_l)
    # plt.axis([0,20,0,50],polar="true")
    # plt.savefig("ciao.png")


    #First movement to the right-up corner of the square
    ra_deg_ruc = ra_deg - (side*fov_h)/2
    dec_deg_ruc = dec_deg + (side*fov_l)/2
    ra_deg_beg = ra_deg_ruc + fov_h/2
    dec_deg_beg = dec_deg_ruc - fov_l/2

    file = open("result.txt","w")

    #Centered on the first sector. Added to the array
    center_beg = SkyCoord(ra_deg_beg*u.degree,dec_deg_beg*u.degree)
    #file.write(center_beg.to_string("hmsdms") + " ")


    temp_ra_deg = ra_deg_beg # X
    temp_dec_deg = dec_deg_beg # Y
    for i in range(0,int(side)):
        for j in range(0, int(side)):
            if (j == 0):
                temp_center = SkyCoord(temp_ra_deg*u.degree,temp_dec_deg*u.degree)
                file.write(temp_center.to_string("hmsdms") + "\n")
                continue
            new_ra_deg = temp_ra_deg + (fov_h*ol_fact) # X Moving
            temp_ra_deg = new_ra_deg
            temp_center = SkyCoord(temp_ra_deg*u.degree,temp_dec_deg*u.degree)
            file.write(temp_center.to_string("hmsdms") + "\n")
            if j == side-1:
                file.write(temp_center.to_string("hmsdms")+ "\n")
        new_dec_deg = temp_dec_deg - (fov_l*ol_fact) # Y Moving
        temp_dec_deg = new_dec_deg
        temp_ra_deg = ra_deg_beg
    file.close()

main("00h42m30s",41.2*u.degree,1.0,16,4.3,5184,3456,750)