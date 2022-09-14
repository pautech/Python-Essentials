#Write a program that will accept 3 numbers
#Display the numbers in Descending Order

#Enter first Number : 12
#Enter second Number : 1
#Enter third Number : 3
#Result = 12 3 1
numcon=[]
num1=int(input("Enter first Number: "))
numcon.append(num1)
num2=int(input("Enter Second Number: "))
numcon.append(num2)
num3=int(input("Enter Third Number: "))
numcon.append(num3)
numcon.sort(reverse=True)

print(numcon)


 