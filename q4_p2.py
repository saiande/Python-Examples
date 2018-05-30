from q4_p1 import parse
import operator

def main():
	f = open("top10words.txt", "w")
	d = parse()
	# n_items = take(10, d.iteritems())
	# print(n_items)
	f.write(str(list(d.items())[:10]))


	# for item in d.items(): 
	# 	print("{}\t{}".format(*item))

if __name__ == "__main__":
    main()