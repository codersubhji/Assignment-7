"""4. Write a program which takes user's age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen."""
age=int(input("Enter any age to check what a category of Human...:"))
if(0<age<=10):
    print("Kid...")
elif(10<age<=20):
    print("Teen")
elif(20<age<=40):
    print("young..")
elif(40<age<60):
    print("Experienced...")
else:
    print("Senior Citizen...")                