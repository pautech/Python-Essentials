#1.Create 4 Variables use input function() (Name (string),Math Grade
#(float),Science Grade (float),English Grade (integer), Average (float))
#2. Use input statement
#3.Display the result:
#Name: __________
#Math Grade:_____________
#Science Grade:___________
#English Grade:___________ 
#Average:______________
print("\n")
print("-----Get My Average App-----")
print("\n")
Name=input("Please Input you Name: ")
MathGrade=float(input("Please Input your Math Grade: "))
ScienceGrade=float(input("Please Input your Science Grade: "))
EnglishGrade=float(input("Please Input your English Grade: "))
average=(MathGrade+ScienceGrade+EnglishGrade)/4
print("\n")
print("Hello!! ",Name+"Your General Average is {:.2f}".format(average))
print("\n")