import pandas as pd

df = pd.read_csv("wine-ratings-small.csv", index_col=0)
sql_tmpl = """INSERT INTO ratings(name, rating, region) VALUES("%s", "%s", "%s");\n"""
sql_file = open("populate.sql", "a")

for _, row in df.iterrows():
    sql_file.write(sql_tmpl % (row['name'], row['rating'], row['region']))
    #print(row)
