# Import libraries and their dependencies 
import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
from pathlib import Path
from PIL import Image

import os
import requests

# Create Header
st.write('''# Renewable Enegergy Portfolio: Is now a good time to buy?''')
st.write('''## Introduction''')
st.write("Using Deep Learning models from SciKit Learn and Tensorflow and using Revenue and EPS as our features, we determine whether our features can be correlated with our renewable stocks future performance. We also provide a dashboard of historical cumulative returns and P/E multiples to help retail investors compare the performance of our portfolio stocks to the NASDAQ, S&P500 and Fossil Fuel corporations." 
"Finally, we display the results of our NLP sentiment analysis to help retail investors more informed investing decisions than those available on social meddia.")
 

# First image
image1 = Image.open('./Visualizations/farm.jpg')
st.image(image1) 

# Set up sidebar
st.sidebar.header('Choose stock/Index')
stocks = st.sidebar.selectbox('Stocks', ['AQN', 'CSIQ', 'CVX','DQ', 'FSLR', 'SEDG','XOM','SP500','NASDAQ'])
image2 = Image.open('./Visualizations/ui_logo.jpg')
st.sidebar.image(image2)        
st.sidebar.write('Group 12: Amany El Gouhary, Katharine Zenta, '
                 'Nicolas Hernandez, Al Bakomito')

# Project 2 Recap 
## Machine Learning Outputs 
st.write('''## Project 2 Recap: Machine Learning Outputs''')
st.write('''#### LSTM One-level Sequential Model, 10 Day Window''')
st.write('Portfolio & SPY Closing Price: US$100k Initial Investment')
image3= Image.open('./Visualizations/ML1.jpg')
st.image(image3)



st.write('Validation & Prediction Period')
image4= Image.open('./Visualizations/ML2.jpg')
st.image(image4)



st.write('Validation & Prediction Period: Zoomed in')
image5= Image.open('./Visualizations/ML3.jpg')
st.image(image5)



# Project 3: Prediction & Classification 
st.write('''## Project 3: Prediction & Classification''')
st.write('''#### Actual vs. Predicted''')
image6= Image.open('./Visualizations/prediction.jpg')
st.image(image6)



st.write('''#### Classification Report''')
image7= Image.open('./Visualizations/confusion.jpg')
st.image(image7)


# Sentiment Analysis  
st.write('''#### Sentiment Analysis: First Solar''')
image8= Image.open('./Visualizations/sentiment.jpg')
st.image(image8)



# Strong Returns & Fundamentals vs. Fossil fuels and Indices 
st.write('''#### Think Green Portfolio Cumulative Profit: $29644''')
image9= Image.open('./Visualizations/cumprof.jpg')
st.image(image9)



st.write('''#### S&P500 Cumulative Profit:$15300''')
image10= Image.open('./Visualizations/SP500.jpg')
st.image(image10)



st.write('''#### Think Green vs. Fossil Fuels vs. Indices Cumulative Profit: A clear outperformer''')
image11= Image.open('./Visualizations/allcumprof.jpg')
st.image(image11)



st.write('''#### Elevated PEs will likely unwind''')
image12= Image.open('./Visualizations/pe.jpg')
st.image(image12)