# Stockso
A Python program that allows users to predict the stock market based on many data factors

## Introduction
Stockso is an open source alpha project developed by Elias Maalouf, a junior developer, the project is based on Python, a programming language that has proved to be a big player in the machine learning industry.

Stockso works on reading information from CSVs and connected APIs(Still work in progress), As a result, Stockso can now produce prediction results that allow stock brokers to know how the market is gonna go.

Caution: This project is still in (very) early alpha stage and lacks a lot of testing and work, I am working on adding more factors such as making the agent understand the political situation to come up with a better prediction, but all of this is still under heavy development, my advice is to use this software as a tool to help you come up with what you want to inverst in. I am not responsible for any investments you take using this software, trade at your own risk, PLEASE TRADE WISELY

## Getting Started
Stockso works in a Python environmnent, so it is best to use pip, for information on how to use pip please visit: https://docs.python.org/3/installing/index.html

## Overview


- The overall workflow to use machine learning to make stocks prediction is as follows:

1. Acquire historical fundamental data – these are the features or predictors
2. Acquire historical stock price data – this is will make up the dependent variable, or label (what we are trying to predict).
3. Preprocess data
4. Use a machine learning model to learn from the data
5. Backtest the performance of the machine learning model
6. Acquire current fundamental data
7. Generate predictions from current fundamental data


This is a very generalised overview, but in principle this is all you need to build a fundamentals-based ML stock predictor.

In addition to that, Please note that this project uses pandas-datareader(https://pandas-datareader.readthedocs.io/en/latest/) to download historical price data from Yahoo Finance(https://pypi.org/project/yahoo-finance/). However, in the past few weeks this has become extremely inconsistent – it seems like Yahoo have added some measures to prevent the bulk download of their data. I will try to add a fix, but for now, take note that download_historical_prices.py may be deprecated.




As a temporary solution, I've uploaded stock_prices.csv and sp500_index.csv in the main folder, so the rest of the project can still function.

## Quickstart for developers

If you want to throw away the instruction manual and play immediately, clone this project, then download and unzip the data file into the same directory. Then, open an instance of terminal and cd to the project's file path, e.g

  cd Users/User/Desktop/MachineLearningStocks


Then, run the following in terminal:

pip install -r requirements.txt

This should have installed all the requirments for the project to run, you can install each one manually if you face any problem(Most of the problems with pip are faced on Windows), for that reason, here is a list of the requirements that you might need for this project to run:

# Requests
-pip3.4 install requests

# TQDM
https://github.com/noamraph/tqdm

# Python Test
https://docs.pytest.org/en/latest/

# Fix Yahoo Python API Test
https://pypi.org/project/fix-yahoo-finance/

# Pandas Datareader
https://pandas-datareader.readthedocs.io/en/latest/

# Numpy
I would like to add a small comment on Numpy, NumPy is the fundamental package for scientific computing with Python, Here is a tutorial and the link to download numpy
http://www.numpy.org/
http://cs231n.github.io/python-numpy-tutorial/

# Pandas
https://pandas.pydata.org/

# Scikit_Learn 
https://pypi.org/project/scikit-learn/


# Installation

python download_historical_prices.py
python parsing_keystats.py
python backtesting.py
python current_data.py
pytest -v
python stock_prediction.py
You should get in CLI a menu that will help you predict the stocks that you want

## Note:
If the above is too hard, please wait for the next update as there will be more updates as we continue.


# Historical data
- For this project, we need three datasets:

- Historical stock fundamentals
- Historical stock prices
- Historical S&P500 prices
- We need the S&P500 index prices as a benchmark:
For example: a 5% stock growth does not mean much if the S&P500 grew 10% in that time period, so all stock returns must be compared to those of the index.

- Historical stock fundamentals
- Historical fundamental data is actually very difficult to find (for free, at least). Although sites like Quandl(https://www.quandl.com/tools/api) do have datasets available, you often have to pay a pretty steep fee.

- It turns out that there is a way to parse this data, for free, from Yahoo Finance. I will not go into details, because Sentdex has done it for us. On his page you will be able to find a file called intraQuarter.zip, which you should download, unzip, and place in your working directory. Relevant to this project is the subfolder called _KeyStats, which contains html files that hold stock fundamentals for all stocks in the S&P500 between 2003 and 2013, sorted by stock. However, at this stage, the data is unusable – we will have to parse it into a nice csv file before we can do any ML.(Since the system cannot read unclean data, a CSV is a must for it to work)

# Historical price data

In the first iteration of the project, I used pandas-datareader, an extremely convenient library which can load stock data straight into pandas. However, after Yahoo Finance changed their UI, datareader no longer worked, so I switched to Quandl, which has free stock price data for a few tickers, and a python API. However, as pandas-datareader has been fixed, we will use that instead.

The code for downloading historical price data can be run by entering the following into terminal:

# python download_historical_prices.py

-Creating the training dataset
Our ultimate goal for the training data is to have a 'snapshot' of a particular stock's fundamentals at a particular time, and the corresponding subsequent annual performance of the stock.

-For example, if our 'snapshot' consists of all of the fundamental data for AAPL on the date 28/1/2005, then we also need to know the percentage price change of AAPL between 28/1/05 and 28/1/06. Thus our algorithm can learn how the fundamentals impact the annual change in the stock price.

-In fact, this is a slight oversimplification. In fact, what the algorithm will eventually learn is how fundamentals impact the outperformance of a stock relative to the S&P500 index. This is why we also need index data.

# Preprocessing historical price data

When pandas-datareader downloads stock price data, it does not include rows for weekends and public holidays (when the market is closed).

-Features
Below is a list of some of the interesting variables that are available on Yahoo Finance.

Valuation measures
'Market Cap'
Enterprise Value
Trailing P/E
Forward P/E
PEG Ratio
Price/Sales
Price/Book
Enterprise Value/Revenue
Enterprise Value/EBITDA
Financials
Profit Margin
Operating Margin
Return on Assets
Return on Equity
Revenue
Revenue Per Share
Quarterly Revenue Growth
Gross Profit
EBITDA
Net Income Avi to Common
Diluted EPS
Quarterly Earnings Growth
Total Cash
Total Cash Per Share
Total Debt
Total Debt/Equity
Current Ratio
Book Value Per Share
Operating Cash Flow
Levered Free Cash Flow
Trading information
Beta
50-Day Moving Average
200-Day Moving Average
Avg Vol (3 month)
Shares Outstanding
Float
% Held by Insiders
% Held by Institutions
Shares Short
Short Ratio
Short % of Float
Shares Short (prior month)
Parsing
However, all of this data is locked up in HTML files. Thus, we need to build a parser. In this project, I did the parsing with regex, but please note that generally it is really not recommended to use regex to parse HTML. However, I think regex probably wins out for ease of understanding (this project being educational in nature), and from experience regex works fine in this case.

-This is the exact regex used:

r'>' + re.escape(variable) + r'.*?(\-?\d+\.*\d*K?M?B?|N/A[\\n|\s]*|>0|NaN)%?(</td>|</span>)'
While it looks pretty arcane, all it is doing is searching for the first occurence of the feature (e.g "Market Cap"), then it looks forward until it finds a number immediately followed by a </td> or </span> (signifying the end of a table entry). The complexity of the expression above accounts for some subtleties in the parsing:

the numbers could be preceeded by a minus sign
Yahoo Finance sometimes uses K, M, and B as abbreviations for thousand, million and billion respectively.
some data are given as percentages
some datapoints are missing, so instead of a number we have to look for "N/A" or "NaN.
Both the preprocessing of price data and the parsing of keystats are included in parsing_keystats.py. Run the following in your terminal:

- python parsing_keystats.py
You should see the file keystats.csv appear in your working directory. Now that we have the training data ready, we are ready to actually do some machine learning.

# Backtesting
In order to perform backtesting you must have some way of testing the performance of your algorithm before you live trade it.

Despite its importance, I originally did not want to include backtesting code in this repository. The reasons were as follows:

Backtesting is messy and empirical. The code is not very pleasant to use, and in practice requires a lot of manual interaction.

Backtesting is very difficult to get right, and if you do it wrong, you will be deceiving yourself with high returns.

Developing and working with your backtest is probably the best way to learn about machine learning and stocks – you'll see what works, what doesn't, and what you don't understand.

In order to perform a backtesting operation:

Run the following in terminal:

python backtesting.py
You should get something like this:

Classifier performance
======================
Accuracy score:  0.81
Precision score:  0.75

Stock prediction performance report
===================================
Total Trades: 177
Average return for stock predictions:  37.8 %
Average market return in the same period:  9.2%
Compared to the index, our strategy earns  28.6 percentage points more
Again, the performance looks too good to be true and almost certainly is.

-Current fundamental data
Now that we have trained and backtested a model on our data, we would like to generate actual predictions on current data.

-As always, we can scrape the data from good old Yahoo Finance. My method is to literally just download the statistics page for each stock (here is the page for Apple), then to parse it using regex as before.

-In fact, the regex should be almost identical, but because Yahoo has changed their UI a couple of times, there are some minor differences. This part of the projet has to be fixed whenever yahoo finance changes their UI, so if you can't get the project to work, the problem is most likely here.

-Run the following in terminal:

python current_data.py
The script will then begin downloading the HTML into the forward/ folder within your working directory, before parsing this data and outputting the file forward_sample.csv. You might see a few miscellaneous errors for certain tickers (e.g 'Exceeded 30 redirects.'), but this is to be expected.

## Stock prediction
Now that we have the training data and the current data, we can finally generate actual predictions. This part of the project is very simple: the only thing you have to decide is the value of the OUTPERFORMANCE parameter (the percentage by which a stock has to beat the S&P500 to be considered a 'buy'). I have set it to 10 by default, but it can easily be modified by changing the variable at the top of the file. Go ahead and run the script:

python stock_prediction.py
You should get something like this:

# 21 stocks predicted to outperform the S&P500 by more than 10%:
NOC FL SWK NFX LH NSC SCHL KSU DDS GWW AIZ ORLY R SFLY SHW GME DLX DIS AMP BBBY APD
Unit testing
I have included a number of unit tests (in the tests/ folder) which serve to check that things are working properly. However, due to the nature of the some of this projects functionality (downloading big datasets), you will have to run all the code once before running the tests. Otherwise, the tests themselves would have to download huge datasets (which I don't think is optimal).

-I thus recommend that you run the tests after you have run all the other scripts (except, perhaps, stock_prediction.py).

-To run the tests, simply enter the following into a terminal instance in the project directory:

pytest -v
Please note that it is not considered best practice to include an __init__.py file in the tests/ directory (see here for more), but I have done it anyway because it is uncomplicated and functional.

-Where to go from here
I have stated that this project is extensible, so here are some ideas to get you started and possibly increase returns (no promises).

-Data acquisition
My personal belief is that better quality data is THE factor that will ultimately determine your performance. Here are some ideas:

Explore the other subfolders in Sentdex's intraQuarter.zip.
Parse the annual reports that all companies submit to the SEC (have a look at the Edgar Database)
Try to find websites from which you can scrape fundamental data (this has been my solution).
Ditch US stocks and go global – perhaps better results may be found in markets that are less-liquid. It'd be interesting to see whether the predictive power of features vary based on geography.
Buy Quandl data, or experiment with alternative data.
Data preprocessing
Build a more robust parser using BeautifulSoup
In this project, I have just ignored any rows with missing data, but this reduces the size of the dataset considerably. Are there any ways you can fill in some of this data?
hint: if the PE ratio is missing but you know the stock price and the earnings/share...
hint 2: how different is Apple's book value in March to its book value in June?
Some form of feature engineering
e.g, calculate Graham's number and use it as a feature
some of the features are probably redundant. Why not remove them to speed up training?
Speed up the construction of keystats.csv.
hint: don't keep appending to one growing dataframe! Split it into chunks
Machine learning
Altering the machine learning stuff is probably the easiest and most fun to do.

-The most important thing if you're serious about results is to find the problem with the current backtesting setup and fix it. This will likely be quite a sobering experience, but if your backtest is done right, it should mean that any observed outperformance on your test set can be traded on (again, do so at your own discretion).

Try a different classifier – there is plenty of research that advocates the use of SVMs, for example. Don't forget that other classifiers may require feature scaling etc.

Hyperparameter tuning: use gridsearch to find the optimal hyperparameters for your classifier. But make sure you don't overfit!

Make it deep – experiment with neural networks (an easy way to start is with sklearn.neural_network).

Change the classification problem into a regression one: will we achieve better results if we try to predict the stock return rather than whether it outperformed?

Run the prediction multiple times (perhaps using different hyperparameters?) and select the k most common stocks to invest in. This is especially important if the algorithm is not deterministic (as is the case for Random Forest)
Experiment with different values of the outperformance parameter.

Should we really be trying to predict raw returns? What happens if a stock achieves a 20% return but does so by being highly volatile?

Try to plot the importance of different features to 'see what the machine sees'.

# Contributing

Feel free to fork, play around, and submit PRs. I would be very grateful for any bug fixes or more unit tests.
Feel free to add features to the program and use it.

