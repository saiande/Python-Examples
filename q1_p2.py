import csv
import time
import math

def main():
	with open('prices_sample.csv') as f:
		Max = 0
		reader = csv.reader(f)
		for i in reader:
			if(float(i[1]) > float(Max)):
				Max = i[1]
				maxDate = i
		x = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(maxDate[0])))
		print("Max($): " + Max + ", Date: " + x)
	with open('prices_sample.csv') as f1:
		reader1 = csv.reader(f1)
		Min = Max
		count = mean = 0
		for j in reader1:
		 	if(float(j[1]) < float(Min)):
		 		Min = j[1]
		 		minDate = j
		 	count += 1
		 	mean += float(j[1])
		mean /= count
		y = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(minDate[0])))
		print("Min($): " + Min + ", Date: " + y)
		print("Mean($): " + str(mean))

	with open('prices_sample.csv') as f2:
		reader2 = csv.reader(f2)
		diff = [float(d[1]) - mean for d in reader2]
		squared = [s ** 2 for s in diff]
		sd = sum(squared)
		sd /= count
		sq = math.sqrt(sd)
		print("SD: " + str(sd))
	with open('prices_sample.csv') as f3:
		reader3 = csv.reader(f3)
		array = []
		for l in reader3:
			array.append(l[1])
		array = sorted(array)
		middle = len(array) / 2
		# z = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(middle[0])))
		if(count % 2 == 0):
			Sum = float(array[int(middle - 1)]) + float(array[int(middle)])
			median = Sum / 2.0
			print("Median($): " + str(median) )
		else:
			print("Median($): " + str(array[middle]))
	
if __name__ == "__main__":
	main()