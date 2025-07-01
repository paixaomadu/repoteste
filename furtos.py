#importação 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#importação do csv
df= pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', sep= ';', encoding='latin1')
df_sep= df[['ano','munic','roubo_celular']]
df_sep

#filtro das cidades metropolitanas
filtro_cid = df_sep.loc[df_sep['munic'].isin(['Belford Roxo','Duque de Caxias','Guapimirim','Itaboraí','Itaguaí','Japeri','Magé','Maricá','Mesquita','Nilópolis','Niterói','Nova Iguaçu','Paracambi','Queimados','Rio Bonito','Rio de Janeiro','São Gonçalo','São João de Meriti','Seropédica','Tanguá'])]
filtro_cid

#filtrar o ano de 2024
df_24= df_sep.loc[(df_sep['ano']== 2024)]
df_24

#groupby para agrupar as cidades
df_gp = df_sep.groupby('munic')['furto_celular'].sum().reset_index()
df_gp= df_gp.sort_values(by= 'furto_celular' , ascending= False) #sort_values para organizar; ascending= False para colocar em ordem decrescente 
df_gp 

#separar os furtos
furto= df_gp['furto_celular']
dados= np.array(furto)

#calcular média
media= np.mean(dados)
media

#calcular mediana
mediana= np.median(dados)
mediana

#calcular a distancia relativa em porcentagem
distancia= (media - mediana) / mediana * 100 # *100 para tranformar em porcentagem
distancia