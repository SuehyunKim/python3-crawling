import csv

f = open('./covid19_articles.csv', 'r', encoding='CP949')

rdr = csv.reader(f)

next(rdr)
count = 0

for row in rdr:
    if '[속보]' in row[2]:
        print(row[2])
        count += 1

print('속보 기사 개수:', count)

f.close()
