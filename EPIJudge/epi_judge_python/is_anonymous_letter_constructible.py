from collections import Counter

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # Implement this placeholder.
    char_freq = Counter(letter_text)
    for x in magazine_text:
    	if x in char_freq:
    		char_freq[x] -= 1
    		if char_freq[x] == 0:
    			char_freq.pop(x)
    		if not char_freq:
    			return True

    return letter_text == ""


from sys import exit

from test_framework import generic_test, test_utils

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
