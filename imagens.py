from bs4 import *
import requests
import os
import glob
 
# CREATE FOLDER
def folder_create(images):
    
    folder_name = 'staticz'
    #os.mkdir(folder_name)
    # image downloading start
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
 
    # print total images found in URL
    print(f"Total {len(images)} Image Found!")
 
    # checking if images is not zero
    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                # In image tag ,searching for "data-srcset"
                image_link = image["data-srcset"]
                 
            # then we will search for "data-src" in img
            # tag and so on..
            except:
                try:
                    # In image tag ,searching for "data-src"
                    image_link = image["data-src"]
                except:
                    try:
                        # In image tag ,searching for "data-fallback-src"
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            # In image tag ,searching for "src"
                            image_link = image["src"]
 
                        # if no Source URL found
                        except:
                            pass

            try:
                r = requests.get(image_link).content
                try:
 
                    # possibility of decode
                    r = str(r, 'utf-8')
 
                except UnicodeDecodeError:
 
                    # After checking above condition, Image Download start
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
 
 
# take url
#url = input("Enter URL:- ")
 
# CALL MAIN FUNCTION
#main(url)