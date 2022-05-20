import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

import numpy as np
import streamlit as st
import pickle


data = load_wine()

wine = pd.DataFrame(data.data, columns=data.feature_names)

scatter_plot = sns.scatterplot(x=wine['alcohol'], y = wine['color_intensity']);

st.title("Simple Linear Regression on Wine Data set")
st.text("What is a strong predictor for alcohol content in your fav wine?")


page = st.sidebar.selectbox('Select a page', ('About', 'The Model'))

if page == 'About':
    st.write("We used the wine data set to see what featues contribute to a wine's alcohol content")

if page == 'The Model':
    st.write("Below you'll find a plot of our alcohol content for predicted and actual values")

    st.dataframe(wine)
    fig = plt.figure(figsize=(10, 4))
    st.bar_chart(wine['alcohol'][:10])
    
