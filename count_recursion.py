# for i in range(10):
#     print(i+1)
    

def count(num):
    if num > 0:
        num = num - 1
        print(num)
        count(num)
    
count(11)