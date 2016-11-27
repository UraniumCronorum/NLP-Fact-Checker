from urllib2 import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/List_of_current_NBA_team_rosters').read()

soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table', class_='toccolours')

for table in tables:
    team = ' '.join(table.th.b.contents[0].split()[:-1])
    for row in table.table.find_all('tr'):
        cols = row.find_all('td')
        if cols:
            name = cols[2].a.contents[0].split(',')
            if len(name) == 2:
                name = name[1].strip() + ' ' + name[0].strip()
            elif len(name) == 1:
                name = name[0].strip()
            print 'playsfor('+name+','+team+')'
