class Node(object):
	"""Node Class"""
	def __init__(self, value):
		self.value = value
		self.children = {}
	def __repr__(self):
		self.listWords()()
		return ""
	def listWords(self, stng):
		if self.value == '$':
				print(stng.replace('*', ''))
		stng += self.value
		for child in self.children:
				self.children[child].listWords(stng)
	def display(self):
		if self.value == "$": return
		
		print('===== NODE =======')	
		print('--> self.value = ', self.value)	
		print('--> self.children: [', end='');

		for key in self.children:
			if key != "$":
				print(key, sep="", end = ",")
		print(']')
		print('------------------')

		for char in self.children:
			(self.children[char]).display()
	def insert(self, stng):
		if stng == "":
			p = Node('$')
			self.children[p.value] = p
		elif not stng[0].isalpha():
			self.insert(stng[1:])
		elif stng[0] in self.children:
			self.children[stng[0]].insert(stng[1:])
		else:
			p = Node(stng[0])
			self.children[stng[0]] = p
			p.insert(stng[1:])

	def search(self, stng):
		if len(stng) == 0:
			if '$' in self.children:
				return True     
		else:
			if stng[0] in self.children:                                   
				return self.children[stng[0]].search(stng[1:])
		return False

	def contains(self, stng):
		if len(stng) == 0:
			return True           
		else:
			if stng[0] in self.children:                                   
				return self.children[stng[0]].contains(stng[1:])
			return False

	def nextLetter(self, stng):
		if len(stng) == 0:
			List = []
			for key in self.children:
				List.append(key)
			return str(random.choice(List))
		return self.children[stng[0]].nextLetter(stng[1:])


def createTrie(root):
	file = open('dictionary.txt')
	for word in file:
		root.insert(word.lower().strip())
	file.close()
	return root

def humanTurn(root, word):
	word += input('Your Turn: ').lower()[0]
	print(word)
	if(root.search(word) == True):
		if(len(word) > 3):
			print("You Lose.", word, "is a word")
			exit()
	if(root.contains(word) == False):
		print("You Lose.", word, "does not start any word")
		exit()
	return word


def computerTurn(root, word):
	nextLetter = root.nextLetter(word)
	print("Computer Turn: ", nextLetter)
	word += nextLetter
	print(word)
	if(root.search(word) == True):
		if(len(word) > 3):
			print("Computer Loses.", word, "is a word")
			exit()
	if(root.contains(word) == False):
		print("Computer Loses.", word, "does not start any word")
		exit()
	return word

from sys import setrecursionlimit; setrecursionlimit(100)
from time import clock
import random

def main():
	root = Node("*")
	root = createTrie(root)
	word = ""
	while True:
		word = humanTurn(root, word)
		word = computerTurn(root, word)

if __name__ == '__main__':
	main()
