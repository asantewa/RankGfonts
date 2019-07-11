import json
import xlsxwriter

workbook = xlsxwriter.Workbook('RankCat.xlsx')
worksheet = workbook.add_worksheet()

data = json.load(open("fonts_pub_api.json", "r"))

serifCount = 2
sansSerifCount = 2
displayCount = 2
handwritingCount = 2
monospaceCount = 2

worksheet.write('A1', 'Serif')
worksheet.write('B1', 'Sans Serif')
worksheet.write('C1', 'Display')
worksheet.write('D1', 'Handwriting')
worksheet.write('E1', 'Monospace')

for item in data['items']:

    if item['category'] == "serif":
        worksheet.write('A' + str(serifCount), item['family'])
        print("{}".format(item['family']))
        serifCount+=1
    
    elif item['category'] == "sans-serif":
        worksheet.write('B' + str(sansSerifCount), item['family'])
        print("\t{}".format(item['family']))
        sansSerifCount+=1

    elif item['category'] == "display":
        worksheet.write('C' + str(displayCount), item['family'])
        print("\t{}".format(item['family']))
        displayCount+=1

    elif item['category'] == "handwriting":
        worksheet.write('D' + str(handwritingCount), item['family'])
        print("\t{}".format(item['family']))
        handwritingCount+=1

    elif item['category'] == "monospace":
        worksheet.write('E' + str(monospaceCount), item['family'])
        print("\t{}".format(item['family']))
        monospaceCount+=1

workbook.close()

       

