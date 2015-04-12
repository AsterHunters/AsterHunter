from astropy.io.fits import FITSDiff
import shutil

class FITSComparison:
    def __init__(self, image_1, image_2, image_3, numdiff=10, tolerance=0.0):
        """
        this is the FITS comparison class constructor
        :param image_1: string, image name
        :param image_2: string, image name
        :param image_3: string, image name
        """
        self.image_1 = image_1
        self.image_2 = image_2
        self.image_3 = image_3

        self.num_differences = numdiff
        self.tolerance = tolerance

        self.report = False

    def comparison(self, conf):
        """
        this is the FITS comparison function
        NB: the images are given by chronological order
        :param conf: DirConfiguration
        :return: list of strings
        """
        fd1 = FITSDiff(conf["temp"] + self.image_1, conf["archive"] + self.image_2, numdiffs=self.num_differences, tolerance=self.tolerance)
        fd2 = FITSDiff(conf["temp"] + self.image_2, conf["archive"] + self.image_3, numdiffs=self.num_differences, tolerance=self.tolerance)
        fd3 = FITSDiff(conf["temp"] + self.image_1, conf["archive"] + self.image_3, numdiffs=self.num_differences, tolerance=self.tolerance)

        # eliminating first approximation interference -> no objects
        if not fd1.identical and not fd2.identical:
            if fd3.identical:
                self.report = False

                # storing the fit file
                self.moveimage([self.image_1], conf)
                return [conf["archive"] + self.image_1]

        # anomaly detected -> repository notification
        if not fd1.identical and not fd2.identical:
            self.report = True

            # storing the fit files
            self.moveimage([self.image_1, self.image_2, self.image_3], conf)
            return [conf["archive"] + self.image_1, conf["archive"] + self.image_2, conf["archive"] + self.image_3]


    def moveimage(self, image_list, conf):
        """
        this method will be invocated to move the selected image to the destination main folder
        :param image_list: list of strings, the image names list
        :param conf: DirConfiguration
        :return: list of strings, used to archive by the php and MySQL server
        """
        for image in image_list:
            shutil.move(conf["temp"] + image, conf["archive"] + image)


    def missionSuccessful(self):
        """
        this method will be used to check for mission successfull
        :return:
        """
        return self.report