import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('CARAMELO.csv', sep= ';')

df['Valor de Venda']= df['Valor de Venda'].str.replace(',','.').astype(float)
print(df['Valor de Venda'].dtype)

#valor de venda por cidades do RJ
df_rj= df.loc[df['Estado Loja']== 'RJ']
df_cid_rj = df_rj.groupby('Cidade Loja')['Valor de Venda'].sum().reset_index()
df_cid_rj= df_cid_rj.sort_values(by= 'Valor de Venda', ascending= True)
df_cid_rj

#_______________________________________________________________________________

#Valor de venda por cidade da loja
df_cl = df.groupby('Cidade Loja')['Valor de Venda'].sum().reset_index()
df_cl= df_cl.sort_values(by= 'Valor de Venda', ascending= True)
df_cl

#_______________________________________________________________________________

#média de venda por categoria de produto
df_pr = df.groupby('Categoria Produto')['Valor de Venda'].mean().reset_index()
df_pr= df_pr.sort_values(by= 'Valor de Venda', ascending= True)
df_pr

#________________________________________________________________________________

#Valor de marca que venda de marcas que vendem produtos eletronicos
df_eletronico= df.loc[df['Categoria Produto']== 'Eletrônicos']
df_eletronico = df_eletronico.groupby('Marca')['Valor de Venda'].sum().reset_index()
df_eletronico= df_eletronico.sort_values(by= 'Valor de Venda', ascending= True)
df_eletronico

#_________________________________________________________________________________

#para criar graficos
df_eletronico.plot(kind='bar', x= 'Marca', y= 'Valor de Venda') #kind= tipo, x é o eixo que não tem alteração, y é o eixo que te alteração
plt.xlabel('\nMarcas Produto') #nome para o eixo x
plt.ylabel('\nValor de venda\n') #nome do eixo y
plt.title('Valor de venda por marca') #titulo
plt.show()