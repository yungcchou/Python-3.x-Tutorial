import sys

def factorial( n ):
    if n == 0:
        return 1
    else:
        return n * factorial( n - 1 )

if __name__ == "__main__":
    if len( sys.argv ) == 2:
        print( f"\n Factorial of { sys.argv[1] } is { factorial( int( sys.argv[1] ) ) }" )
    else:
        print( f"\n Usage: { sys.argv[0] } <num>" )
        print( f"\n Example: { sys.argv[0] } 5" )