import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


df = pd.read_csv('gapminder.csv')
clist = df['country'].unique()
country = st.sidebar.selectbox("Select a country:",clist)
st.header("GDP per Capita over time")
fig = px.line(df[df['country'] == country], 
    x = "year", y = "GNI per cap", title = country)
st.plotly_chart(fig)