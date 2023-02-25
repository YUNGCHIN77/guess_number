import random
start = int(input("請輸入隨機數字範圍起始值："))
over = int(input("請輸入隨機數字範圍結束值："))

r = random.randint(start, over)
count = 0
    
while True:
    guess = int(input(f"從{start}~{over}中猜猜看一個數字："))
    count += 1
    if guess == r:
        print("猜對囉!好棒棒")
        print(f"一共猜了{count}次")
        break    
    elif guess > r:
        print("哈哈哈比答案大")
    else:
        print("哈哈哈比答案小")
        

