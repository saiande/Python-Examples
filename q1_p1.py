import csv
import time

def main():
	with open('prices_sample.csv') as f:
		reader = csv.reader(f)
		text_file = open("datetimes.txt", "w")
		for i in reader:
			x = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(i[0])))
			text_file.write(x+"\n")
		text_file.close()
			


if __name__ == "__main__":
    main()