import requests
import pandas as pd

url = 'https://www.estrategiasdeinversion.com/cotizaciones/indices/ibex-35/1/desc/variacion-porcentual?gclid=CjwKCAjwgr6TBhAGEiwA3aVuIRuVssaDkelirEroGhMwXA9bgAYYLR8BFaAF_btZX0HWjj5JjKnb9xoC44wQAvD_BwE'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
print(df)
df.to_csv('data.csv')