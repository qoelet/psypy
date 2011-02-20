# Monoalphabetic cipher
# Spaces are retained here, though in actual usage, it's worth removing them to make the encryption stronger.
# Like Caesar, but specify n as the amount to shift

ALPHASET = "abcdefghijklmnopqrstuvwxyz"

def shift(plaintext, n):
    newtext = ""
    plaintext = plaintext.lower()
    for char in plaintext:
        if char in ALPHASET:
            pos = ALPHASET.find(char)
            try:
                newtext += ALPHASET[pos+n]
            except IndexError:
                pos = pos - 26
                newtext += ALPHASET[pos+n]
        else:
            newtext += char
            
    return newtext
    
    
# tests
if __name__ == '__main__':
    # I'm using this to solve the 2nd question on pythonchallenge.com
    secret = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
    print shift(secret, 2)
    print shift("map", 2)