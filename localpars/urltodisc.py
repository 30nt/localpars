import urllib.request as res
import csv
from bs4 import BeautifulSoup

q=[]
rows=[]
with open('/home/volodymyr/PycharmProjects/FirstMoney/localpars/Resurs/next.csv','r') as csvfile: #считал из файла ссылки
    reader = csv.reader(csvfile)
    i = 1
    for row in reader:
        print(row[0])
        new_q="https://www.sec.gov"+row[0]
        if new_q.find('Arch')!=-1:
            #q.append(new_q)
            print(new_q)
            # html = res.urlopen(new_q).read()
            # html=str(html)
            # print(html)
            rev = [new_q, ]
            d = open('/home/volodymyr/PycharmProjects/FirstMoney/localpars/Resurs/{}myfile.txt'.format(i),'r')
            for list in d:
                #print(list)
                listcopy=list
                while list.find('revenues') != -1:
                    a = list.partition('revenues')
                    b = a[2].lstrip()
                    if b[0].isdigit():
                        revenues = b[0:12]
                        revenues=revenues.strip()
                        rev.append(revenues)
                        print(rev)
                    list = a[2].lstrip()
                while listcopy.find('shares outstanding') != -1:
                    a = listcopy.partition('shares outstanding')
                    b = a[2].lstrip()
                    if b[0].isdigit():
                        shares = b[0:12]
                        shares = shares.strip()
                        rev.append('sh')
                        rev.append(shares)
                        print(rev)
                    listcopy = a[2].lstrip()
                rows.append(rev)
            i+=1

        print(rows)

with open('/home/volodymyr/PycharmProjects/FirstMoney/localpars/Resurs/next2.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(rows)