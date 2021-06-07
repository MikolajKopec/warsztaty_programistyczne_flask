import sys,os,re
name = None
path = None
abs = None
some_directory=sys.argv[1]
i=2
while i<len(sys.argv):
    x=sys.argv[i]
    if x=="-name":
        x=sys.argv[i+1]
        name=re.compile(x)
        i+=1
    i+=1
def iteracja(directory):
    ls=[]
    for j in os.listdir(directory):
        j=os.path.join(directory,j)
        ls.append(j)
        if os.path.isdir(j):
            ls.extend(iteracja(j))
iteracja(some_directory)