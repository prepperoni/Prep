#include <unordered_map>
#include <unordered_set>
#include <iostream>

using namespace std;

struct TrieNode {
	unordered_map<char, TrieNode*> children;

	TrieNode() : children() {}
	~TrieNode() {
		for (auto &c : children) {
			delete c.second;
		}
	}
};

TrieNode* make_trie(unordered_set<string> string_set){
	TrieNode* rootNode = new TrieNode();

	for (auto &string : string_set) {
		TrieNode* curNode = rootNode;
		for (auto &letter : string) {
			if (curNode->children.find(letter) == curNode->children.end()) {
				curNode->children[letter] = new TrieNode();
			}

			curNode = curNode->children[letter];
		}
		curNode->children['\0'] = new TrieNode();
	}

	return rootNode;
}

void printWords(TrieNode *node, string s) {
	for (auto &entry : node->children) {
		if (entry.first == '\0') {
			cout << s << endl;
		} else {
			printWords(entry.second, s + entry.first);
		}
	}
}

int main() {
	printWords(make_trie({"granger", "kristina", "bananna"}), "");
}