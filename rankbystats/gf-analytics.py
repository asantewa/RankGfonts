
import requests
import pandas as pd
from bs4 import BeautifulSoup



response = requests.get('https://www.google.com/fonts/stats?key=WebFonts2010')
response.raise_for_status()
soup = BeautifulSoup(response.text, features='lxml')
body = soup.find_all('div', class_="column")



all_data = []
all_data = [i.contents[0].strip() for i in body]

n=6
row_data=[all_data[i:i + n] for i in range(0, len(all_data), n)]


df=pd.DataFrame(row_data)
#df.columns = df.iloc[0]
#df.reindex(df.index.drop(0))
#df.head(50)

headers = df.iloc[0]
new_df = pd.DataFrame(df.values[1:],columns=headers)
new_df.head()



new_df.to_json('gf-analytics.json',orient='records')






