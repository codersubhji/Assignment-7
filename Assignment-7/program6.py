"""6. Write a python program to check whether a given string is a multiword string or single
word string using match case statement"""
strg=eval(input("Enter string ...:"))
match strg:
    case strg  if strg ==' ':
        print("Multiword string")
    case strg if strg != ' ':
        print("single word")
  
      