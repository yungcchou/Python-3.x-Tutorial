a = 18 # Global variable
b = 20 # Global variable
def fun1():
    a = 9 # Local variable
    b += 2
    print( f"global b: {b}" )
    return a

if __name__ == "__main__":
    print( f"Out side of function a: {a}" )
    print( f"Get a value from fun1() a: {fun1()}")
