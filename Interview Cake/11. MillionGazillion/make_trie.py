def make_trie(string_set):
	trieRoot = {}

	for string in string_set:
		curNode = trieRoot
		for char in string:
			if char not in curNode.children:
				curNode.children[char] = {}
			curNode = curNode.children[char]
		curNode.children['*'] = None

	return trieRoot

def printWords(trieRoot, curString):
	for letter in trieRoot.children.keys():
		if letter == '*':
			print(curString)
		else:
			printWords(trieRoot.children[letter], curString + letter)