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
Our project's purpose is to build on our previous work and use Classification and Sentiment Analysis to demonstrate that our renewable energy portfolio is a good investment for environmentally conscious and socially responsible investors. This project utilized a neural network via Classification to anaylze the projection of the green portofolio prices and if they would provide a positive outcome. As a comparison we use NLP sentiment analysis to further illustrate these renewable energy stocks are a great investment. Once we have gathered our data we will create a user friendly interactive dashboard where investors can view our findings. Our hope is that with the knowledge provided the investors will make a more informed decision to enthusatically invest in these companies which will provide positive reutrns. 

The following provides a brief description of how we gathered the data and developed our code, followed by our findings after analysing the data. Finally, we use Streamlit (https://albakomito-g12-project-3-streamlitapp-3zw1yp.streamlitapp.com/) as a frontend development tool to display our result in a user friendly UI.

### Data Exploration, Machine Learning, NLP & Conclusions
When preforming our classification analysis we found that our results were not always accurate or conclusive. When gathering the data we included closing prices, eps and revenue in our analysis. After running an initial analysis the accuracy was not providing results that we had hoped. The accuracy was 53% which was disappointing. But a future step or outlook on this analysis could be to further explore different models or analyze different time frames to perhaps generate different results. 

The next step we did was create a sentiment analysis using Google News API and see what the results would be in hopes of positive outcomes. However, unfortunately our results were again inconclusive as some months were positive and others were more so on the negative side. Another issue we ran into was not having enough data or news on some of the stocks we chose to create a more comprehensive sentiment analysis on our portfolio. 

While we are very passionate about this idea and green investing. We were disappointed to conclude our analysis was not sufficient to provide enough information to the investors to make an informed decision based on what is in the interactive dashboard.

We would have to pursue this idea in more depth and require more time to try new analysis and approaches to gather better data and results. That being said green investments are certainly a great idea to explore further in the future. 
