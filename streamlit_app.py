import streamlit
import pandas

streamlit.title('My Mom`s New Healthy Diner')

streamlit.header('🎉Breakfast Menu🎉')

streamlit.text('Omega 3 & Blueberry Oatmeal')

streamlit.text('🥬Kale, Spinach & Rocket Smotthie')

streamlit.text('🥚Hard-Boiled Free-Range Egg')

streamlit.text('🥑Avacado Toast')


streamlit.header('🍌🍍Build Your Own Smoothie🥕🍒🍏🍉')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# let's put a pick list here so they can pick the fruit they want to include
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

#new section to display fruityvice api response

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
