import pandas as pd
import numpy as np

#Load Name
Names = pd.read_csv("../../Data/pokemonNumbers.csv",header=None)
Names.columns = ['pokemonid', 'name']
Names['pokemonid'] = Names['pokemonid'].apply(lambda x: x-1)
Names.head()
dictionary = dict(zip(Names['pokemonid'], Names['name']))
#print(dictionary)

#Load City
train = pd.read_csv('../../Data/300k.csv', low_memory=False)
city = train[['pokemonId', 'city']]
print(city)

#Cacualte Frequency
poke_city = city.groupby(['city','pokemonId']).size()
poke_city = poke_city.unstack()
poke_city.fillna(0, inplace=True)
#print(poke_city)

x = poke_city.index
y = poke_city.iloc[:, 24]

data = pd.DataFrame({'x':x,'y':y})
print(data)
data.to_csv('pikachu_city.csv', header=True, index= False)