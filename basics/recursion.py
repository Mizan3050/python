
def rec_func_mult(a,b):
    if(a==0 or b == 0):
        return 0
    if(b == 1):
        return a
    else:
        return a+rec_func_mult(a,b-1)

num_a = int(input("Enter a number you want to multiply: "))
num_b = int(input("Now enter a number you want to multiply to: "))
print(rec_func_mult(num_a, num_b))
