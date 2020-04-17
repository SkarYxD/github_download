import os
import urllib.request
import zipfile
 
author = 'SkarYxD'
repository = 'amx_antivirus'
branch = 'master'
output_dir = 'C:\/Users\/JkDev\/Desktop'
 
# Download the repository
download_url = f'https://github.com/{author}/{repository}/archive/{branch}.zip'
download_path = os.path.join(output_dir, f'{repository}.zip')
 
with urllib.request.urlopen(download_url) as response:
    data = response.read()
   
    with open(download_path, 'wb') as f:
        f.write(data)
 
# Unzip
with zipfile.ZipFile(download_path, 'r') as zip_ref:
    zip_ref.extractall(output_dir)
 
# Delete zip file
os.remove(download_path)
 
# Do something with the downloaded files
readme_file = os.path.join(output_dir, f'{repository}-{branch}', 'README')
 
with open(readme_file, 'r') as f:
    print(f.read())
