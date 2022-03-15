for x in range(-100,100):
    print(x, "IF1")
    if x % 13 == 0 and x % 2 == 0:
        print(x ** 2)	
        a = str(x).split()
        print(a,"IF3")
    for n in range(-100,100,7):
        if n % 2 != 0:
            print(n, "IF2")
            b = str(n).split()
            print(b, "IF4")
	 
