#班級:四模四丙 學號:C107147319 姓名:林鼎鈞
print('班級:四模四丙 學號:C107147319 姓名:林鼎鈞')
'''
以while搭配每次迴圈+1個星號的函數，完成10次星號輸出
'''
print('【hsue HW1 星型數列】') 
print('→以while搭配每次迴圈+1個星號的函數，完成10次星號輸出:\n') 

i1 = 0   #定義初始值i(initial)
t1 = 10  #定義目標值t(target)
while i1 <= t1:
    i1 += 1
    print(i1*'*')

#hsue HW2 最短九九乘法表(170字元)
print('【hsue HW2 最短九九乘法表(170字元)】') 
print('→沒啥好說的...:\n') 
y = 1
while y < 10:
    y += 1
    for j in range(y-1, y):
        for i in range(2, 10):
            print('{}x{}={:2} '.format(i, j, i*j), end='')
    print('\n')
    
   

#hsue HW2-1 可變九九乘法表
'''
以變數定義橫坐標初值與終值，並以while搭配每次迴圈針對縱坐標變數調整初值與終值
，製作出可變乘法表
'''
print('【hsue HW2-1 可變九九乘法表】') 
print('→以變數定義橫坐標初值與終值，並以while搭配每次迴圈針對縱坐標變數調整初值與終值，製作出可變乘法表:\n') 

[xi2, xt2] = [3, 18] #定義Y軸縱坐標初始值yi(initial)與極限值yt(terminal)
[yi2, yt2] = [1, 18] #定義X軸橫坐標初始值xi(initial)與極限值xt(terminal)
while yi2 <= yt2:
    yi2 += 1
    for y2 in range(yi2-1, yi2):
       for x2 in range(xi2, xt2+1):
            print('{:2}x{:2}={:4} ▍'.format(x2, y2, y2*x2), end="")
    print('\n')

