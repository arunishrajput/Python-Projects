# Print first input number of prime numbers

N = int(input('Enter number of prime number to print: '))
count = 0
num = 2
print('first',N,'Prime numbers are : ')
while count<N:
    check = 1
    for i in range (2,num//2+1):
        if num%i==0:
            check = 0
            break
    if check == 1:
        print(num)
        count+=1
    num+=1