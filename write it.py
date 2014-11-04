#Writing to txt

print("Create a txt file with write method")
text_file = open("write_it.txt", "w")

lines = ["HELLO EVERYBODY\n\n"
         "HELLO AGAIN\n"]
         
text_file.writelines(lines)
text_file.close()



