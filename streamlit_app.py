import streamlit as st
import pandas as pd
import requests
from urllib.error import URLError
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

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get('https://www.fruityvice.com/api/fruit/' + fruit_choice)
    fruityvice_json = pd.json_normalize(fruityvice_response.json())
    return fruityvice_json


st.header('Fruityvice Fruit Advice !')
try: 
    fruit_choice = st.text_input('What fruit do you want advice on?')
    if not fruit_choice: 
        st.error("Please select a fruit to get information.")
    else:
        fruityvice_json = get_fruityvice_data(fruit_choice)
        st.dataframe(fruityvice_json)
except URLError as e:
    st.error()

# Call Snowflake


st.header("The fruit load list contains:")
st.dataframe(my_data_rows)
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        my_data_rows = my_cur.fetchall()
        return my_data_rows
    
# Add a button to load the fruit
if st.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    st.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
        return "Thanks for adding" + new_fruit

add_my_fruit = st.text_input('What fruit would you like to add ?')
if st.button('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    back_from_snowflake = insert_row_snowflake(add_my_fruit)
    st.text(back_from_snowflake)


