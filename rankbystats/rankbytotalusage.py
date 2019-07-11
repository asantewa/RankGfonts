import sys
import csv
import operator

data = csv.reader(open('RankU.csv', 'r'), delimiter=",")

sortedlist = sorted(data, key=operator.itemgetter(1), reverse=True)

with open("RankedFonts.csv", "w") as f:
    fileWriter = csv.writer(f, delimiter=',')
    for row in sortedlist:
        fileWriter.writerow(row)


