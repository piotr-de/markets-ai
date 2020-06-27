#!/usr/bin/env python
# coding: utf-8

# In[64]:


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[84]:


spx = yf.Ticker("SP=F")
gold = yf.Ticker("GC=F")

spx_gold = pd.DataFrame({
    "SPX": spx.history(period="10y")["Close"],
    "Gold": gold.history(period="10y")["Close"]
},
    columns=["SPX", "Gold"]
)

spx_gold = spx_gold.sort_values(by="Date", ascending=False)

print(spx_gold)


# In[ ]:


get_ipython().system('jupyter nbconvert --to python *.ipynb')
