'''
Load data
'''
import requests
from social_exception import socialException

class load():

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
                