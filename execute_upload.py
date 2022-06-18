
import os
import subprocess
from num_files import main
import json
filename = "ola.txt"
APP_FOLDER = 'static/uploads/'
dic = {}

def ex():

    arr = os.listdir(APP_FOLDER)
    #print("array", arr[0])
    n = main()
    file =" "
    args ="python3 create_test_file.py " + "'static/uploads/' " + "50 " + n +" "  + "resultado"
    subprocess.call([args],shell=True)
    #subprocess.call("python3 create_test_file.py static/uploads/ 50 20 resultado",shell=True)
    subprocess.call("python3 svm_model.py train_photos.pkl resultado.pkl -1 > ola.txt ", shell=True)
    file = print_file(filename)[0]
    first = print_file(filename)[1]
    print(file)
    print(first)
    """ file = file.replace("[","")
    file = file.replace("]","") """
    #file.replace(".","")
    #x = file.split(" ")
    x = ''.join(char for char in file if char.isalnum())
    print(x)
    l=""
    for i in range(len(x)):
        l = l + x[i]
    """ for x in l:
        print(x) """
    #return l
    i=0
    for arr in arr:
        if l[i] =="1":
            dic[arr] = "True"
        else:
            dic[arr] = "False"
        i = i+1
    print("dicionario",dic.values())
    toJSON = json.dumps(list(dic.values()))
    data = json.loads(toJSON)
    return data,l,first

def print_file(filename):

    s=""
    f = open(filename,'r')

    first = f.readline()
    #print("1 linha", first)
    for line in f:
        s = s + line
        #str = s.replaceAll("[^a-zA-Z0-9]", " ")
    return s,first

#ex()
