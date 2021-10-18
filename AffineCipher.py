#-------------------------------------------------AFFINE CIPHER--------------------------------------------#
'''	The affine cipher is a type of monoalphabetic substitution cipher,
		where each letter in an alphabet is mapped to its numeric equivalent,
		encrypted using a simple mathematical function, and converted back to a letter. 
'''

'''	multiplicative inverse function
		A modular multiplicative inverse of an integer ‘a’ is an integer ‘x’ 
		such that the product ax is congruent to 1 with respect to the modulus m.
		The multiplicative inverse of ‘a’ only exists if ‘a’ and ‘m’ are coprime.
'''
def modinv(a, m):
	for x in range(1,m):
		if(((a%m) * (x%m)) % m == 1):
			return x 
	return -1


'''	affine cipher encryption function
		It uses modular arithmetic to transform the integer that each plaintext
		letter corresponds to into another integer that corresponds to cipher text letter.
		Encryption function for single letter is :

		E(X) = (ax + b) mod m
		modulus m : weight of alphabet
		a and b : cipher keys
'''

def affine_encrypt(text, key):
	return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
				+ ord('A')) for t in text.upper().replace(' ', '') ])


'''	affine cipher decryption function
		In deciphering the ciphertext, we must perform the opposite functions
		on the ciphertext to retrieve the plaintext. In this we convert each of the
		encrypted text into integer values.
		Decryption function is :

		D(x) = a^-1(x - b)mod m ,m=26
		a^-1 : modular multiplicative inverse of a modulo m
		1 = aa^-1 mod m
'''

def affine_decrypt(cipher, key):
	return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
# 					% 26) + ord('A')) for c in cipher ])


def main():
	while(True):
		print(
				'------------AFFINE CIPHER-----------\n'
				'\t1. Encrypt\n'
				'\t2. Decrypt\n'
				 '-----------------------------------\n'
		)
		ch = int(input('Enter your choice(0 to exit) : '))
		if ch == 0:
			break
		elif ch == 1:
			user_input = input("Enter some Text : ")
			key = list(map(int,input("Enter values for a and b : ").split()))
			affine_encrypted_text = affine_encrypt(user_input, key)
			print('\tEncrypted Text :',( affine_encrypted_text ))
		elif ch == 2:
			user_input2 = input("Enter text to decrypt : ")
			key = list(map(int,input("Enter values for a and b : ").split()))
			print('\tDecrypted Text :',(affine_decrypt(user_input2, key) ))


if __name__ == '__main__':
	main()
