import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

#st.markdown('''
#Remember that there are several ways to output content into your web page...
#Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
#''')
#'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride
#'''


# - date and time
d = st.date_input(
    "Seleccione la fecha",
    datetime.date(2001, 4, 23))
t = st.time_input('Seleccione la hora', datetime.time(8, 00))
pickup_datetime = (f'{d} {t}UTC')
key = pickup_datetime

# - pickuplongitude
pickup_longitude = st.text_input('pickup longitude', '40.7614327')
#- pickup latitude
pickup_latitude = st.text_input('pickup latitude', '73.9798156')
#- dropoff longitude
dropoff_longitude  = st.text_input('Dropoff Longitude', '40.6513111')
#- dropoff latitude
dropoff_latitude = st.text_input('Dropoff Latitudes', '73.8803331')
#- passenger count
passenger_count = st.slider('Cantidad de pasajeros', 1, 8, 2)

#'''
### Once we have these, let's call our API in order to retrieve a prediction
#See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...
#🤔 How could we call our API ? Off course... The `requests` package 💡
#'''

# Se presiona el boton para llamar al api
if st.button('Predecir el precio'):

    params = {
        'key':key,
        'pickup_datetime':pickup_datetime,
        'pickup_longitude':pickup_longitude,
        'pickup_latitude':pickup_latitude,
        'dropoff_longitude':dropoff_longitude,
        'dropoff_latitude':dropoff_latitude,
        'passenger_count':passenger_count
        }

    params

    url = 'https://taxifare.lewagon.ai/predict_fare/'

    response = requests.get(
        url, params=params
    ).json()    

    response

    # print is visible in server output, not in the page
