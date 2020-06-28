# Takes a string and given a integer to change the string by the number of key 
# Convert to bult-in unicode and add the key, then use char() to convert the unicode back to string.

def caesarCipherEncryptor(string, key):
	newLetters = []
	newKey = key % 26
	for letter in string:
		newLetters.append(getNewLetter(letter, newKey))
	return "".join(newLetters)

def getNewLetter(letter, key):
	newLetterCode = ord(letter) + key
	return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

	
	
