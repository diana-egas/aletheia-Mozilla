import shutil
import os
APP_FOLDER = 'static/uploads'
def main ():
    shutil.rmtree(APP_FOLDER)
    os.mkdir(APP_FOLDER)
main()