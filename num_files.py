
import os
def main():
    APP_FOLDER = 'staticz/'
    totalFiles = 0
    totalDir = 0
    arr = os.listdir(APP_FOLDER)
    #print("Womes",arr)
    for base, dirs, files in os.walk(APP_FOLDER):
        for directories in dirs:
            totalDir += 1
        for Files in files:
            totalFiles += 1
    print('numero total files',totalFiles)
    return str(totalFiles)
    #return arr
def main_web():
    APP_FOLDER = 'staticz/'
    totalFiles = 0
    totalDir = 0
    arr = os.listdir(APP_FOLDER)
    #print("Womes",arr)
    for base, dirs, files in os.walk(APP_FOLDER):
        for directories in dirs:
            totalDir += 1
        for Files in files:
            totalFiles += 1
    #print('numero total files',totalFiles)
    return str(totalFiles)
    #return arr

def arr():
    APP_FOLDER = 'static/uploads/'
    totalFiles = 0
    totalDir = 0
    arr = os.listdir(APP_FOLDER)
    #print("Womes",arr)
    for base, dirs, files in os.walk(APP_FOLDER):
        for directories in dirs:
            totalDir += 1
        for Files in files:
            totalFiles += 1
    #print('numero total files',totalFiles)
    #return str(totalFiles)
    return arr

def arr_web():
    APP_FOLDER = 'staticz/'
    totalFiles = 0
    totalDir = 0
    arr1 = os.listdir(APP_FOLDER)
    #print("Womes",arr1)
    for base, dirs, files in os.walk(APP_FOLDER):
        for directories in dirs:
            totalDir += 1
        for Files in files:
            totalFiles += 1
    #print('numero total files',totalFiles)
    #return str(totalFiles)
    #print(",,",arr1)
    return arr1
#main()