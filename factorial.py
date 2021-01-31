#To find out the factorial of a number
def factorial(num):
    if num>=1:
        return num*factorial(num-1)
    else:
        return 1
num = int(input("Enter a number whose factorial is to be calculated "))
resu = factorial(num)
if num>=0:
    print ("Factorial of the given number",num,"is", resu)
else:
    print ("Invalid Input")
