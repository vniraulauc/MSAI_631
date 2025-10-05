# src/download_data.py
import os
import zipfile
from urllib.request import urlretrieve

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)

url = "http://files.grouplens.org/datasets/movielens/ml-100k.zip"
zip_path = os.path.join(DATA_DIR, "ml-100k.zip")

print("Downloading MovieLens 100K...")
urlretrieve(url, zip_path)
print("Extracting...")
with zipfile.ZipFile(zip_path, "r") as z:
    z.extractall(DATA_DIR)
print("Done. Files in:", DATA_DIR)
