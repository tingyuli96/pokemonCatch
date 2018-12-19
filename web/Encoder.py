import pandas as pd


def IDtoName(dataset):
    """
    Input: one dataframe column
    Return: onde dataframe column
    function: convert the ID to Name for pokemon
    example: test['a'] = IDtoName(test['a'])
    """
    Names = pd.read_csv("../Data/pokemonNumbers.csv",header=None)
    Names.columns = ['pokemonid', 'name']
    #Names.head()
    dictionary = dict(zip(Names['pokemonid'], Names['name']))
    dataset = dataset.apply(lambda x: dictionary[x])
    return dataset

# #TestCase
# test = pd.DataFrame({'a':[1,2,3,45,67]})
# test['a'] = IDtoName(test['a'])
# print(test.head)
