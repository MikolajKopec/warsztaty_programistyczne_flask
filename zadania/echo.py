import sys
terminator = "\n"
rev = False
up = False
separator = " "
for i,each in enumerate(sys.argv[1:]):
    if each=="-n":
        terminator = " "
    elif each=="-r":
        rev = True 
    elif each == "-u":
        up = True
    elif each == "-l":
        separator = "\n"
    else:
        break
arg = sys.argv[i+1:]
if rev:
    arg=list(reversed(arg))
if up:
    for i,x in enumerate(arg):
        arg[i] = x.lower()
    arg[0] = arg[0].capitalize()
print(separator.join(arg),end=terminator)
