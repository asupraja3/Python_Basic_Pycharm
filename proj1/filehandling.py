f = open('mydata.txt', 'r')
#print(f.read())
print(f.readline())#reads one line
print(f.readlines())#reads all lines and returns  a list
fdata = f.readlines()
## Writing to a file
f1 = open('abc','w')
f1.write('some data\n')
f1.write('some more data\n')

## Appending to a file
f1.write('another line\n')
#write from mydata.txt to abc
for i in fdata:
    f1.write(i)
#close the file
f1.close()
f.close()