from engine import FITSComparison
import urllib.parse
import http.client
import sys

class Hunter:
    def __init__(self, id, images, dates, coordinates):
        """
        this class will be used to perform all the session operation
        :param id: int
        :param images: list of the images
        :param dates: string
        :param coordinates: list of the coordinates (RA, DEC)
        """
        self.id = id

        self.images = images
        self.dates = dates
        self.coordinates = coordinates

        self.analysis = None
        self.compared = None

        self.configuration = {"temp":    "/home/alessio/AsterHunter/AsterHunter/temp/",
                              "archive": "/home/alessio/AsterHunter/AsterHunter/archive/"}


    def makeComparison(self):
        """
        this method will use a FITSComparison class to work on images
        :param configuration, DirConfiguration
        :return: None
        """
        self.analysis = FITSComparison(self.images[0], self.images[1], self.images[2])
        self.compared = self.analysis.comparison(self.configuration)

    def insertImages(self):
        """
        this method will connecto to the localhost http server to access database via php engine
        :return: None
        """
        params = urllib.parse.urlencode({"id":          self.id,
                                         "success":     self.analysis.missionSuccessful(),
                                         "images":      self.compared,
                                         "datetime":    self.dates,
                                         "coord":       self.coordinates})

        headers = {"Content-type": "application/x-www-form-urlencoded"}

        try:
            connection = http.client.HTTPConnection("127.0.0.1")
            connection.request('POST', "/index.php/survey/addsurvey", params, headers)
            connection.getresponse().read()
            connection.close()
        except ConnectionError:
            sys.exit()


