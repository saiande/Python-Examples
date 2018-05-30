from collections import Counter

def parse():
	dictionary = {}
	f = open("100-0.txt", "r")
	newList = Counter(f.read().split())
	# for item in dictionary.items(): 
	# 	print("{}\t{}".format(*item))
	for i,j in newList.most_common():
		dictionary[i] = j
	print(dictionary)
	return dictionary
	

if __name__ == "__main__":
    parse()