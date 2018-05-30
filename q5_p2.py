import math
import string
import re
from q5_p1 import isPassword

def main():
	while(True):
		string = input("Enter a password: ")
		if(isPassword(string) == False):
			continue
		else:
			break

if __name__ == "__main__":
    main()