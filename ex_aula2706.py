#importação 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#importação do csv
df= pd.read_csv('funcionarios_dados_ti (1).csv', sep= ';')
df

#separar os salario
tempo= df['Salario']
dados= np.array(tempo)
dados

#calcular média
media= np.mean(dados)
media

#calcular mediana
mediana= np.median(dados)
mediana

#calcular a distancia relativa
distancia= (media - mediana) / mediana
distancia