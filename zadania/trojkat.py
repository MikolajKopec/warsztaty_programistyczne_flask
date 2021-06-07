def trojkat(h):
    i=1
    while i<=h:
        print("*"*i)
        i+=1
def od_trojkat(h):
    i=h
    while i>0:
        print("*"*i)
        i-=1
# def piramida(h):
#     i=1
#     x=1
#     s=h-1
#     while i<=h:
#         print(" "*s+"*"*x)
#         x=x+2
#         i+=1
#         s-=1
def piramida(h):
    spacje = range(h-1,-1,-1)
    for i in range(len(spacje)):
        print(" "*spacje[i]+"*"*(1+i*2))
# h = int(input("Wpisz wysokość trójkąta"))
h=3
piramida(h)