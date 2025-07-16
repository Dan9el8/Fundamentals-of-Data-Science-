file = open(file='textfile.txt', mode='r')
text = file.readlines()
print(text)
file.close()

#To read the entire file at once we use the read() method instead of readlines()
with open(file='textfile.txt', mode='r') as f:
    text = f.read()
    print(text)

    #To write a file use mode='w'
    with open(file='writefile', mode='w') as f:
        f.write('testing writing out')
