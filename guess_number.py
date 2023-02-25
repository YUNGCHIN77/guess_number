import random
r = random.randint(1, 100)

guess = int(input("從1~100中猜猜看一個數字："))
if guess == r:
        print("猜對囉!好棒棒")
    
while guess != r:
    
    if guess > r:
        print("哈哈哈比答案大")
    else:
        print("哈哈哈比答案小")
        
    guess = int(input("猜猜看一個數字"))
    
    if guess == r:
        print("猜對囉!好棒棒")
        break

