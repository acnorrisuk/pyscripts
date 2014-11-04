# reading from txt file

print("opening and closing file...")
text_file = open("read_it.txt", "r")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print("\nReading entire file...")
text_file = open("read_it.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()


print("\nReading line 1 only...")
text_file = open("read_it.txt", "r")
print(text_file.readline(6))
text_file.close()

print("\nReading all as a list...")
text_file = open("read_it.txt", "r")
lines = text_file.readlines()
print(lines)
text_file.close()

print("\nHow many lines are there?")
text_file = open("read_it.txt", "r")
lines = text_file.readlines()
print(len(lines))
text_file.close()

print("\nLooping through lines...")
text_file = open("read_it.txt", "r")
for line in text_file:
    print(line)

text_file.close()

input("exit")


