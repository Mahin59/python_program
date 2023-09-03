
def fibo(n):
    if n==1:
        return 0
    if n ==2:
        return 1
    if n > 2:
        return fibo(n-1) + (n-2)
num = 10
for n in range(num):
    print(fibo(n),end=" ")