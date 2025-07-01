import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#importação do csv
df= pd.read_csv('pesquisa_satisfacao.csv', sep= ';')
df

#organizar os valores do menos para o maior
df_s= df.sort_values(by='Tempo de Espera (min)', ascending = True)
df_s

#separar só o tempo de espera
tempo= df['Tempo de Espera (min)']
dados= np.array(tempo)
dados

#separar os 25% de clientes com menor tempo de espera
q1= np.percentile(dados, 25)
q1

#filtro de clientes e tempo de espera
cliente= df_s[['Cliente', 'Tempo de Espera (min)']]
cliente_q1= cliente[cliente['Tempo de Espera (min)'] <=q1] #define um criterio para exibir com uma condição de valores abaixo de q1
cliente_q1

#grafico 
cliente_q1.plot(x='Cliente', y='Tempo de Espera (min)', kind='bar')
plt.title('Clientes que tiveram o menor tempo de espera')
plt.xlabel('\ncliente\n')
plt.ylabel('\nTempo de espera\n')
plt.show()


