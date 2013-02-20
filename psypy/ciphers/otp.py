# One time pad, Vernam 1917
# key = series of bits as long as the message
# encryption: ciphertext = key XOR msg 
# decription: msg = key XOR ciphertext

import bitarray # pip install bitarray, not a standard library

def encrypt(key, msg):
	# normalizing inputs to bools, XOR in Python is simply !=
	# reuse as decrypt, swapping msg with ciphertext.
	assert len(key) == len(msg)

	c = 0
	ciphertext = []
	while c < len(msg):
		ciphertext.append(msg[c] != key[c])
		c += 1

	return ciphertext

if __name__ == '__main__':
	# create msg
	ba = bitarray.bitarray()
	msg = "hi i am a secret"
	ba.fromstring(msg)
	msg_as_bits = ba.tolist()

	# create a random key as long as msg
	key_len = len(msg_as_bits)
	key = bitarray.bitarray(key_len) # use a random key
	key_as_bits = key.tolist()

	ciphertext = encrypt(key_as_bits, msg_as_bits)
	decrypted = encrypt(key_as_bits, ciphertext)

	# printouts
	print "msg = %s (%s)" % (msg, bitarray.bitarray(msg_as_bits))
	print "key = %s" % bitarray.bitarray(key_as_bits)
	print "encrypted = %s" % bitarray.bitarray(ciphertext)
	print "decrypted = %s (%s)" % (bitarray.bitarray(decrypted).tostring(), bitarray.bitarray(decrypted))
