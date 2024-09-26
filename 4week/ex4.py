def sumfunc(num):
    sum = 0
    for i in range(num + 1):
       sum += i 
    return sum   
    
       

while(True):
    num = int(input("1이상의 정수를 입력해주세요."))
    if  (num > 0):
        sum = sumfunc(num)
        print(f'1~{num}까지 정수의 합은 {sum} 입니다.')
        break
    else:
        print("다시 입력해주세요")
        