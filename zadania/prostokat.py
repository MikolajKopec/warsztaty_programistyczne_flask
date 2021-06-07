def prostokat(a,b):
    i = 0
    while i<a:
        print("*"*b)
        i+=1
def pusty_p(a,b):
    i=0
    while i<a:
        if i==0 or i==(a-1):
            print("*"*b)
        else:
            print("*" + " "*(b-2)+"*")
        i+=1
#prostokat(3,4)
pusty_p(4,5)