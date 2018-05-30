import math
import string
import re
import sys

def isPassword(string):
	if(len(string) < 8):
		print("False: less than 8 characters")
		return False
	if not(any(c.isdigit() for c in string)):
		print("False: no numbers")
		return False
	if not(any(c.isalpha() for c in string)):
		print("False: no alphabetic letters")
		return False
	special = set('[~!@#$%^&*()_+{}":;\']+$')
	if not(any(c in special for c in string)):
		print("False: no special characters")
		return False
	count = 0
	if(re.findall(r'((\w)\2{2,})', string)):
		print("False: too many consecutive duplicates")
		return False
	for x in range(0, len(string)):
		if(x + 2 < len(string)):
			if(ord(string[x]) + 1 == ord(string[x + 1])):
				if(ord(string[x]) + 2 == ord(string[x + 2])):
					print("False: increasing values of 3")
					return False
	noDuplicates = "".join(set(string))
	if(len(noDuplicates) < len(string)/2):
		print("False: duplicate length not enough")
		return False

def main():
	string = sys.argv[-1]
	isPassword(string)

if __name__ == "__main__":
    main()