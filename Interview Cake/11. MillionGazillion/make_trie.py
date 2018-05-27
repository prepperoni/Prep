class TrieNode:
	def __init__(self):
		self.children = {}

def make_trie(string_set):
	trieRoot = TrieNode()

	for string in string_set:
		curNode = trieRoot
		for char in string:
			if char not in curNode.children:
				curNode.children[char] = TrieNode()
			curNode = curNode.children[char]
		curNode.children['*'] = None

	return trieRoot

def printWords(trieRoot, curString):
	for letter in trieRoot.children.keys():
		if letter == '*':
			print(curString)
		else:
			printWords(trieRoot.children[letter], curString + letter)