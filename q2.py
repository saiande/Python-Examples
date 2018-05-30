import csv
import math

def main():
	filename = input("What is the file name? ")
	# print(filename)
	with open(filename) as f:
		reader = csv.reader(f)
		sumX = sumY = sumProd = sumXS = sumYS = count = 0
		for i in reader:
			sumX += int(i[0])
			sumY += float(i[1])
			sumProd += int(i[0]) * float(i[1])
			sumXS += int(i[0]) ** 2
			sumYS += float(i[1]) ** 2
			count += 1
		print(sumX, sumY, sumProd, sumXS, sumYS)
		# print(count)
		top1 = (sumX * sumY) / count
		# print(sumX)
		top = sumProd - top1
		# print(top)
		bottom1 = (sumXS) - ((sumX ** 2) / count)
		# print(bottom1)
		bottom2 = float(sumYS) - float((sumY ** 2) / count)
		# print(bottom2)
		bottom = float(math.sqrt(bottom1 * bottom2))
		# print(bottom)
		total = top / bottom
		print(total)


if __name__ == "__main__":
    main()