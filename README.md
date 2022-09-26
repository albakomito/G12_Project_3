# Renewable Energy Investing 

<img src="https://github.com/albakomito/Renewable-Energy-Investing/blob/main/Visualizations/windfarm.jpg" width="600" height="400">



## Renewable Energy: A good time to invest? 

### Source Files
* Visualizations: Images we used to run streamlitapp.py
* Downloads/CSV_1: CSV's used in fundamental_charts.ipynb
* Downloads/CSV_2: CSV's used in machine_learning.ipynb and stock_sentiment.ipynb

### Output Notebooks: 
* fundamental_charts.ipynb: Key performance indicators (ratios) used for our deployed investor dashboard. 
* machine_learning.ipynb: Machine learning code. 
* stock_sentiment.ipynb: sentiment analysis code. 
* streamlit deployment: https://albakomito-g12-project-3-streamlitapp-3zw1yp.streamlitapp.com/
* Note: Code instructions are all contained within each notebook. 


### Summary(Introduction) 
Our project's purpose is to build on our previous work and use Classification and Sentiment Analysis to demonstrate that our renewable energy portfolio is a good investment for environmentally conscious and socially responsible investors. This project utilizeS a neural network via Classification to anaylze the projection of the green portofolio prices and if they would provide a positive outcome. As a comparison, we use NLP sentiment analysis to further illustrate these renewable energy stocks are a great investment. Once we have gathered our data, we will create a user-friendly interactive dashboard where investors can view our findings. Our hope is that with the knowledge provided, investors will make a more informed decision to invest in these companies, and hopefully achieve market-beating returns. 

Below, we  briefly describe how we gathered the data,  developed our code, and key findings after analysing the data. Finally, we use Streamlit (https://albakomito-g12-project-3-streamlitapp-3zw1yp.streamlitapp.com/) as a frontend development tool to display our results in a user friendly UI.

### Data Exploration, Machine Learning, NLP & Conclusions
When preforming our classification analysis, we found that our results were not always accurate or conclusive. When gathering the data we included closing prices, earnings per share (eps) and revenue in our analysis. Our initial analysis (without closing prices, eps and revenue) yielded a very low accuracy score of 33%.

<img src="https://github.com/albakomito/Renewable-Energy-Investing/blob/main/Visualizations/confusion2.jpg" width="300" height="200">

Upon adding eps, revenue and closing prices to our analysis, our classification model yielded an accuracy score of 59%, which (while higher than our model without the features) was not conclusive. However,  a future step in this analysis could be to  explore different models or analyze different time frames to hopefully generate superior accuracy scores. 

Our next step was to create a sentiment analysis using Google News API and observe results in hopes of positive outcomes. However,  our results were again inconclusive as some months were positive and others were more so on the negative side. Another issue we ran into was not having enough data or news on some of the stocks we chose to create a more comprehensive sentiment analysis on our portfolio. 

While we are very passionate about this idea and green investing. We were disappointed to conclude our analysis was not sufficient to provide enough information to the investors to make an informed decision based on what is in the interactive dashboard.

We would have to pursue this idea in more depth and require more time to try new analysis and approaches to gather better data and results. That being said green investments are certainly a great idea to explore further in the future. 
