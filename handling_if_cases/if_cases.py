num = int(input()) 
n = num % 2 

if n == 0 and (2<= num <=5): 
    print('Not Weird')
elif n == 0 and (6<= num <=20): 
    print('Weird')
elif n == 0 and num > 20: 
    print("Not Weird")
elif num % 2 != 0: 
    print('Weird')
