#1
for x in range( 0, 150, 1):
    print(x)
#2    
for x in range( 5, 1000, 5):
    print(x)
#3   
for x in range( 1, 100, 1):
    print(x)
    if x%10==0:
        print("coding dojo")
    elif x%5==0:
        print("Coding")
#4
maximum = int(input(" Please Enter the Maximum Value : "))
Oddtotal = 0
for number in range(1, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, Oddtotal))
#5
for x in range( 2018, 1, -4):
    print(x)
 #6       
lowNum=10
highNum=100
mult=5
for i in range(lowNum,highNum):
    if(i%mult==0):
        print(i)
