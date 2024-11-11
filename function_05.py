a = 18 # Global variable
b = 20 # Global variable
def fun1( *args):
    total = 0
    for i in args:
        total += i
    return total

if __name__ == "__main__":
    print(fun1(10, 67, 58,1,2,3)) # 18
