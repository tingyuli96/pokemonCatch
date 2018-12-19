import pandas as pd
import numpy as np
import random
import sys
sys.path.append('../')
import Encoder

#Load Data
train = pd.read_csv('../../Data/300k.csv', low_memory=False)
train = train[['appearedLocalTime', 'pokemonId', 'city']]
train['appearedLocalTime'] = train.appearedLocalTime.apply(lambda x: x.split("T")[1])

#Save Data
data = pd.DataFrame({'time':train['appearedLocalTime'],'ID':train['pokemonId'],'city':train['city']})
a = random.sample(range(data.shape[0]), 1000)
data = data.sample(frac=0.0005)
#data = data[1:10]
namefilepath = "../../Data/pokemonNumbers.csv"
#data['ID'] = Encoder.IDtoName(namefilepath, data['ID'])
print(data.head)
data.to_csv('../static/time_city.csv', header=True, index= False)