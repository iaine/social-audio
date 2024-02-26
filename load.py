'''
Load data
'''
import requests
from hashlib import sha256

from database import database
from social_exception import socialException

class Load():

    def load(self, fname):
        '''
        Main load function
        '''
        if fname.endswith('.csv'):
            self.load_csv(fname)
        elif fname.endswith('.ndjson'):
            self.load_json(fname)
        else:
            raise socialException("Cannot handle file")
            

    def load_csv(self, fname):
        pass

    def load_json(self, fname):
        pass

    def load_web_data(self, audio_column, directory):
        '''
          Function to 
        '''

        for audio_file in audio_column:
            fname = requests.get(audio_file)
            if fname.status_code == 200:
                a_file = audio_file.split('/')[:-1]
                with open(directory + '/' + a_file, 'w') as fh:
                    fh.write(fname.text)

    def load_zeeschuimer(self, fname):
        '''
        Handle the Zeeschuimer files ofr now
        '''
        _fname = fname.split('-')

        if _fname[2] == "tiktok.com":
            self._load_tiktok(fname)
        elif _fname[2] == "instagram.com":
            self._load_instagram(fname)
        else:
            raise socialException('Data Source not handled.')
        
    def _load_tiktok(fname):
        '''
        Handle Zeeschuimer export
        '''

        if fname.endswith('.csv'):
            with open(fname, 'r') as fh:
                data = fh.read()
            
            db = database()
            project_id = self._create_hash(fname)
            for datum in range(1, len(data)):
                db.insert_row(project_id, datum[0])
        else:
            raise socialException('PLease convert with Zeehaven')
        
    def _create_hash(self, fname):
        '''
        Create hash for file
        '''
        return sha256(fname)
                