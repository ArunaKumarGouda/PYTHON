# Q)1:- Write a pythin program to create a dictionary of hindi words with values as their english translation. Provede user with an option to look it up!.
d = {
    "chuha": "rat",
    "kela": "banana",
    "billi": "cat",
    "kuta": "dog"
}

word = input("Enter hindi word :")
print(d[word])


# Q)2 :- Write a program to input eight numbers from the user and display all the unique numbers(once).
s = set()
n = int(input("Enter number :"))
s.add(int(n))
n = int(input("Enter number :"))
s.add(int(n))
n = int(input("Enter number :"))
s.add(int(n))
n = int(input("Enter number :"))
s.add(int(n))
n = int(input("Enter number :"))
s.add(int(n))
n = int(input("Enter number :"))
s.add(int(n))
n = int(input("Enter number :"))
s.add(int(n))
n = int(input("Enter number :"))
s.add(int(n))
print(s)


# Q)3 :- Can we have a set with 18(int) and '18'(str) as a value in it?
s = set()
s.add(int(18))
s.add("18")
print(s)


#Q)4 :- What will be the length of following set s:
s = set()
s.add(5)          # In python 5 and 5.0 are treated as same value
s.add(5.0)
s.add("5")
print(s, len(s))  # The length of s is 2


# Q)5 :- What is the type if 's'?
s = {}
print(type(s))  #  dict

# Q)6 :- Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the name are unique.
d = {}

friends = input("Enter friends name :")
language = input("Enter language :")
d.update({friends: language})

friends = input("Enter friends name :")
language = input("Enter language :")
d.update({friends: language})

friends = input("Enter friends name :")
language = input("Enter language :")
d.update({friends: language})

friends = input("Enter friends name :")
language = input("Enter language :")
d.update({friends: language})

print(d)
