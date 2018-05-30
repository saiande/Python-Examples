import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen("https://finance.google.com/finance/market_news").read()
soup = bs.BeautifulSoup(sauce, "lxml")

d = [[] for x in range(10)]
count = 0
for name in soup.find_all('span', class_ = 'name'):
	d[count].append((name.text.strip('\n')))
	count+= 1

count = 0
for source in soup.find_all('div', class_='byline'):
	for src in source.find_all('span', class_='src'):
		d[count].append((src.text.strip('\n')))
		count += 1
		# print(count)

count = 0
for date in soup.find_all('div', class_='byline'):
	for date1 in source.find_all('span', class_='date'):
		d[count].append((date1.text.strip('\n')))
		count += 1
		# print(count)

# print(d)

thefile = open('top10articles.txt', 'w')
for item in d:
	thefile.write(str(item))
