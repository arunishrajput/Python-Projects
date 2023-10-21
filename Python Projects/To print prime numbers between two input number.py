# To print prime numbers between two input number
FN = int(input('Enter first prime number: '))
LN = int(input('Enter last prime number: '))
num = FN
while num <= LN:
    for i in range(FN,(num//2)+1):
        if num%i==0:
            break
    else:
        print(num)
    num += 1