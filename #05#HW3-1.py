#HW3-1
#class:MDE4-3 Name:Dean Lin
'''
In this chapter, use 3 type command to control python and file:

    Open file: use 'open()' function create file object
    Read file: use command to read which is file object provide: 'read()', 'readline()', 'readlines'
    Close file: use command to clese file which is file object provide: 'close()'

'''

#Write in file 1
print('Write in file 1')
fi = open("./poem.txt","w")             #Defind 'fi' to open file poem.txt, mode "w"
print('Open file ./poem.txt')
VAL = '登金陵鳳凰台'
fi.write(VAL)                           #File object:  <>.write
print("Write in-", VAL)
fi.close()                              #File object:  <>.close
print("File closed")


#Write in file 2
print('Write in file 2')
file1 = open("./output1.txt","w")
file1.write('Sunny day')
file1.write('!  '+'How are you?')
file1.close()

file2 = open("./output2.txt","w")
print('please type 10 words/numbers in file')
for i in range(1, 11, 1):
    s= input('No.' + str(i) + 'str')
    file2.write(s+',')                  #Write "S" in to file
file2.close()


#Read file 1

print('Read file 1')
fi = open("./output2.txt","r")
content = fi.read()
print(content)

str1 = fi.read(6)                       #print first 6 character to monitor------(+6:count from front/-6:count form last/6:count after first 6 character)
print(str1)
fi.close
