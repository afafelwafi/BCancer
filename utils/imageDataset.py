import requests 
import pandas as pd 
import urllib.request, urllib.error, urllib.parse, urllib.request, urllib.parse, urllib.error,sys
import ast
import zipfile
from tqdm.notebook import tqdm

# Tcia server's client 
from utils.tciaclient import TCIAClient

# Function to print server response #######
def printServerResponse(response):
    if response.getcode() == 200:
        print("Server Returned:\n")
        print(response.read())
        print("\n")
    else:
        print("Error: " + str(response.getcode()))

# Create Client
tcia_client = TCIAClient(baseUrl="https://services.cancerimagingarchive.net/services/v4",resource = "TCIA")

def download_images(patients,patient_serie,collectionID,unzip=False):
    """
    Download images for Breast cancer 
    """
    for patient in tqdm(patients):
        # Find the related study to the patient
        print("Downloading images for patient in zip format:",patient )
        try:
            redl=tcia_client.get_patient_study(collection= collectionID, patientId = patient).read()
            # Extract studyInstance
            StudyInstanceUID = ast.literal_eval(redl.decode('utf-8'))[0]['StudyInstanceUID']
            # Collect series 
            series = tcia_client.get_series(collection= collectionID, studyInstanceUid  = StudyInstanceUID ).read()
            series= ast.literal_eval(series.decode('utf-8'))
            # Find related serie to the predefined description (scaner 1T)           
            t1serieInstanceUID=[serie for serie in series if "t1" in serie[ 'SeriesDescription'] or "T1" in serie[ 'SeriesDescription'] or "IDEAL" in serie[ 'SeriesDescription']  ][0][ 'SeriesInstanceUID']
            patient_serie[patient] =  t1serieInstanceUID
            tcia_client.get_image(seriesInstanceUid = t1serieInstanceUID , downloadPath  ="./images/zipFiles", zipFileName =patient+".zip" )
        except urllib.error.HTTPError as err:
            print("Errror executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())   
        # Download images:
        print("Unziping files for patient:",patient )
        if unzip==True:
            with zipfile.ZipFile('./images/ZipFiles/'+patient+".zip", 'r') as zip_ref:
                zip_ref.extractall("images/"+patient)
        print("Download is done")
    return patient_serie
class ImageDataset:
    patient_serie={}
    patients=[]
    collectionID= "Duke-Breast-Cancer-MRI"
    def __init__(self,patients):
        self.patients = patients
        self.patient_serie= download_images(self.patients,self.patient_serie,self.collectionID)
   