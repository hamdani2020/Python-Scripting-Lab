import requests
import os
import shutil
from datetime import datetime


# Clean Up Previous Directory
if os.path.exists('hamdani_gandi'):
    try:
        shutil.rmtree('hamdani_gandi')
        print(f"Directory '{hamdani_gandi}' has been removed successfully.")
    except Exception as e:
        print(f"Error{e}")


# Create a New Directory
download_folder = 'hamdani_gandi'
if not os.path.exists(download_folder):
    os.makedirs('hamdani_gandi')
    print(f"Directory: {download_folder} created")

# Define the Local File Path
local_file_path = os.path.join(download_folder, "hamdani_gandi.txt")

# Download the File
url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"
response = requests.get(url)


if response.status_code == 200:
    print(f"File successfull download.")
    with open(local_file_path, 'wb') as file:
        file.write(response.content)
        print("File saved successfully.")
else:
    print(f"Failed to download file. Status code :{reponse.status_code}")


# Overwrite File Content
user_input = input("Describe what you have learned so far in a sentence. ")
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")


with open(local_file_path, "w") as file:
    file.write(user_input + "\n")
    file.write(f"Last modified on: {current_time}")
    print("File successfully modified")


# Display the Updated File Content
with open(local_file_path, 'r') as file:
    print("\nYou Entered: ",end='')
    print(file.read())
