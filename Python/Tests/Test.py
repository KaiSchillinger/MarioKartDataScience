import pandas as pd

# Dateiname für den Datensatz
DATAFILE = '../CSV_DATA/data.csv'
ZIELFILE = '../CSV_DATA/data_test.csv'

strecken = pd.read_csv('../../Zusatzdaten/strecken_cups.csv')

df1 = pd.read_csv(DATAFILE)
df2 = pd.read_csv(ZIELFILE)

print(strecken)

# df1.info()
# df1.info()