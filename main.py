import pandas as pd

#separador incluído como ; porque o arquivo tem isso como padrão, separação das colunas com ;'
#decimal incluído como , porque o arquivo tem isso como padrão, separação dos números com ','
df = pd.read_csv('indicadores-continuidade-coletivos-2020-2029.csv', sep =';', decimal = ',')


#exibir as 5 primeiras colunas 
print(df.head())
#checando quantas linhas e colunas
print(df.shape)

#print ver o nome das colunas 
print(df.columns)

#checar os tipos de dados e valores não nulos
df.info()

#calcular as estatísticas descritivas
print(df.describe())