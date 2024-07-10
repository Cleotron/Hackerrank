# 0,1,1,2,3,5,8...
# input: place (starting from 0), output: fib number

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    print(fibonacci(3)) # 2
    print(fibonacci(5)) # 5