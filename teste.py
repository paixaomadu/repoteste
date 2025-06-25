import numpy as np

lista= [12,15,17,20,30,25,28,22,40,35]

dados= np.array(lista) 
dados.sort() #sort serve para ordenar do menor para o maior
dados

q1= np.percentile(dados, 25) #percentile serve para delimitar a distribuição de dados por porcentagem
q2= np.percentile(dados, 50)
q3= np.percentile(dados, 75)

