import sys

if __name__ == "__main__":
    if len( sys.argv ) == 4:
        if sys.argv[2] == '+':
            print( f"\n { sys.argv[1] } + { sys.argv[3] } = { int( sys.argv[1] ) + int( sys.argv[3] ) }" )
        elif sys.argv[2] == '-':
            print( f"\n { sys.argv[1] } - { sys.argv[3] } = { int( sys.argv[1] ) - int( sys.argv[3] ) }" )
        elif sys.argv[2] == 'x':    
            print( f"\n { sys.argv[1] } * { sys.argv[3] } = { int( sys.argv[1] ) * int( sys.argv[3] ) }" )
        elif sys.argv[2] == '/':
            print( f"\n { sys.argv[1] } / { sys.argv[3] } = { int( sys.argv[1] ) / int( sys.argv[3] ) }" )
        else:
            print( f"\n { sys.argv[2] } is not a valid operator" )
    else:
        print( f"\n Usage: { sys.argv[0] } <num1> <operator> <num2>" )
        print( f"\n Example: { sys.argv[0] } 10 + 5" )