# Q) 1:- write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.
'''
there is one txt file called poem.txt and i write some text here like:

Twinkle twinkle little star
To kese he app log
'''
f = open("chapter_1/poem.txt")
content = f.read()
f.close()

if("Twinkle" in content):
    print("The word Twinkle is present in the content")

else:
    print("The word Twinkle is not present in the content")



# Q) 2:- The game() function is a program lets a user play a game and return the score as an integer. You need to read a file 'Hi-score.txt' which is either blank and contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
import random

def game():
    print("You are playing the game...")
    score = random.randint(1, 62)

    # Fetch the hiscore
    with open("chapter_1/03_hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score: {score}")
    if(score > hiscore):
        # Write this hiscore to the file
        with open("chapter_1/03_hiscore.txt", "w") as f:
            f.write(str(score))
        
    return score
game()


# Q) 3:- Write a progrma to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder from a 13-year old.
def generateTables(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n * i}\n"

    with open(f"chapter_1/multiplicationTables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generateTables(i)



# Q) 4:- A file contains a word "Donkey" multiple times. You need to write a progeam which replace this word with ###### by updating the same file.
word = "Donkey"
with open("chapter_1/Donkey.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("chapter_1/Donkey.txt", "w") as f:
    f.write(contentNew)

print("The word Donkey is successfully replaced as ######. To see this please visit the Donkey.txt")



# Q) 5:- Repeat program 4 for a list of such words to be censored.
words = ["Donkey", "bad", "ganda"]

with open("chapter_1/Donkey1.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("chapter_1/Donkey1.txt", "w") as f:
    f.write(content)

print("Successfully replaced the words")



# Q) 6:- Write a program to mine a log file and find out whether it contains 'python'.

'''
There is a text file contain the name log.txt and there is written some word:

The high level language
platform independent
python is a objected oriented programming language
'''

with open("chapter_1/log.txt", 'r') as f:
    content = f.read()

if("python" in content):
    print("Yes python is present")
else:
    print("No python is not present")



# Q) 7:- Write a program to find out the line number where python is present from ques 6.
'''
There is a text file contain the name log.txt and there is written some word:

The high level language
platform independent
python is a objected oriented programming language
'''
with open("chapter_1/log.txt") as f:
    lines = f.readlines()

lineNumber = 1
for line in lines:
    if("python" in line):
        print(f"python is present in line {lineNumber}")
        break
    lineNumber += 1

else:
    print("No python is not present")



# Q)
