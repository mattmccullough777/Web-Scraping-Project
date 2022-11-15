
from urllib.request import urlopen
from bs4 import BeautifulSoup



#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
print()
##
##
##
##

#This prints the specific box
tablecellrank = soup.findAll("td", attrs = {"class":"a-text-right mojo-header-column mojo-truncate mojo-field-type-rank mojo-sort-column"})
tablecellname = soup.findAll("td", attrs = {"class":"a-text-left mojo-field-type-release mojo-cell-wide"})
tablecellrelease = soup.findAll("td", attrs = {"class":"a-text-left mojo-field-type-date a-nowrap"})
tablecelltotalgross = soup.findAll("td", attrs = {"class":"a-text-right mojo-field-type-money mojo-estimatable"})
tablecelldistributor = soup.findAll("td", attrs = {"class":"a-text-left mojo-field-type-studio"})
#print(tablecells[0].text)



#this prints the first row
#tablecells = soup.findAll("tr")
#print(tablecells[0].text)

#this prints everything in the first 7 rows including the title row
#for cell in tablecells[:7]:
    #print(cell.text)

# counterrank = 0
# countername = 0
# counterrelease = 0
# countertotalgross = 0
# counterdistributor = 0


# for x in range(6):
#     rank = tablecellrank[counterrank].text
#     name = tablecellname[countername].text
#     release = tablecellrelease[counterrelease].text
#     total_gross = tablecelltotalgross[countertotalgross].text
#     distributor = tablecelldistributor[counterdistributor].text

# print(rank)
# print(name)
# print(release)
# print(total_gross)
# print(distributor)




#Bhojwani's answers

movie_rows = soup.findAll('tr')

for x in range(1,6):
    td = movie_rows[x].findAll('td')
    print(td[1].text)
    input() 