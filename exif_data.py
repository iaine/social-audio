'''
Function to get exif data from files.
Needs exiftool
'''
import exiftool

class Metadata():

    def get_metadata(self, fname):
        '''
           Function to extract filename
        '''
        with exiftool.ExifToolHelper() as et:
            metadata = et.get_metadata(files)
            for d in metadata:
                print("{:20.20} {:20.20}".format(d["SourceFile"],
                                         d["EXIF:DateTimeOriginal"]))