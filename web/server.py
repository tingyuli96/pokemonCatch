from flask import Flask, request, render_template, g, redirect, Response,session,flash
import os
from sklearn.externals import joblib
import pandas as pd
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, Form
from wtforms import StringField, TextAreaField, PasswordField, SelectField, BooleanField, IntegerField
from wtforms.validators import InputRequired,  DataRequired, Length, NumberRange

app = Flask(__name__)
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
Bootstrap(app)

# class FormPredictPokemon(FlaskForm):
#     """docstring for FormPredictPokemon"""
#     latitude = FloatField('latitude',validators = [InputRequired()])
#     longitude = FloatField('longitude', validators = [InputRequired()])
#     terrainType = convert_tp(request.form['terrainType'])
#     closeToWater = convert_water(request.form['closeToWater'])
#     temperature = request.form['temperature']
#     windSpeed = request.form['windSpeed']
#     pressure = request.form['pressure']
#     population_density = convert_pd(float(request.form['population_density']))
#     pclass = request.form['class']
#     weather = request.form['weather']

def terrainTypechoise():
    d = {'Water':0,'Evergreen Needleleaf forest':1,'Evergreen Broadleaf forest':2,'Deciduous Needleleaf forest':3,
        'Deciduous Broadleaf forest':4,'Mixed forest':5,'Closed shrublands':6,'Open shrublands':7,'Woody savannas':8,
        'Savannas':9,'Grasslands':10,'Permanent wetlands':11,'Croplands':12,'Urban and built-up':13,
         'Cropland/Natural vegetation mosaic':14,'Snow and ice':15,'Barren or sparsely vegetated':16,'Unclassified':254,
        'Fill Value':255}
    d_list = []
    for i in d:
        d_list.append((d[i],i))
    return d[a]

def convert_pd(a):
    if a < 200:
        b = 0
    if 200< a< 400:
        b = 1
    if 400< a < 800:
        b = 2
    if  a > 800:
        b = 3
    return b

def convert_tp(a):
    d = {'Water':0,'Evergreen Needleleaf forest':1,'Evergreen Broadleaf forest':2,'Deciduous Needleleaf forest':3,
        'Deciduous Broadleaf forest':4,'Mixed forest':5,'Closed shrublands':6,'Open shrublands':7,'Woody savannas':8,
        'Savannas':9,'Grasslands':10,'Permanent wetlands':11,'Croplands':12,'Urban and built-up':13,
         'Cropland/Natural vegetation mosaic':14,'Snow and ice':15,'Barren or sparsely vegetated':16,'Unclassified':254,
        'Fill Value':255}
    return d[a]

def convert_water(a):
    d = {'True':0,'False':1}
    return d[a]
def convert_pr(a):
    if a < 1000:
        b = 0
    if 1000 <= a < 1005:
        b = 1
    if 1005 <= a < 1010:
        b = 2
    if 1010 <= a < 1015:
        b = 3
    if 1015 <= a <1020:
        b = 4
    if 1020 <= a < 1025:
        b = 5
    if 1025 <= a < 1030:
        b = 6
    if a >= 1030:
        b = 7
    return b

def convert_wb(a):
    if a >400:
        b = 0
    if a < 24:
        b = 0
    if 24 <= a < 70:
        b = 1
    if 70 <= a < 120:
        b = 2
    if 120 <= a < 170:
        b = 3
    if 170 <= a <220:
        b = 4
    if 220 <= a <270:
        b = 5
    if 270 <= a < 320:
        b = 6
    if 320 <= a < 400:
        b = 7
    return(b)

def convert_we(a):
    weather = {'Foggy': 1, 'Clear': 2, 'PartlyCloudy': 3, 'MostlyCloudy': 4,"Overcast" : 5,"Rain" : 6,"BreezyandOvercast" : 7,"LightRain" : 8, "Drizzle" : 9,"BreezyandPartlyCloudy" : 10,"HeavyRain" : 11,"BreezyandMostlyCloudy" :12,
          "Breezy" : 13, "Windy": 14, "WindyandFoggy" : 15, "Humid" : 16, "Dry" : 17, "WindyandPartlyCloudy" : 18, "DangerouslyWindy":19, "DryandMostlyCloudy": 20, "DryandPartlyCloudy" : 21, "DrizzleandBreezy":22,"LightRainandBreezy" :23,
               "HumidandPartlyCloudy" :24, "HumidandOvercast" : 25,"RainandWindy" : 26}
    return weather[a]
def convert_pd_location(a):
    if a < 200:
        b = 0
    if 200 <= a < 800:
        b = 1
    if 800 <= a < 1400:
        b = 2
    if a >= 1400:
        b = 3
    return(b)
def convert_tm(a):
    if a <10:
        b = 0
    if 10 <= a < 20:
        b = 1
    if 20 <= a < 30:
        b = 2
    if 30 <= a < 40:
        b = 3
    if a >= 40:
        b = 4
    return b

def convert_ws(a):
    if a < 1:
        b = 0
    if 1 <= a < 5:
        b = 1
    if 5 <= a < 10:
        b = 2
    if 10 <= a < 15:
        b = 3
    if 15 <= a < 20:
        b = 4
    if 20 <= a < 25:
        b = 5
    if 25 <= a < 30:
        b = 6
    if 30 <= a < 35:
        b = 7
    if a >= 35:
        b = 8
    return b
def IDtoName(namefilepath, dataset):
    Names = pd.read_csv(namefilepath,header=None)
    Names.columns = ['pokemonid', 'name']
    #Names.head()
    dictionary = dict(zip(Names['pokemonid'], Names['name']))
    dataset = dataset.apply(lambda x: dictionary[x])
    return dataset

@app.route("/")
def hello():
    # context = dict(data=hello)
    return render_template("index.html")

@app.route("/search_id",methods=['POST'])
def predict_id():
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    terrainType = convert_tp(request.form['terrainType'])
    closeToWater = convert_water(request.form['closeToWater'])
    temperature = request.form['temperature']
    windSpeed = request.form['windSpeed']
    pressure = request.form['pressure']
    population_density = convert_pd(float(request.form['population_density']))
    pclass = request.form['class']
    weather = request.form['weather']
    from collections import OrderedDict
    head_list = ['latitude','longitude','terrainType','closeToWater','temperature','windSpeed','pressure','population_density','class','weather']
    d = {'latitude':latitude,'longitude':longitude,'terrainType':terrainType,'closeToWater':closeToWater,'temperature':temperature,
                      'windSpeed':windSpeed,'pressure':pressure,'population_density':population_density,'class':pclass,'weather':weather}
    row = d
    d2 = OrderedDict()
    for key in head_list:
        if row.get(key) is not None:
            d2[key] = row.get(key)
    feature = pd.DataFrame([d2])
    print(feature.head())
    weather_head = ['weather_BreezyandMostlyCloudy','weather_BreezyandOvercast','weather_BreezyandPartlyCloudy','weather_Clear',
                    'weather_DangerouslyWindy','weather_Drizzle','weather_DrizzleandBreezy','weather_Dry','weather_DryandMostlyCloudy',
                    'weather_DryandPartlyCloudy','weather_Foggy','weather_HeavyRain','weather_Humid','weather_HumidandOvercast','weather_HumidandPartlyCloudy'
                    ,'weather_LightRain','weather_LightRainandBreezy','weather_MostlyCloudy','weather_Overcast','weather_PartlyCloudy'
                    ,'weather_Rain','weather_RainandWindy','weather_Windy','weather_WindyandFoggy','weather_WindyandPartlyCloudy']
    d3 = {'weather_BreezyandMostlyCloudy':0,'weather_BreezyandOvercast':0,'weather_BreezyandPartlyCloudy':0,'weather_Clear':0,
                    'weather_DangerouslyWindy':0,'weather_Drizzle':0,'weather_DrizzleandBreezy':0,'weather_Dry':0,'weather_DryandMostlyCloudy':0,
                    'weather_DryandPartlyCloudy':0,'weather_Foggy':0,'weather_HeavyRain':0,'weather_Humid':0,'weather_HumidandOvercast':0,
                    'weather_HumidandPartlyCloudy':0
                    ,'weather_LightRain':0,'weather_LightRainandBreezy':0,'weather_MostlyCloudy':0,'weather_Overcast':0,'weather_PartlyCloudy':0
                    ,'weather_Rain':0,'weather_RainandWindy':0,'weather_Windy':0,'weather_WindyandFoggy':0,'weather_WindyandPartlyCloudy':0}
    row2 = d3
    d4 = OrderedDict()
    for key in weather_head:
        if row2.get(key) is not None:
            d4[key] = row2.get(key)
    Weather = pd.DataFrame([d4])
    Weather['weather_'+weather] = 1
    feature = feature.join(Weather)
    feature = feature.drop(['weather'],1)
    print(feature.shape)
    model = joblib.load('static/model.pkl')
    prediction = model.predict(feature)
    pid = pd.DataFrame({'a':prediction})
    pred = pd.DataFrame(IDtoName('static/pokemonNumbers.csv',pid['a']))
    context = dict(data=pred.iloc[0]['a'])
    return render_template("index.html", **context)

@app.route("/search_location",methods=['POST'])
def search_location():
    pclass = request.form['class']
    hour = request.form['appearedHour']
    minute = request.form['appearedMinute']
    day = request.form['appearedTimeOfDay']
    terrainType = convert_tp(request.form['terrainType'])
    pressure = convert_pr(float(request.form['pressure']))
    windBearing = convert_wb(float(request.form['windBearing']))
    weather = convert_we(request.form['weather'])
    population_density = convert_pd_location(float(request.form['population_density']))
    temperature = convert_tm(float(request.form['temperature']))
    windSpeed = convert_ws(float(request.form['windSpeed']))
    closeToWater = convert_water(request.form['closeToWater'])
    from collections import OrderedDict
    feature_list = ['class','appearedHour','appearedMinute','appearedTimeOfDay','terrainType','pressure',
                    'windBearing','weather','population_density','temperature','windSpeed','closeToWater']
    d = {'class':pclass,'appearedHour':hour,'appearedMinute':minute,'appearedTimeOfDay':day,'terrainType':terrainType,
        'pressure':pressure,'windBearing':windBearing,'weather':weather,'population_density':population_density,
        'temperature':temperature,'windSpeed':windSpeed,'closeToWater':closeToWater}
    row = d
    d2 = OrderedDict()
    for key in feature_list:
        if row.get(key) is not None:
            d2[key] = row.get(key)
    feature = pd.DataFrame([d2])
    print(feature.head())
    model_latitude = joblib.load('static/model_latitude.pkl')
    model_longitude = joblib.load('static/model_longitude.pkl')
    pred_latitude = model_latitude.predict(feature)
    pred_longitude = model_longitude.predict(feature)
    result = [pred_latitude[0],pred_longitude[0]]
    print(result)
    context = dict(data1=result)
    return render_template("index.html", **context)


if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using
        python server.py
    Show the help text using
        python server.py --help
    """

    HOST, PORT = host, port
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)


  run()
