import sys

def cipher( text, key, type ):
    result = ""
    for i in range( len( text ) ):
        char = text[i]
        if char.isalpha() == False:
            if type == 'Enc':
                result += chr( ( ord( char ) + key ) )
            elif type == 'Dec':
                result += chr( ( ord( char ) - key) )
        else:
            if char.isupper():
                if type == 'Enc':
                    result += chr( ( ord( char ) + key - 65 ) % 26 + 65 )
                elif type == 'Dec':
                    result += chr( ( ord( char ) - key - 65 ) % 26 + 65 )
            else:
                if type == 'Enc':
                    result += chr( ( ord( char ) + key - 97 ) % 26 + 97 )
                elif type == 'Dec':
                    result += chr( ( ord( char ) - key - 97 ) % 26 + 97 )
    return result

if __name__ == "__main__":
    if len( sys.argv ) == 4:
        key = int( sys.argv[2] )
        print( f"\n Encrypted text: { cipher( sys.argv[3], key, sys.argv[1] ) }" )