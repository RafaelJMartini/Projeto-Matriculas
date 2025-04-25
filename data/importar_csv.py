import pandas as pd

df = pd.read_csv("data/MatriculadosBrasil.csv", sep=';')

print(df.head(10)) 