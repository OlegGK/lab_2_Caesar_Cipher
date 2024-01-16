# Caesar cipher - Decryption without knowing encryption key

# frequency_of_letters_in_percent = {'A': 8.08, 'B': 1.67, 'C': 3.18, 'D': 3.99, 'E': 12.56,
# 									'F': 2.17, 'G': 1.80, 'H': 5.27, 'I': 7.24, 'J': 0.14,
# 									'K': 0.63, 'L': 4.04, 'M': 2.60, 'N': 7.38, 'O': 7.47,
# 									'P': 1.91, 'Q': 0.09, 'R': 6.42, 'S': 6.59, 'T': 9.15,
# 									'U': 2.79, 'V': 1.00, 'W': 1.89, 'X': 0.21, 'Y': 1.65,
# 									'Z': 0.07}

letters_numbers = {'A': 0, 'a': 0, 'B': 1, 'b': 1, 'C': 2, 'c': 2, 'D': 3, 'd': 3,
							'E': 4, 'e': 4, 'F': 5, 'f': 5, 'G': 6, 'g': 6, 'H': 7, 'h': 7,
							'I': 8, 'i': 8, 'J': 9, 'j': 9, 'K': 10, 'k': 10, 'L': 11, 'l': 11,
							'M': 12, 'm': 12, 'N': 13, 'n': 13, 'O': 14, 'o': 14, 'P': 15, 'p': 15,
							'Q': 16, 'q': 16, 'R': 17, 'r': 17, 'S': 18, 's': 18, 'T': 19, 't': 19,
							'U': 20, 'u': 20, 'V': 21, 'v': 21, 'W': 22, 'w': 22, 'X': 23, 'x': 23,
							'Y': 24, 'y': 24, 'Z': 25, 'z': 25}

def get_unique_letters(text = 'test'):
	unique_symbols_in_text = set(text)
	upper_lower_case_letters_in_text = [letter for letter in unique_symbols_in_text if letter.isalpha()]
	all_letters_in_lower_case = [letter.lower() for letter in upper_lower_case_letters_in_text]
	unique_letters_in_text = set(all_letters_in_lower_case)
	# print(unique_letters_in_text)

	return unique_letters_in_text

def get_amount_of_letters_in_text(text = 'text'):
	letters_amount = 0
	for symbol in text:
		if symbol.isalpha():
			letters_amount += 1

	return letters_amount

def get_most_frequent_letter_in_text(encrypted_text = 't'):
	uniq_letters = get_unique_letters(encrypted_text)
	most_frequent_letter = ''
	total_number_of_letters = get_amount_of_letters_in_text(encrypted_text)
	uniq_letters = get_unique_letters(encrypted_text)
	separated_letters = [letter.lower() for letter in encrypted_text if letter.isalpha()]
	max_value = 0
	for letter in uniq_letters:
		letter_frequency_in_percent = separated_letters.count(letter) / total_number_of_letters
		
		if max_value < letter_frequency_in_percent:
			max_value = letter_frequency_in_percent
			most_frequent_letter = letter

	print("Most frequent letter in encrypted text:", most_frequent_letter)

	return most_frequent_letter


def find_shift_n(encrypt_text = 'text'):
	most_frequent_letter = get_most_frequent_letter_in_text(encrypt_text)
	most_frequent_letter_in_EN_text = 'e'
	shift_n = letters_numbers[most_frequent_letter] - letters_numbers[most_frequent_letter_in_EN_text]
	print("Found key for sipher:", shift_n)

	return shift_n


def decrypt_text(encrypted_text = 'test'):
	key = find_shift_n(encrypted_text)
	decrypted_text = ''
	decrypt_letter = ''	
	decrypt_letter_number = 0
	
	for symbol in encrypted_text:
		if symbol.isalpha():
			decrypt_letter_number = (letters_numbers[symbol] - key) % 26
			target_value_in_letters_numbers = [i for i in letters_numbers if letters_numbers[i] == decrypt_letter_number]
			decrypt_letter = target_value_in_letters_numbers[0]

			if symbol.islower():
				decrypted_text += decrypt_letter.lower()
			if symbol.isupper():
				decrypted_text += decrypt_letter.upper()
		else:
			decrypted_text += symbol
			
	return decrypted_text


# Cipher:
# Khoor Zruog ! Frqjudwxodwlrqv, brx kdyh vxffhvvixoob ghfubswhg ph ! Kdyh ixq zlwk wklv sxccoh

# Decrypted text:
# Hello World ! Congratulations, you have successfully decrypted me ! Have fun with this puzzle

# encrypted_string = input("Enter encrypted string of text: ")
encrypted_string = 'Khoor Zruog ! Frqjudwxodwlrqv, brx kdyh vxffhvvixoob ghfubswhg ph ! Kdyh ixq zlwk wklv sxccoh'

decrypted_text = decrypt_text(encrypted_string)
print("===Result of decryption===:")
print(decrypted_text)





