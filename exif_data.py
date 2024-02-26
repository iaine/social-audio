'''
Function to get exif data from files.
Needs exiftool
'''
import exiftool
import requests

class Metadata():

    def download(self, url):
        media_file = requests.get(url)
        if media_file.status_code == 200:
            fname = url.split('/')[:-1]
            with open("data/"+fname, 'w') as fh:
                fh.write(media_file.content)
            
            self.get_metadata(fname)
            
    def get_metadata(self, fname):
        '''
           Function to extract filename
        '''
        with exiftool.ExifToolHelper() as et:
            metadata = et.get_metadata(fname)
            for d in metadata:
                print("{:20.20} {:20.20}".format(d["SourceFile"],
                                         d["EXIF:DateTimeOriginal"]))