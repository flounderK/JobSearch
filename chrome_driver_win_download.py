import requests
from bs4 import BeautifulSoup
import zipfile
import os

file_name = 'chromedriver_win32.zip'
download_url = 'https://chromedriver.storage.googleapis.com/'
latest_release = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'

s = requests.session()
r = s.get(latest_release)
version = r.content.decode("utf-8").strip()
download_url = download_url + version + '/' + file_name 
r = s.get(download_url)
with open(file_name, 'wb') as f:
    f.write(r.content)
s.close()
zip_ref = zipfile.ZipFile(file_name, 'r')
zip_ref.extractall('.')
zip_ref.close()
os.remove(file_name)

