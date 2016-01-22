# Script to fetch data from http://data.worldbank.org/indicator/SP.POP.TOTL

import lxml.html as LH
import requests

def text(elt):
    return elt.text_content().replace(u'\xa0', u' ').replace('\n',' ').strip()

url = "http://data.worldbank.org/indicator/SP.POP.TOTL"
r = requests.get(url)
root = LH.fromstring(r.content)

#open a file which we will save the data to
f = open('pop_data.txt','w')

# The table didn't seem to have the id you were searching for,
# I've selected it by its class
for table in root.xpath('//table[@class="views-table sticky-enabled cols-7"]'):

#loop through the rows    
    for row in table.xpath('//tr'):
        #write the contents of the header cells separated by a tab
        for header in row.findall('th'):     
            f.write(text(header) + '\t')

        #write the contents of the normal cells as above
        for td in row.findall('td'):
            f.write(text(td) + '\t')

        #write a new line
        f.write('\n')

#close the file    
f.close()
