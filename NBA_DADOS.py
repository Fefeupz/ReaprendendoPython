import pandas as pd 

file = 'Players.csv'

nba = pd.read_csv(file)
#print(nba.columns)
#print(nba['height'])
#print(nba['weight'])

#encontrando o IMC de peso/altura e acionando na planilha
#IMC = nba['weight'] / ((nba['height']/100)**2)
#nba['IMC'] = (IMC)

#print da média total de IMC
#print(nba['IMC'].mean())

#Altura mínima e máxima
#print(nba['height'].min())
#print(nba['height'].max())

#Peso mínimo e máximo
#print(nba['weight'].min())
#print(nba['weight'].max())

#Estado com maior número de jogadores
#print(nba['birth_state'].value_counts())

#Qual o jogador mais alto
#print(nba.sort_values(by='height').tail(2))