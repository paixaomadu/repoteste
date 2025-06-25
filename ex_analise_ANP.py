import pandas as pd

'''arquivos= ["2020_01.csv", "2020_02.csv", "2021_01.csv", "2022_01.csv", "2022_02.csv", "2023_01.csv", "2023_02.csv", "2024_01.csv", "2024_02.csv"]

df= pd.concat([pd.read_cvs(arquivo) for arquivo in arquivos], ignore_index=True)
df'''

df20_1= pd.read_csv('2020_01.csv', sep= ';')
df20_2= pd.read_csv('2020_02.csv', sep= ';')
df21_1= pd.read_csv('2021_01.csv', sep= ';')
df21_2= pd.read_csv('2021_02.csv', sep= ';', encoding="latin1") 
df22_1= pd.read_csv('2022_01.csv', sep= ';')
df22_2= pd.read_csv('2022_02.csv', sep= ';')
df23_1= pd.read_csv('2023_01.csv', sep= ';')
df23_2= pd.read_csv('2023_02.csv', sep= ';')
df24_1= pd.read_csv('2022_01.csv', sep= ';')
df24_2= pd.read_csv('2024_02.csv', sep= ';')

df_comp= pd.concat([df20_1,df20_2,df21_1,df21_2,df22_1,df22_2,df23_1,df23_2,df24_1,df24_2], ignore_index=True)

df_comp['Valor de Venda']= df_comp['Valor de Venda'].str.replace(',','.').astype(float)
print(df_comp['Valor de Venda'].dtype)


# Evolução mensal do preço medio da gasolina por estado (feito)_______________________________

df_comp['Data da Coleta'] = pd.to_datetime(df_comp['Data da Coleta'], format = "%d/%m/%Y")
df_comp['Mês']= df_comp['Data da Coleta'].dt.month

df_evol= df_comp.groupby(['Mês','Estado - Sigla'])['Valor de Venda'].mean().reset_index()
df_evol= df_evol.sort_values(by='Mês', ascending = True)
#_____________________________________________________________________________________________

#Comparação de preços entre gas aditivada e gas comum (feito) _________________________________
dfgas_com= df_comp.loc[(df_comp['Produto']== 'GASOLINA')]
dfgas_adt= df_comp.loc[(df_comp['Produto']== 'GASOLINA ADITIVADA')]

dfgas_com_media= dfgas_com.groupby('Produto')['Valor de Venda'].mean().reset_index()
dfgas_adt_media= dfgas_adt.groupby('Produto')['Valor de Venda'].mean().reset_index()

df_comp_gas= pd.concat([dfgas_com_media, dfgas_adt_media])
#_______________________________________________________________________________________________

#Análise de variação de preços por regiao

df_n= df_comp.loc[(df_comp['Regiao - Sigla']== 'N')]
df_ne= df_comp.loc[(df_comp['Regiao - Sigla']== 'NE')]
df_co= df_comp.loc[(df_comp['Regiao - Sigla']== 'CO')]
df_se= df_comp.loc[(df_comp['Regiao - Sigla']== 'SE')]
df_s= df_comp.loc[(df_comp['Regiao - Sigla']== 'S')]

df_media_n = df_n.groupby(['Regiao - Sigla','Produto'])['Valor de Venda'].mean().reset_index()
df_media_ne = df_ne.groupby(['Regiao - Sigla','Produto'])['Valor de Venda'].mean().reset_index()
df_media_co = df_co.groupby(['Regiao - Sigla','Produto'])['Valor de Venda'].mean().reset_index()
df_media_se = df_se.groupby(['Regiao - Sigla','Produto'])['Valor de Venda'].mean().reset_index()
df_media_s = df_s.groupby(['Regiao - Sigla','Produto'])['Valor de Venda'].mean().reset_index()

df_comp_reg= pd.concat([df_media_s, df_media_se, df_media_ne, df_media_co, df_media_n])
#_________________________________________________________________________________________________

# Postos com maiores e menores preços por tipo de combustivel (feito)
df_etanol= df_comp.loc[(df_comp['Produto']== 'ETANOL')]
df_diesel= df_comp.loc[(df_comp['Produto']== 'DIESEL')]
df_diesels10= df_comp.loc[(df_comp['Produto']== 'DIESEL S10')]
df_gnv= df_comp.loc[(df_comp['Produto']== 'GNV')]

# groupby etanol
df_media_et= df_etanol.groupby(['Bandeira','Produto'])['Valor de Venda'].mean().reset_index()
df_media_et= df_media_et.sort_values(by= 'Valor de Venda', ascending= True) #repetir essa estrutura para gasolina e diesel 

# groupby gasolina comum
df_media_gas= dfgas_com.groupby(['Bandeira','Produto'])['Valor de Venda'].mean().reset_index()
df_media_gas= df_media_gas.sort_values(by= 'Valor de Venda', ascending= True)

# groupby gasolina diesel
df_media_die= df_diesel.groupby(['Bandeira','Produto'])['Valor de Venda'].mean().reset_index()
df_media_die= df_media_die.sort_values(by= 'Valor de Venda', ascending= True)

# groupby gasolina aditivada
df_media_gas_adt= dfgas_adt.groupby(['Bandeira','Produto'])['Valor de Venda'].mean().reset_index()
df_media_gas_adt= df_media_gas_adt.sort_values(by= 'Valor de Venda', ascending= True)

# groupby gnv
df_media_gnv= df_gnv.groupby(['Bandeira','Produto'])['Valor de Venda'].mean().reset_index()
df_media_gnv= df_media_gnv.sort_values(by= 'Valor de Venda', ascending= True)

# groupby gasolina diesel s10
df_media_dies10= df_diesels10.groupby(['Bandeira','Produto'])['Valor de Venda'].mean().reset_index()
df_media_dies10= df_media_dies10.sort_values(by= 'Valor de Venda', ascending= True)

df_comp_pc= pd.concat([df_media_et, df_media_gas,df_media_die, df_media_gas_adt, df_media_gnv, df_media_dies10])
#___________________________________________________________________________________________________________________________

# Estado que teve maior variação de preço por gasolina entre 2020 e 2024

dfgas_com= df_comp.loc[(df_comp['Produto']== 'GASOLINA')]
dfgas_com_media= dfgas_com.groupby(['Produto', 'Regiao - Sigla'])['Valor de Venda'].mean().reset_index()









# area de exibição

print("Comparação de preços entre gasolina comum e aditvada")
df_comp_gas

print("Postos com maiores e menores preços por tipo de combustível")
df_comp_pc # seria melhor se printasse um por um e colocar head e o tail, posteriormente unir os dois em outra dataframe.

print("Evolução mensal do preço medio da gasolina por estado")
df_evol

print("Análise de variação de preços por região")
df_comp_reg




