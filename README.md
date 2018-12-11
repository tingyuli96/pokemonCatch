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
