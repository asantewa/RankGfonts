import os
import xlsxwriter
import sqlite3

from bs4 import BeautifulSoup

conn = sqlite3.connect('ama.db')
db = conn.cursor()

def prepare_db():
    db.execute("CREATE TABLE if not exists html(description longtext);")
    conn.commit()
    html_to_db()

def html_to_db():
    db.execute("delete from html")
    rootdir = os.getcwd()
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".html"):
                with open(filepath, encoding='utf8') as htmlfile:     #for when default system codec fails to open the data, add the correct codec with an encoding argument
                    soup = BeautifulSoup(htmlfile, 'lxml')
                    for i in soup.find_all('p', class_=False):
                        insert=(f'{i.text}',)
                        db.execute("insert into html values (?)",insert)
    conn.commit()
    db_to_excel()

def db_to_excel():
    workbook = xlsxwriter.Workbook('Desc.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Description')
    descCount = 2
    db.execute("select description from html order by length(description) desc")
    data=db.fetchall()
    for data_for_excel in data:
        worksheet.write('A' + str(descCount), " ")
        descCount += 1
        worksheet.write('A' + str(descCount), data_for_excel[0])
        descCount += 1
    workbook.close()
    conn.close()

prepare_db()
