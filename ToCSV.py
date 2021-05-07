import pandas as pd, yfinance as yf, numpy as np, json
import os, sys

ticker = "GME"
sdate, edate = "2021-01-25", "2021-02-02"
df = yf.download(ticker, start = sdate, end = edate, interval = "1h")
path = os.getcwd()
df.to_csv(path+"/GME.csv")