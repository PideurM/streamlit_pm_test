import streamlit as st
import pandas as pd
import requests

import snowflake.connector 



st.header('Breakfast Menu')

st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')
st.text('🍌🍞 Banana Bread')
st.text('🍳🥓🍞 Full English Breakfast')
st.text('🥞🍓🍌 Pancakes with Berries & Banana')
st.text('🍳🥓🍞 Eggs & Bacon')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

df = pd.read_csv('fruit_macro.csv')
df = df.set_index('Fruit')

fruit_selected = st.multiselect('Select your fruit', list(df.index),['Avocado','Banana'])
fruit_to_show = df.loc[fruit_selected]

#Display the dataframe
st.dataframe(fruit_to_show)

# Call fruityvice API
st.header('Fruityvice Fruit Advice !')
fruit_choice = st.text_input('What fruit do you want advice on?','Kiwi')
st.write('You selected', fruit_choice)
fruityvice_response = requests.get('https://www.fruityvice.com/api/fruit/' + fruit_choice)
fruityvice_json = pd.json_normalize(fruityvice_response.json())
st.dataframe(fruityvice_json) # Display the dataframe


