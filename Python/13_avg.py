ch = input("Enter a word which is made of 5 vowels (a, e, i, o, u): ")

count_even = 0
count_odd = 0

if ch.count("a") % 2 == 0:
    count_even += 1
else:
    count_odd += 1

if ch.count("e") % 2 == 0:
    count_even += 1
else:
    count_odd += 1

if ch.count("i") % 2 == 0:
    count_even += 1
else:
    count_odd += 1

if ch.count("o") % 2 == 0:
    count_even += 1
else:
    count_odd += 1

if ch.count("u") % 2 == 0:
    count_even += 1
else:
    count_odd += 1

print("Even number of vowels:", count_even)
print("Odd number of vowels:", count_odd)
