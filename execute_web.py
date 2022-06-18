import os
import subprocess
import json
from num_files import main_web

filename = "ola.txt"
APP_FOLDER = 'staticz/'

dic = {}

def ex():

    arr = os.listdir(APP_FOLDER)
    #print("array", arr[0])
    n = main_web()
    print("numero files", n)
    file =" "
    args ="python3 create_test_file.py " + "'staticz/' " + "50 " + n +" "  + "resultado"
    subprocess.call([args],shell=True)
    #subprocess.call("python3 create_test_file.py static/uploads/ 50 20 resultado",shell=True)
    subprocess.call("python3 svm_model_web.py train_photos.pkl resultado.pkl -1 > ola.txt ", shell=True)
    file = print_file(filename,n)#[0]

    #print("len file::", len(file))
    int_n= int(n)

    # print ("len[n]", file[x])
    # print ("len[n+1]", file[x+1])
    # print ("len[n+2]", file[x+2])
    last = []
    last_one=[]
    for i in range(int_n,(len(file)-1)):
        last.append(file[i])
        print(file[i])
    last_one = " ".join(last)
        
    print("last len", len(last_one), last_one)
    """ file = file.replace("[","")
    file = file.replace("]","") """
    #file.replace(".","")
    #x = file.split(" ")

    x = ''.join(char for char in last_one if char.isalnum())
    print(x)
    l=""
    #print(len(x))
    for i in range(len(x)):
        l = l + x[i]
    print("l", l)
    #for x in l:
    #return l
    i=0
    print("arr", arr, len(arr), len(l))
    for arr in arr:
        #print("i",i)
        if(i < len(l)):
            if l[i] =="1":
                dic[arr] = "True"
            else:
                dic[arr] = "False"
        i = i+1
    print("dicionario",dic)
    toJSON = json.dumps(list(dic.values()))
    data = json.loads(toJSON)
    #print("data", data, "l", l)

    j=0
    data_t =[]
    for x in file:
        if(j<= int(n)):
            data_t.append(x)   
            j = j+1
    #print("data_te", data_t)       
    return data,l,data_t

def print_file(filename,n):

    s=[]
    first=[]
    second = []
    i=0
    f = open(filename,'r').read().splitlines()
    #print("estou aqui:", first)
    #print("file:", f)
    #print("last", f[int(n)+1])
    for line in f:          
        #print("cada linha", line)
        #first = "ola" #file.readline()
        s.append(line)
        i = i+1
        #str = s.replaceAll("[^a-zA-Z0-9]", " ")
    return s
#ex()
