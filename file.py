

def main():
    filename = "ola.txt"
    um = "1."
    zero =" 0."
    s=""
    v = "imagem verdadeira"
    fs = "imagem falsa"
    f = open(filename,'r')
    for line in f:s=""
    v = "imagem verdadeira"
    fs = "imagem falsa"
    f = open(filename,'r')
    lines = f.readlines()
    last = lines[-2:-1]
    print(str(last))
    for a in last:
        print (a )
    res = [int(s) for s in str(last).split() if s.isdigit()] 
    res1 = str(last).count("1.")
    print(res1)
    """ s = output()
    print("s",s)
    if s == 0:
        return fs
    if s == 1:
        return v
    #return s """
    """ s = output()
    print("s",s)
    if s == 0:
        return fs
    if s == 1:
        return v
    #return s """
    return s

main()