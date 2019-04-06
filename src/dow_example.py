import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('djia.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

stks = ['NKE', 'IBM', 'JPM' ,'GE']

start = '2010'
end = '2016'

rtndf = df[stks][start:end].pct_change().dropna()
rtndf.hist(bins=50)

# Compute volatility of each stock
voldf = rtndf.std()

# write a csv file
voldf.to_csv('stkvol.csv')
voldf.to_pickle('stkvol.pkl')

pltflag = False

if pltflag:

    pltdf = df[start:end]

    # pandas fig 1 
    pltdf[stks].pct_change().plot()

    # pandas fig 2
    pltdf[stks].pct_change().dropna().cumsum().plot()

    ## Matplotlib plots
    plt.figure()

    for stkind in range(len(stks)): 
        plt.subplot(2,2,stkind+1)
        tmpdf = pltdf[stks[stkind]]
        plt.plot(tmpdf.index,tmpdf.values)
        plt.title('Prices of ' + stks[stkind] + ' from ' + start + ' to ' + end)
        plt.xlabel('Dates')
        plt.ylabel('Price')

    plt.show()

