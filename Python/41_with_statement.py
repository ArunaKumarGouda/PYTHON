# The best way to open and close the file automatically is the with statement.

f = open("chapter_1/01_file.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("chapter_1/01_file.txt") as f:
    print(f.read())

# You don't have to explicitly close the file
