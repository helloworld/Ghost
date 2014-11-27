class Node(object):
	"""Node Class"""
	def __init__(self, value):
		self.value = value
		self.children = {}
	def __repr__(self):
		self.print()
		return ""
	def print(self, stng):
		return ""
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
		return ""
	def search(self, stng):
		return ""

from sys import setrecursionlimit; setrecursionlimit(100)
from time import clock

def main():
	root = Node("*")
	root.display()

if __name__ == '__main__':
	main()
