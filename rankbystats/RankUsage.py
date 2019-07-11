import json
import xlsxwriter

workbook = xlsxwriter.Workbook('RankUsage.xlsx')
worksheet = workbook.add_worksheet()

data = json.load(open("gf-analytics.json", "r"))

FontFamilyCount = 2


worksheet.write('A1', 'Font Family')


for item in data:
        worksheet.write('A' + str(FontFamilyCount), item["Font Family"])
        print("{}".format(item["Font Family"]))
        FontFamilyCount+=1
 
    

workbook.close()
