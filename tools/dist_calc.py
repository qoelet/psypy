# Calculate the difference in position for two given alphabets

ALPHASET = "abcdefghijklmnopqrstuvwxyz"

if __name__ == '__main__':
    a = raw_input("Enter first alphabet: ")
    b = raw_input("Enter second alphabet: ")
    
    pos_a = ALPHASET.find(a)
    pos_b = ALPHASET.find(b)
    
    if pos_a > pos_b:
        print "Difference: %d" % (pos_a-pos_b)
    else:
        print "Difference: %d" % (pos_b-pos_a)