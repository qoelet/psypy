# Break the characters down to columns, and then make the ciphertext by reading it top to bottom, left to right

def encrypt(plaintext, k):
    count = 1
    row = 0
    newtext = []
    newrow = []
    colarray = []
    codedtext = ""
    for char in plaintext:
        if ( count % k ) != 0:
            if char != ' ':
                newrow.append(char)
                count += 1
        else:
            newrow.append(char)
            newtext.append(newrow)
            newrow = []
            count += 1
    # append tail chars
    newtext.append(newrow)
    print newtext
    count = 0
    colcount = 0
    while count != k:
        colcount = 0
        for row in newtext:
            try:
                codedtext += row[count]
                colcount += 1
            except IndexError:
                pass
        colarray.append(colcount)
        count += 1
    
    return (codedtext, colarray)
    
def decrypt(codedtext, colarray):
    plaintext = ""
    newtext = []
    count = 0
    
    while len(codedtext) != 0:
        newtext.append(codedtext[0:colarray[count]])
        codedtext = codedtext[colarray[count]:]
        count += 1
        
    count = 0    
    while count != len(newtext):
        for row in newtext:
            try:
                plaintext += row[count]
            except IndexError:
                pass
        count += 1
    return plaintext
    
# tests
if __name__ == '__main__':
    result = encrypt("hellohowareyouyoukenny", 7)
    print result
    result = decrypt(result[0], result[1])
    print result