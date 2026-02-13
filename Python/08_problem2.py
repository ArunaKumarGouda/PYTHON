# Problem 1 :
# Write a python program to display a user entered name followed by Good Afternoon using input () function.
name = input("Enter a name :")
print(f"Good Afternoon, {name}")


# Problem 2 : 
# Write a program to fill in a letter templete given below with name and date/
#  letter = '''
#         Dear <|Name|>,
#         You are selected!
#         <|Date|>
#         '''
letter = '''
          Dear <|Name|>,
          You are selected!
          <|Date|> 
          '''
print(letter.replace("<|Name|>", "Aruna Kumar Gouda").replace("<|Date|>", "26 Aug 2025"))


# Problem : 3
# Write a program to detect double space in a string.
string = "Aruna Kumar  Gouda"
print(string.find("  ")) # Output is : 11  : if there is no double space then it return -1


# Problem : 4
# Replace the double space from problem 3 with single spaces.
string = "Aruna Kumar  Gouda"
print(string.replace("  ", " "))


# Problem : 5
# Write a program to format the following letter using escape sequences characters.
letter = "Dear Aruna, \n\tYour python language is very nice. \nThanks!"
print(letter)
