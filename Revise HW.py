#Class:MDE4-3 Name:Dean
print('Class:MDE4-3 Name:Dean')
'''
Print stars shape 10 times with While command, the value which multplied plus 1 every loop
'''
print('【hsue HW1 Star shape sequence】') 
print('→Print stars shape 10 times with While command, the value which multplied plus 1 every loop:\n') 

i1 = 0   #Define initial value i1
t1 = 10  #Define target valie t1
while i1 <= t1:
    i1 += 1
    print(i1*'*')

#hsue HW2 Shortest 9x9 multplication table(170chr)
print('【hsue HW2 Shortest 9x9 multplication table(170chr)】') 
print('→Nothing to say...:\n') 
y = 1
while y < 10:
    y += 1
    for j in range(y-1, y):
        for i in range(2, 10):
            print('{}x{}={:2} '.format(i, j, i*j), end='')
    print('\n')
    
   

#hsue HW2-1 Varibale multplication table
'''
The variable define initial value and final value, list it down with While command.
'''
print('【hsue HW2-1 Varibale multplication table】') 
print('→The variable define initial value and final value, list it down with While command.:\n') 

[xi2, xf2] = [3, 18] #Define x-axis abscissa initial value xi and final value xf
[yi2, yf2] = [1, 18] #Define y-axis ordinate initial value yi and final value yf
while yi2 <= yf2:
    yi2 += 1
    for y2 in range(yi2-1, yi2):
       for x2 in range(xi2, xf2+1):
            print('{:2}x{:2}={:4} ▍'.format(x2, y2, y2*x2), end="")
    print('\n')

