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
st.write("Using Deep Learning models from SciKit Learn and tensorflow and using Revenue, EPS and PE multiples as our features, we determine whether our features can be correlated with our renewable stocks future performance. We also provide a dashboard of historical cumulative returns and P/E multiples to help retail investors compare the performance of our portfolio stocks to the NASDAQ, S&P500 and Fossil Fuel corporations." 
"Finally, we display the results of our NLP sentiment analysis to help retail investors more informed investing decisions than those available on social meddia.")
 

# First image
image1 = Image.open('./Visualizations/farm.jpg')
st.image(image1) 

# Set up sidebar
st.sidebar.header('Choose stock/Index')
stocks = st.sidebar.selectbox('Stocks', ['AQN', 'CSIQ', 'CVX','DQ', 'FSLR', 'SEDG','XOM','SP500','NASDAQ'])
image2 = Image.open('C:/Users/Owner/Class_Notes/03_Projects/Project_3/G12_Project_3/Visualizations/ui_logo.jpg')
st.sidebar.image(image2)        
st.sidebar.write('Group 12: Amany El Gouhary, Katharine Zenta, '
                 'Nicolas Hernandez, Al Bakomito')

