f = open("chapter_1/01_file.txt")

# for Multiple lines
lines = f.readlines()
print(lines, type(lines))


# for single line
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
line4 = f.readline()
print(line4)
line5 = f.readline()
print(line5 == "")


# # using while loop
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()
