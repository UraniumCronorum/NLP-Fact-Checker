from urllib2 import urlopen
from bs4 import BeautifulSoup
import time
import datetime

html = urlopen('https://en.wikipedia.org/wiki/List_of_current_NBA_team_rosters').read()

soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table', class_='toccolours')

def date2ts(dateStr):
    dt = datetime.datetime.strptime(dateStr, '%Y-%m-%d')
    return int(time.mktime(dt.timetuple()))

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
            #print 'playsfor('+name+','+team+')'
            height = cols[3].contents[1].split('(')[1].strip(')').split()[0].strip()
            weight = cols[4].contents[0].split()[0].strip()
            age    = cols[5].contents[0].strip()
            age = date2ts(age[:4] + '-' + age[5:7] + '-' + age[8:10])
            print  'height('+name+','+height+')'
            print 'weight('+name+','+weight+')'
            print 'age('+name+','+str(age)+')'
            raw_input()
