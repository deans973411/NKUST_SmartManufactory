#HW3-1
#

#寫入檔案1
print('寫入檔案1')
fi = open("./poem.txt","w")
print('開啟檔案./poem.txt')
VAL = '登金陵鳳凰台'
fi.write(VAL)
print("寫入內容-", VAL)
fi.close()
print("檔案已關閉")


#寫入檔案2
print('寫入檔案2')
file1 = open("./output1.txt","w")
file1.write('天氣很棒')
file1.write('!  '+'你好嗎?')
file1.close()

file2 = open("./output2.txt","w")
print('請輸入10個數字以輸入到文件內')
for i in range(1, 11, 1):
    s= input('輸入第' + str(i) + '個數')
    file2.write(s+',')
file2.close()


#讀取檔案1
'''
開啟檔案:使用open()函數建立檔案物件
讀取檔案:使用檔案物件提供的read(),readline(),readlines()方法讀取
關閉檔案:使用檔案物件提供的close()方法關閉檔案
'''
print('讀取檔案1')
fi = open("./output2.txt","r")
content = fi.read()
print(content)

str1 = fi.read(6)
print(str1)
fi.close
