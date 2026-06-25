import urllib.request
import zipfile
import os

url = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
zip_path = "smsspamcollection.zip"

urllib.request.urlretrieve(url, zip_path)

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall("data_temp")

os.rename("data_temp/SMSSpamCollection", "data/spam.csv")
os.remove(zip_path)
os.rmdir("data_temp")

print("Done! Dataset saved to data/spam.csv")