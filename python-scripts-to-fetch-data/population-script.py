from BeautifulSoup import BeautifulSoup
import urllib2
import codecs

response = urllib2.urlopen('http://data.worldbank.org/indicator/SP.POP.TOTL')
html = response.read()
soup = BeautifulSoup(html)

tabulka = soup.find("table", {"class" : "detail-char"})

population = [] # stores all information in this list
for row in tabulka.findAll('tr'):
    col = row.findAll('td')
    prvy = col[0].string.strip()
    druhy = col[1].string.strip()
    population = '%s;%s' % (prvy, druhy)
    records.append(population)

fl = codecs.open('output.txt', 'wb', 'utf8')
line = ';'.join(records)
fl.write(line + u'\r\n')
fl.close()
