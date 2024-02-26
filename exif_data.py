'''
Function to get exif data from files.
Needs exiftool
'''
import exiftool
import requests

from database import database as db

class Metadata():

    def download(self, projectid, url):
        media_file = requests.get(url)
        if media_file.status_code == 200:
            fname = url.split('/')[:-1]
            with open("data/"+fname, 'w') as fh:
                fh.write(media_file.content)
            
            self.get_metadata(projectid, fname)
            
    def get_metadata(self, projectid, fname):
        '''
           Function to extract filename
        '''
        with exiftool.ExifToolHelper() as et:
            metadata = et.get_metadata(fname)
            for k, v in metadata:
                db.insert_features(projectid, fname, k, metadata[k])