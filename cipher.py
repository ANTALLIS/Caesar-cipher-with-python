print("Hello")
plaintext = input("Input text: ")
key = int(input("key (0 - 25): "))
ciphertext = ""

assert key < 26 and key >= 0, "Key is invalid"
assert plaintext.isalpha() == True, "Only letters please"

plaintext = plaintext.lower()

for i in plaintext:
	tmp = ord(i) + key
	if tmp > 122:
		tmp %= 122
		tmp += 96
	ciphertext += chr(tmp)

print(ciphertext)
