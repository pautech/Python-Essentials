#Write a program that will check the employees years in service and office.
#The user will input number for years and in service and the following offices (it, acct, hr)
# check the following conditions


employeeInfoYears=int(input("Enter number of Years in Service: "))
employeeInfoOffices=input("Enter Office (IT,ACCT,HR): ")
office=employeeInfoOffices

if(employeeInfoYears>=10 and office.upper()=="IT"):
    print("Your Bonus is 10,000")
elif(employeeInfoYears<10 and office.upper()=="IT"):
    print("Your Bonus is 5,000")

elif(employeeInfoYears>=10 and office.upper()=="ACCT"):
    print("Your Bonus is 10,000")
elif(employeeInfoYears<10 and office.upper()=="ACCT"):
        print("Your Bonus is 5,000")

elif(employeeInfoYears>=10 and office.upper()=="HR"):
    print("Your Bonus is 10,000")
elif(employeeInfoYears<10 and office.upper()=="HR"):
        print("Your Bonus is 5,000")