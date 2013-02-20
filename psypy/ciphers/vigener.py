# Vigener cipher, from 16th century

ALPHASET = "abcdefghijklmnopqrstuvwxyz"

def encrypt(k, msg):
	# assumes message only contains alphabets
	encrypted = ""
	k_store = list(k)
	k_store.reverse()

	for c in msg:
		x = ALPHASET.index(c)
		if len(k_store) > 0:
			k_store = list(k)
			k_store.reverse()

		y_c = k_store.pop()
		y = ALPHASET.index(y_c)
		encrypted += (ALPHASET[(x+y) % 26])

	return encrypted

def decrypt(k, msg):
	# assumes message only contains alphabets
	decrypted = ""
	k_store = list(k)
	k_store.reverse()

	for c in msg:
		x = ALPHASET.index(c)
		if len(k_store) > 0:
			k_store = list(k)
			k_store.reverse()

		y_c = k_store.pop()
		y = ALPHASET.index(y_c)
		decrypted += (ALPHASET[(x-y) % 26]) # simple reverse the operation

	return decrypted

if __name__ == '__main__':
	key = "pizza"
	msg = "thisisasecretmessage"

	e =  encrypt(key, msg)
	print e
	d = decrypt(key, e)
	print d