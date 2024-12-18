import inline as inline
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import inline
import yfinance as yf

assets = ['^NSEI','RELIANCE.NS', 'ADANIPORTS.NS', 'TCS.NS','LT.NS', 'MARUTI.BO']
pf_data =pd.DataFrame()

for a in assets:
    pf_data[a]=yf.download(a, start='2004-08-01', end='2024-10-29')['Adj Close']

print(pf_data.tail())

(pf_data/pf_data.iloc[0]*100).plot(figsize=(10,5))
plt.show()

log_returns= np.log(pf_data/pf_data.shift(1))
print(log_returns)

print(log_returns.mean()*250)
print(log_returns.cov()*250)
print(log_returns.corr())
num_assets=len(assets)
print(num_assets)
arr=np.random.random(2)
print(arr)
print(arr[0]+arr[1])

weights=np.random.random(num_assets)
weights/=np.sum(weights)
print(weights)
print(weights[0]+weights[1])

Expected_Portfolio_Return=np.sum(weights*log_returns.mean())*250
print(Expected_Portfolio_Return)
Expected_Portfolio_Variance=np.dot(weights.T, np.dot(log_returns.cov()*250,weights))
print(Expected_Portfolio_Variance)
Expected_Portfolio_Volatility=np.sqrt(np.dot(weights.T, np.dot(log_returns.cov()*250,weights)))
print(Expected_Portfolio_Volatility)

pfolio_returns=[]
pfolio_volatility=[]
for x in range(1000):
    weights=np.random.random(num_assets)
    weights /=np.sum(weights)
    pfolio_returns.append(np.sum(weights*log_returns.mean())*250)
    pfolio_volatility.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov()*250,weights))))
print(pfolio_returns,pfolio_volatility)


for x in range(1000):
    weights=np.random.random(num_assets)
    weights /=np.sum(weights)
    pfolio_returns.append(np.sum(weights*log_returns.mean())*250)
    pfolio_volatility.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov()*250,weights))))
pfolio_returns=np.array(pfolio_returns)
pfolio_volatility=np.array(pfolio_volatility)
print(pfolio_returns,pfolio_volatility)

portfolios= pd.DataFrame({'Return': pfolio_returns, 'Volatility': pfolio_volatility })
print(portfolios.head())
print(portfolios.tail())

portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10,6))
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
plt.show()
