# average at given number
n=int(input('enter the number ')) # how many numbers
s=0 #initialize variable
for i in range(1,n+1):
    n1=eval(input('enter the value '))
    s += n1

average=s/n

print(average)
