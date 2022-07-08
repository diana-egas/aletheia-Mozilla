
import os
import subprocess
import re
from num_files import main

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
    file = print_file(filename)
    print(file)
    """ file = file.replace("[","")
    file = file.replace("]","") """
    #file.replace(".","")
    #x = file.split(" ")
    x = ''.join(char for char in file if char.isalnum())
    #print(x)
    l=""
    for i in range(len(x)):
        l = l + x[i]
    for x in l:
        print(x)
    #return l
    i=0
    for arr in arr:
        if l[i] =="1":
            dic[arr] = "Verdadeira"
        else:
            dic[arr] = "Falsa"
        i = i+1
    print("dicionario",dic)
    return dic,l

def print_file(filename):

    s=""
    v = "imagem verdadeira"
    fs = "imagem falsa"
    f = open(filename,'r')
    for line in f:
        s = s + line
        #str = s.replaceAll("[^a-zA-Z0-9]", " ")
        #print("jkcd", s)
    return s

#ex()
