import pandas as pd, yfinance as yf, numpy as np, json
import os, sys

sdate, edate = "2021-01-25", "2021-02-03"
df = yf.download("GME", start = sdate, end = edate, interval = "1h")
path = os.getcwd()
df.to_csv(path+"/GME.csv")
df = yf.download("AMC", start = sdate, end = edate, interval = "1h")
path = os.getcwd()
df.to_csv(path+"/AMC.csv")
