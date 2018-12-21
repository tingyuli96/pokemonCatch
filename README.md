## Let's Catch Pokemon
PokemonGo is a mobile AR game, where players can catch virtual creatures Pokemon useGPS and camera on their phone. In this project, we predict where pokemon may appear and what king of pokemon will appear based on historical data in PokemonGo.
## Getting Started
### Dataset
https://www.kaggle.com/semioniy/predictemall/home

This dataset consists of roughly 293,000 pokemon sightings (historical appearances of Pokemon), having coordinates, time, weather, population density, distance to pokestops/ gyms etc. as features.
### Directory Hierarchy

````
pokemonCatch
|--Data    
|	|--pokemonNumbers.csv            
|	|--smalldata.csv   
|--DataVisual   
|	|--OriginDataVisual.ipynb     # original data visualization   
|	|--PredictDataVisual.ipynb    # predict data visualiztion  
|--FeatureExtraction  
|	|--CorrelationAnalysis.ipynb  # Analysis correlation between features  
|	|--feature_abstract.ipynb     #  
|	|--FeatureSelection.ipynb     #   
|	|--OutputasCity.ipynb   
|	|--/PredictPokemonid.ipynb     # predict pokemon id based on historical data  
|--Pic
|--Predict  
|	|--predict_id.ipynb
|	|--predic_location.ipynb  
|	|--SimilarPokemonPredict.ipynb  
+--Result  
````


### Prerequisites
python3.7
jupyter notebook
pyspark

numpy
pandas
basemap
seaborn
matplotlib

## System Description

![system](https://github.com/colirain/pokemonCatch/blob/master/Pic/system.png)

This shows a whole picture of our project.

### Original Data Visualization

#### The activity of Pokemon in different regions

![pokemon](https://github.com/colirain/pokemonCatch/blob/master/Pic/Pokemon%20activity%20origin.png)

#### The distibution of Pokemon in different cities

Omanyte

![Omanyte](https://github.com/colirain/pokemonCatch/blob/master/Pic/pokemon%20Omanyte%20in%20city.png)

Pidgeotto

![Pidgeotto](https://github.com/colirain/pokemonCatch/blob/master/Pic/pokemon%20Pidgeotto%20in%20city.png)

Pikache

![Pikache](https://github.com/colirain/pokemonCatch/blob/master/Pic/pokemon%20Pikachu%20in%20city.png)

#### The distribution of pokemon at different time in a day in different cities

![](https://github.com/colirain/pokemonCatch/blob/master/Pic/pokemon%20in%20city%20at%20time.png)

### Correlation Analyse

![](https://github.com/colirain/pokemonCatch/blob/master/Pic/Correclation.jpg)

Correlation analysis of all the feature in the data set. The darker the color is, the more correlated the two feature are.

### Prediction

#### Prediction of where Pokemon may appear

![](https://github.com/colirain/pokemonCatch/blob/master/Pic/Pokemon%20activity%20noclass.png)

The red spots represent the ground truth of test dataset, the blue spots represent the prediction results.

#### Prediction of what kind of Pokemon may appear in a given city

![](https://github.com/colirain/pokemonCatch/blob/master/Pic/id_predict.png)

The blue one is the ground truth, the red one is the prediction results.

### Similar Pokemon

![](https://github.com/colirain/pokemonCatch/blob/master/Pic/BehaviorSimilar.jpg)

The darker the color is, the more similar the two Pokemon are.

### Web application

Our web application is in the 'web' folder. You can see more details there. 



