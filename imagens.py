from bs4 import *
import requests
import os
import glob
 
# CREATE FOLDER
def folder_create(images):
    
    folder_name = 'staticz'
    #os.mkdir(folder_name)
    download_images(images, folder_name)
"""  try:
    folder_name = 'staticzzz'
    # folder creation
    os.mkdir(folder_name)

# if folder exists with that name, ask another name
except:
    print("Folder Exist with that name!")
    folder_create() """

 
 
# DOWNLOAD ALL IMAGES FROM THAT URL
def download_images(images, folder_name):
    # initial count is zero
    count = 0
 
    #print(f"Total {len(images)} nr images!")
 
    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                image_link = image["data-srcset"]
                 
            except:
                try:
                    image_link = image["data-src"]
                except:
                    try:
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            image_link = image["src"]
 
                        except:
                            pass

            try:
                r = requests.get(image_link).content
                try:
 
                    r = str(r, 'utf-8')
 
                except UnicodeDecodeError:
 
                    with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
                        f.write(r)
 
                    # counting number of image downloaded
                    count += 1
            except:
                pass
 
        if count == len(images):
            print("All Images Downloaded!")
             
        # if all images not download
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")
 
# MAIN FUNCTION START
def main(url):
   
    # content of URL
    r = requests.get(url)
 
    # Parse HTML Code
    soup = BeautifulSoup(r.text, 'html.parser')
 
    # find all images in URL
    images = soup.findAll('img')
    
    
    files = glob.glob('staticz/*')
    for f in files:
        os.remove(f)
    # Call folder create function
    folder_create(images)

#main(url)