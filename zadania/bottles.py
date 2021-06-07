x=99
for i in range(x,0,-1):
    print("{0} bottles of beer on the wall, {0} bottles of beer.".format(i))
    print("Take one down, pass it around, {} bottles of beer on the wall...".format(i-1))
    if i==1:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, {} bttles of beer on the wall...".format(x))
    print