"""5. Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number."""
num=int(input("Enter any number to check the number is even or odd..:"))
if(num>=0)and(num%2==0):
    print("Saurabh Shukla")
elif(num<0) and(num&1):
    print("Prateek Jain")
else:
    print("Aditya Chaudhary")        