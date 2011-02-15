# Monoalphabetic cipher
# Spaces are retained here, though in actual usage, it's worth removing them to make the encryption stronger.

ALPHASET = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext):
    newtext = ""
    plaintext = plaintext.lower()
    for char in plaintext:
        if char in ALPHASET:
            pos = ALPHASET.find(char)
            try:
                newtext += ALPHASET[pos+3]
            except IndexError:
                pos = pos - 26
                newtext += ALPHASET[pos+3]
        else:
            newtext += char
            
    return newtext
    
def decrypt(codedtext):
    newtext = ""
    codedtext = codedtext.lower()
    for char in codedtext:
        if char in ALPHASET:
            pos = ALPHASET.find(char)
            try:
                newtext += ALPHASET[pos-3]
            except IndexError:
                pos = pos + 26
                newtext += ALPHASET[pos-3]
        else:
            newtext += char
            
    return newtext
    
# tests
if __name__ == '__main__':
    print encrypt("the quick brown roman fox jumped over the lazy ostrogoth dog")
    print decrypt("WKH TXLFN EURZQ URPDQ IRA MXPSHG RYHU WKH ODCB RVWURJRWK GRJ")