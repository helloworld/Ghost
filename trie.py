class Node(object):
	"""Node Class"""
	def __init__(self, value):
		self.value = value
		self.children = {}
	def __repr__(self):
		self.print()
		return ""
	def listWords(self, stng):
		if self.value == '$':
		        print(stng)
		        
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
		elif stng[0] in self.children:
			self.children[stng[0]].insert(stng[1:])
		else:
			p = Node(stng[0])
			self.children[stng[0]] = p
			p.insert(stng[1:])

	def search(self, stng):
		return ""

from sys import setrecursionlimit; setrecursionlimit(100)
from time import clock

def main():
	root = Node("*")
	root.insert('cat')
	root.insert('catnip')
	root.insert('cats')
	root.insert('catnap')
	root.insert("can't")
	root.insert('cat-x')
	root.insert('dog')
	root.insert('dogs')
	root.insert('dognip')
	root.listWords("")

if __name__ == '__main__':
	main()
