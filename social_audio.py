from extract import Extract as ex
from audio_details import audioDetails as ad
import glob
import configparser
import sys

from social_exception import socialException

config = configparser.ConfigParser()
config.read('config.ini')

zee_file = sys.argv[2]

fs = ""
if config["download"] is not None:
    fs = glob.glob(config["download"])

    for f in fs:
        ex.extract_from_video(f)
        ad.get_details(f)
else:
    raise socialException("No directory found. ")