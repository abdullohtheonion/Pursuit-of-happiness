import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Pursuit of happiness")
option_x = st.selectbox("Select the data for X-axis",
             ["GDP", "Happiness", "Generosity"])
option_y = st.selectbox("Select the data for Y-axis",
             ["GDP", "Happiness", "Generosity"])
st.subheader(f"{option_x} and {option_y}")

file = pd.read_csv("happy.csv")
x = file[option_x.lower()]
y = file[option_y.lower()]

figure = px.scatter(x=x, y=y, labels={'x': option_x, 'y':option_y})
st.plotly_chart(figure)