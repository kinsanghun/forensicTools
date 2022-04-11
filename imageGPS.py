from PIL import Image
from PIL.ExifTags import TAGS

class imageinfo:
    def __init__(self, path="./resource/"):
        self.path = path

    def ImageGPS(self, filename):
        image = Image.open(self.path + filename)
        info = image._getexif()
        image.close()

        taglabel = dict()

        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            taglabel[decoded] = value

        exifGPS = taglabel['GPSInfo']

        latData = exifGPS[2]
        lonData = exifGPS[4]

        latDeg = latData[0]
        latMin = latData[1]
        latSec = latData[2]

        lonDeg = lonData[0]
        lonMin = lonData[1]
        lonSec = lonData[2]

        Lat = str(int(latDeg)) + "°" + str(int(latMin)) + "'" + str(latSec) + "\"" + exifGPS[1]
        Lon = str(int(lonDeg)) + "°" + str(int(lonMin)) + "'" + str(lonSec) + "\"" + exifGPS[3]

        print("[+] Image GPS : ", Lat, Lon)
