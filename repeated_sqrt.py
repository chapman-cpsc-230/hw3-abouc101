from math import sqrt
for n in range(1,60): #This will calculate the number of times to press the Sqrt button.
    r = 2.0 #This is saying the base number, the one we are rooting is 2
    for i in range(n):
        r = sqrt(r) #It is taking the sqrt of r, and changing r to that number
    for i in range(n):
        r = r**2 #Now it is squaring r, to get it back to the same number.
    print ("%d times sqrt and **2: %.16f" % (n,r)) #This is simply telling the user what the outcome is.
enter = raw_input('')
