I would like to explore the stock anomaly (Jan 25 – Feb 2) of GameStop as well as AMC. In Stock Trading there is a concept that the momentum of one stock can spur that of another. GameStop and AMC were seemingly intertwined with the reddit and Elon Musk twitter saga of popularity and “meme” culture. I originally wanted to explore the relation of GME with twitter tracking but was unable to get a developer’s account to use twitter. For my new proposal, I will be relating GME and AMC stock information. My questions are as follows:

1.	How did GameStop share price change over time?
2.	How did AMC share price change over time?
3.	How does the share price of Game Stop relate to the price of AMC during Jan 25 to Feb 2?

The two data sets I will need are the periodic stock prices of GME and AMC from Jan 25 to Feb 2. Because the time frame is so small, I will be looking at hourly data rather than daily. Due to this, I will retrieve the first one from YahooFinance using Python because there is not functionality to retrieve and download such data via Yahoo Finance website, I will then export these data to CSV files to read into R. 

There will be a minimum of three variables of interest: stock price, volume, and time. Time might be put into subsections by date and hour since open on January 2. I might consider doing a continuous variable of time since midnight at Jan 25.

I will have some basic visualizations to understand the individual trends:
1.	Interactive Line graph of Share Price over Time for each stock and volume coloring
2.	Column plot of daily average share prices for both stocks
3.	Scatter Plot of GME share price vs. AMC share price w/ regression line overlay

