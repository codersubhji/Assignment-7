#1. Write a python script to display the number of days in a given month number.
month=int(input("Enter month between 1 to 12..:"))
match month:
    case month in (2):
    print("28 or 29 days")
    case month in (1,3,5,7,9,11,12):
    print("31 days")
    case  month in (4,6,8,10):
    print("30 days")
    case_:
    print("sorry you have wrong entered..?")    