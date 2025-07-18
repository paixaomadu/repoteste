#importação 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#furto e roubo de veículos ---------------------------------------------------------------
#importação do cvs
df= pd.read_csv('DOMensalEstadoDesde1991.csv', sep= ';', encoding='latin1')
df

#filtro do ano
df_ano= df.loc[(df['ano'] >= 2015)]
df_ano

#juncao do ano e recuperação de veículos
df_rec = df_ano.groupby('ano')['recuperacao_veiculos'].sum().reset_index()
df_rec= df_rec.sort_values(by= 'ano')
df_rec

#grafico de recuperação
df_ano.plot(x='ano', y='recuperacao_veiculos',kind= 'line')
plt.title('Recuperação de veículos')
plt.xlabel('\nAno\n')
plt.ylabel('\nquantidade de veículos\n')
plt.show()

#juncao do ano, furtos e roubos
df_vei = df_ano.groupby('ano')[['furto_veiculos' ,'roubo_veiculo']].sum().reset_index()
df_vei

#grafico dos furtos
df_ano.plot(x='ano', y='furto_veiculos',kind= 'line')
plt.title('Furtos de veículos')
plt.xlabel('\nAno\n')
plt.ylabel('\nquantidade de veículos\n')
plt.show()

#grafico de roubo
df_ano.plot(x='ano', y='roubo_veiculo',kind= 'line')
plt.title('Roubo de veículos')
plt.xlabel('\nAno\n')
plt.ylabel('\nquantidade de veículos\n')
plt.show()

#relação entre furtos e recuperação de veículos
plt.scatter(df_ano['furto_veiculos'] , df_ano['recuperacao_veiculos'])
plt.show() 

#relação entre roubos e recuperação 
plt.scatter(df_ano['roubo_veiculo'] , df_ano['recuperacao_veiculos'])
plt.show()

#array, média, mediana e distância de recuperação
array1= df_ano['recuperacao_veiculos']
dados1= np.array(array1)

media= np.mean(dados1)
media

mediana= np.median(dados2)
mediana

distancia= (media - mediana) / mediana *100
distancia

#array, média, mediana e distância de roubo
array2= df_ano['roubo_veiculo']
dados2= np.array(array2)

media= np.mean(dados2)
media

mediana= np.median(dados2)
mediana

distancia= (media - mediana) / mediana *100
distancia

#array, média, mediana e distância de furto
array3= df_ano['furto_veiculos']
dados3= np.array(array3)




#apreensão de menor ---------------------------------------------------------------
#importação 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#importação do cvs
df= pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseMunicipioMensal.csv', sep= ';', encoding='latin1')
df

#filtro dos municipios da baixada
df_baixada = df.loc[df['fmun'].isin(['Belford Roxo','Duque de Caxias','Guapimirim','Itaguaí','Japeri','Magé','Mesquita','Nilópolis','Nova Iguaçu','Paracambi','Queimados','São João de Meriti','Seropédica'])]
df_baixada

#juncao dos municipios da baixada e apreensao de menor
df_apre = df_baixada.groupby('fmun')['aaapai' ].sum().reset_index()
df_apre= df_apre.sort_values(by= 'aaapai')
df_apre

#separar só as apreensoes
apre= df_apre['aaapai']
dados= np.array(apre)
dados.sort() #sort serve para ordenar do menor para o maior
dados

#quartil
q3= np.percentile(dados, 75)
q3

#condição
df_maior= df_apre.loc[(df_apre['aaapai'] >= q3)]
df_maior

df_apre.tail(5) #tail para pegar os 5 últimos

#grafico de roubo
df_apre.plot(x='fmun', y='aaapai', kind= 'barh')
plt.title('Apreensão de menores')
plt.xlabel('\nQuantidade de apreensões\n')
plt.ylabel('\nMunicípios\n')
plt.show()

#array, média, mediana e distancia de apreensões
array= df_apre['aaapai']
dados= np.array(array)

media= np.mean(dados)
media

mediana= np.median(dados)
mediana

distancia= (media - mediana) / mediana *100
distancia


#estelionato ---------------------------------------------------------------
#importação 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#importação do cvs
df= pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', sep= ';', encoding='latin1')
df

#filtro de municipio e ano
df_rj= df.loc[(df['munic'] == 'Rio de Janeiro') & (df['ano'] >= 2020)]
df_rj

#junção do ano, municipio e estelionato
df_rj = df_rj.groupby(['ano', 'cisp'])[['estelionato', 'registro_ocorrencias']].sum().reset_index()
df_rj= df_rj.sort_values(by= 'ano')
df_rj

#grafico 
df_rj.plot(x='ano', y='estelionato',kind= 'line')
plt.title('Evolução de registro de estelionato no RJ')
plt.xlabel('\nAno\n')
plt.ylabel('\nquantidade de registros\n')
plt.show()

#array, média, mediana e distancia do estelionato
array= df_rj['estelionato']
dados= np.array(array)

media= np.mean(dados)
media

mediana= np.median(dados)
mediana

distancia= (media - mediana) / mediana *100
distancia

#array de delegacia
delegacia= df_rj['cisp']
dados= np.array(delegacia)

#quartil
q3= np.percentile(dados, 75)
q3

#condição e criação de uma nova coluna (ano/cisp)
df_dele= df_rj.loc[(df_rj['estelionato'] >= q3)]
df_dele= df_dele.sort_values(by= 'estelionato')
df_dele['ano']= df_dele['ano'].astype(str)
df_dele['cisp']= df_dele['cisp'].astype(str)
df_dele['ano/cisp']= df_dele['ano'] + '/' + df_dele['cisp']
df_dele

#grafico 
df_dele.head(10).plot(x='ano/cisp', y='estelionato',kind= 'bar')
plt.title('Delegacias com mais registros nos últimos 5 anos')
plt.xlabel('\nAno/DP\n')
plt.ylabel('\nquantidade de registros\n')
plt.show()


#crimes violentos na regiao dos lagos ---------------------------------------------------------------
#importação 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#importação do cvs
df= pd.read_csv('https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv', sep= ';', encoding='latin1')
df

#filtro das regiões dos lagos
df_lagos = df.loc[df['munic'].isin(['Araruama', 'Arraial do Cabo', 'Armação dos Búzios', 'Cabo Frio', 'Iguaba Grande', 'São Pedro da Aldeia', 'Saguarema'])]
df_lagos

#junção do ano, municipio e estelionato
df_vio = df_lagos.groupby('munic')[['hom_doloso', 'lesao_corp_morte', 'latrocinio',  'hom_por_interv_policial', 'tentat_hom', 'lesao_corp_dolosa','estupro']].sum().reset_index()
df_vio

#criação de uma nova coluna
df_vio['Crimes violentos']= df_vio['hom_doloso'] + df_vio['lesao_corp_morte'] + df_vio['hom_por_interv_policial']+df_vio['latrocinio']+ df_vio['tentat_hom']+ df_vio['lesao_corp_dolosa']+ df_vio['estupro']
df_vio

#array dos crimes
crimes= df_vio['Crimes violentos']
dados= np.array(crimes)

#quartil
q1= np.percentile(dados, 25)
q1

#condição menor que 25%
df_maior= df_vio.loc[(df_vio['Crimes violentos'] <= q1)]
df_maior=df_maior[['munic', 'Crimes violentos']]
df_maior

#condição maior que 25%
df_maior= df_vio.loc[(df_vio['Crimes violentos'] >= q1)]
df_maior=df_maior[['munic', 'Crimes violentos']]
df_maior= df_maior.sort_values(by= 'Crimes violentos')
df_maior