
import requests 
import pandas as pd 

# We are storing url of dataset
folder = "dataset/"
url_features = 'https://wiki.cancerimagingarchive.net/download/attachments/70226903/Clinical_and_Other_Features.xlsx?api=v2'
url_image_features= 'https://wiki.cancerimagingarchive.net/download/attachments/70226903/Imaging_Features.xlsx?api=v2'
features_filename = 'Clinical_and_Other_Features.xlsx'
image_features_filename = 'Imaging_Features.xlsx'
prediction_filename='predictions.xlsx'

def download_files():
    """
    Download xlsx files from the cancer imaging archive
    """
    # We are creating a requests variable with the above url
    r = requests.get(url_features, allow_redirects=True)
    r_images = requests.get(url_image_features, allow_redirects=True)
    # We are writing the content of above request to a file
    open(folder+features_filename, 'wb').write(r.content)
    open(folder+image_features_filename, 'wb').write(r_images.content)
    

def make_table():
    """
    Extract all features together from both files and concatenate them in one table 
    """
    print("Reading dataframes...")
    clinical_df = pd.read_excel(open(folder+features_filename, 'rb'),header=[0,1])[1:]
    images_df = pd.read_excel(open(folder+image_features_filename, 'rb'),header=0,index_col="Patient ID")
    test_df = pd.read_excel(open(prediction_filename, 'rb'),header=0,index_col="Patient ID")
    print("Droping columns with only nan values...")
    # Drop columns that contain only nan values
    clinical_df.dropna(axis=1,how='all',inplace=True)
    images_df.dropna(axis=1,how='all',inplace=True)
    
    print("Extract clinical features...")
    dict_features={i:[] for i, j in clinical_df.columns}
    for i, j in clinical_df.columns:
        dict_features[i].append(j)
        
    # Combine headers in clinical data 
    clinical_df.columns = [f'{j}' for i, j in clinical_df.columns]
    print("Set index...")
    # set index for clinical data
    clinical_df.rename(columns={'Patient Information,Patient ID':'Patient ID'},inplace=True)
    clinical_df.set_index('Patient ID',inplace=True)
    print("Done...")
    return clinical_df, images_df, test_df, dict_features
