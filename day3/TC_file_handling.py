file=open("file1.txt","r")
content=file.read()
print(content)
file.close()

file=open("file1.txt","a")
file.write("\nnew lines added\nhere")
file.close()
