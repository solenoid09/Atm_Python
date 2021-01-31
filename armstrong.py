#The following program is to check whether the entered number an Armstrong number
number = int(input("Enter a number to check whether it is an armstrong or not: "))
temp = number
if number>0:    #To find the number is whether is greater than 0 or not
    suma=0
    while temp>0:
        n = temp%10           # To Extract the digit
        suma = suma + (n*n*n) # To store the final sum
        temp = (int)(temp/10) # To minimise the number
    if suma==number:                #To compare both sum and the given input
        print("The above number is an Armstrong Number")
    else:
        print ("The above number is not an Armstrong Number")
else:
    print ("Please Enter a Valid Number")
