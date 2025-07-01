#importação 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#importação do csv
df= pd.read_csv('dados_saude_estilo_vida.csv', sep= ',', encoding='latin1')
df

#graficos
plt.scatter(df['Atividade FÃ­sica (min/dia)'], df['IMC'])

plt.scatter(df['NÃ­vel de Estresse'], df['Horas de Sono'])