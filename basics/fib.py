
# def fib(num):
#     if(num<=1):
#         return num
#     else:
#         return fib(num-1)+fib(num-2)

def fib(num):
    fib_last = 0
    for i in range(num):
        if(i>1):
            fib_last = fib_last+i
        else:
            fib_last = fib_last + (i-1)
    return fib_last
    
print(fib(9))