"""
Determines best portfolio allocation between BTC ETH ETC LTC DASH NEO ZEC XMR 
Uses sharpe ratio, finds low volatility with high returns. Designed to be ran Monthly
Author: Samuel L. Peoples
Version date: 20171208
"""
from urllib.request import urlopen
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import datetime
import re
import os


"""
buildCryptoList(html, name)
    html: list of urls
    name: list of currency names
This function builds the individual lists for the year,
For BTC ETH ETC LTC DASH NEO ZEC, XMR the function will pull
    Time, High price (USD), Low price (USD), Open Price (USD) 
    Close price (USD), Volume From, Volume To, and the Percent Returns
It will then save the data to [name]CurrencyHLOC.csv
"""
def buildCrpytoList(html, name):
    list = []
    htmlOpen = urlopen(html)
    htmlSoup = BeautifulSoup(htmlOpen, 'html.parser')
    htmlRows = str(htmlSoup).split('[')
    htmlRows = re.split("},{",htmlRows[1])
    htmlRows[0] = htmlRows[0].replace("{","")
    htmlRows[htmlRows.__len__()-1] = htmlRows[htmlRows.__len__()-1].partition("}")[0]
    for row in htmlRows:
        items = row.split(",")
        returns = returnVal(float(items[4].split(":")[1]),float(items[1].split(":")[1]))
        entry = {
            "Time":timeFix(items[0].split(":")[1]), 
            name+"Close":items[1].split(":")[1], 
            name+"High":items[2].split(":")[1], 
            name+"Low":items[3].split(":")[1], 
            name+"Open":items[4].split(":")[1], 
            name+"VolumeFrom":items[5].split(":")[1], 
            name+"VolumeTo":items[6].split(":")[1],
            name+"Returns":str(returns)}
        list.append(entry)
    df = pd.DataFrame(list)
    df.reindex(columns = ["Time",name+"High", name+"Low", name+"Open",name+"Close", name+"VolumeFrom", name+"VolumeTo", name+"Returns"]).to_csv(name+"CurrencyHLOC.csv", header ={"Time","High", "Low", "Open","Close", "VolumeFrom", "VolumeTo"})
    return df

"""
timeFix(timestamp)
    timestamp: unix UTC timestamp
This function converts timestamps to place legible timestamps in the dataset
"""
def timeFix(timestamp):
    return(datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S'))

"""
returnVal(num,den)
    num: open price
    den: close price
This function bypasses divZero errors.
"""
def returnVal(num, den):
    if den <=0:
        return 0
    else:
        diff = den-num
        return diff/num
"""
buildMaster(coins, coinsNames)
    coins: list of urls with coin data
    coinsNames: list of currency names
This fucntion builds the master list by merging all currency lists by date.
It will then save the data to MasterCurrencyHLOC.csv
"""
def buildMaster(coins, coinsNames):
    masterList = []
    for i in range(8):
        masterList.append(buildCrpytoList(coins[i], coinsNames[i]))
    masterDF = masterList[0].merge(masterList[1], left_on = "Time", right_on = 'Time', how= 'outer').merge(
        masterList[2], left_on = "Time", right_on = 'Time', how= 'outer').merge(
        masterList[3], left_on = "Time", right_on = 'Time', how= 'outer').merge(
        masterList[4], left_on = "Time", right_on = 'Time', how= 'outer').merge(
        masterList[5], left_on = "Time", right_on = 'Time', how= 'outer').merge(
        masterList[6], left_on = "Time", right_on = 'Time', how= 'outer').merge(
        masterList[7], left_on = "Time", right_on = 'Time', how= 'outer')
    masterDF.reindex(columns = [
        "Time",
        coinsNames[0]+"High",coinsNames[0]+"Low",coinsNames[0]+"Open",coinsNames[0]+"Close",coinsNames[0]+"VolumeFrom",coinsNames[0]+"VolumeTo",coinsNames[0]+"Returns",
        coinsNames[1]+"High",coinsNames[1]+"Low",coinsNames[1]+"Open",coinsNames[1]+"Close",coinsNames[1]+"VolumeFrom",coinsNames[1]+"VolumeTo",coinsNames[1]+"Returns",
        coinsNames[2]+"High",coinsNames[2]+"Low",coinsNames[2]+"Open",coinsNames[2]+"Close",coinsNames[2]+"VolumeFrom",coinsNames[2]+"VolumeTo",coinsNames[2]+"Returns",
        coinsNames[3]+"High",coinsNames[3]+"Low",coinsNames[3]+"Open",coinsNames[3]+"Close",coinsNames[3]+"VolumeFrom",coinsNames[3]+"VolumeTo",coinsNames[3]+"Returns",
        coinsNames[4]+"High",coinsNames[4]+"Low",coinsNames[4]+"Open",coinsNames[4]+"Close",coinsNames[4]+"VolumeFrom",coinsNames[4]+"VolumeTo",coinsNames[4]+"Returns",
        coinsNames[5]+"High",coinsNames[5]+"Low",coinsNames[5]+"Open",coinsNames[5]+"Close",coinsNames[5]+"VolumeFrom",coinsNames[5]+"VolumeTo",coinsNames[5]+"Returns",
        coinsNames[6]+"High",coinsNames[6]+"Low",coinsNames[6]+"Open",coinsNames[6]+"Close",coinsNames[6]+"VolumeFrom",coinsNames[6]+"VolumeTo",coinsNames[6]+"Returns",
        coinsNames[7]+"High",coinsNames[7]+"Low",coinsNames[7]+"Open",coinsNames[7]+"Close",coinsNames[7]+"VolumeFrom",coinsNames[7]+"VolumeTo",coinsNames[7]+"Returns",]
        ).to_csv(
            "MasterCurrencyHLOC.csv", header ={"Time","High", "Low", "Open", "Close","VolumeFrom", "VolumeTo"})
    return masterList

"""
This function builds the list of percent returns,
prints the percent returns for today and average percent returns for the year. 
It will then save the data to returns.csv
"""    
def buildReturns():
    data = pd.read_csv('MasterCurrencyHLOC.csv')
    data.set_index('Time',inplace=True)
    returns = data.drop(data.columns[[0,1,2,3,4,5,6,8,9,10,11,12,13,15,16,17,18,19,20,22,23,24,25,26,27,29,30,31,32,33,34,36,37,38,39,40,41,43,44,45,46,47,48,50,51,52,53,54,55]],axis =1)
    returns.to_csv("returns.csv")
    print ("Percent Returns on Closure:")
    print(returns.ix[-1])
    print()
    print("Average Percent Returns on Closure:")
    print(returns.mean())
    return returns

"""
optimize(masterList, returns)
    masterList: HLOC list with data for each currency
    returns: list of percent returns
This function will develop 30,000 randomized portfolios, and find the portfolio
with the highest sharpe ratio. (https://www.investopedia.com/terms/s/sharperatio.asp)
It then saves the results to sharpeRatios30kResults.csv and passes them to be plotted.
"""
def optimize(masterList, returns):
    mean_returns = returns.mean()
    matCov = returns.cov()
    coins = ["btc", "eth", "etc", "ltc", "dash", "neo", "zec", "xmr"]
    port = 30000
    results = np.zeros((4 + len(coins)-1, port))
    for i in range(port):
        weights = np.array(np.random.random(8))
        weights /= np.sum(weights)
        port_return = np.sum(mean_returns*weights)*5
        port_stdv = np.sqrt(np.dot(weights.T,np.dot(matCov, weights)))*np.sqrt(5)
        #Returns based on this portfolio
        results[0,i] = port_return
        #standard deviation based on this portfolio
        results[1,i] = port_stdv
        #Variance of this portfolio
        results[2,i] = results[0,i]/ results[1,i]
        #3: BTC
        #4: ETH
        #5: ETC
        #6: LTC
        #7: DASH
        #8: NEO
        #9: ZEC
        #10: XMR
        for j in range(len(weights)):
            results[j+3,i]= weights[j]
    pd.DataFrame(results).to_csv("sharpeRatios30kResults.csv")
    plotResults(results)

"""
plotResults(results)
    results: array of values from 30,000 portfolios
        % returns
        Std dev
        variance
        BTC allocation
        ETH allocation
        LTC allocation
        DASH allocation
        NEO allocation
        ZEC allocation
        XMR allocation
This function will develop the scatterplot of 30,000 portfolios,
x = Volatility, y = Returns
It then saves the figure to sharpeRatios30k.png.
The function will then print the suggested portfolio allocation, and
save the contents to recommendedPortfolio.csv
"""
def plotResults(results):
    heat = results[0]/results[2]
    scatter = []
    for i in range(30000):
        scatter.append([str(results[2][i]), 
                           str(results[0][i]),
                           "BTC: "+str(results[3][i]),
                            "ETH: "+str(results[4][i]),
                            "ETC: "+str(results[5][i]),
                            "LTC: "+str(results[6][i]),
                            "DASH: "+str(results[7][i]),
                            "NEO: "+str(results[8][i]),
                            "ZEC: "+str(results[9][i]),
                            "XMR: "+str(results[10][i])])
        if results[0][i]/ results[2][i] == max(heat):
            maxX = results[2][i]
            maxY = results[0][i]
            recommendedPortfolio = [
            "Recommended Portfolio Distribution:",
            "BTC: "+str(results[3][i]),
            "ETH: "+str(results[4][i]),
            "ETC: "+str(results[5][i]),
            "LTC: "+str(results[6][i]),
            "DASH: "+str(results[7][i]),
            "NEO: "+str(results[8][i]),
            "ZEC: "+str(results[9][i]),
            "XMR: "+str(results[10][i])]
    plt.scatter(x = results[2], y = results[0], c=[str(point/255.) for point in heat])
    plt.scatter(x = maxX, y = maxY, c = 200, s = 75, alpha = .2)
    plt.title('30,000 Portfolios, Sharpe Ratio')
    plt.xlabel('Volatility')
    plt.ylabel('Returns')
    plt.savefig("sharpeRatios30k.png")
    print()
    for line in recommendedPortfolio:
        print(line)
        
    pd.DataFrame(scatter).to_csv("scatterPoints.csv")
    pd.DataFrame(recommendedPortfolio).to_csv("recommendedPortfolio.csv")
    plt.show()
    
"""
Controls the implementation of the script, sets up urls and develops output files
"""
def main():
    path = re.split(" ",str(datetime.datetime.today()))[0]
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)
    btc = "https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=100&aggregate=3"
    eth = "https://min-api.cryptocompare.com/data/histoday?fsym=ETH&tsym=USD&limit=100&aggregate=3"
    etc = "https://min-api.cryptocompare.com/data/histoday?fsym=ETC&tsym=USD&limit=100&aggregate=3"
    ltc = "https://min-api.cryptocompare.com/data/histoday?fsym=LTC&tsym=USD&limit=100&aggregate=3"
    dash = "https://min-api.cryptocompare.com/data/histoday?fsym=DASH&tsym=USD&limit=100&aggregate=3"
    neo = "https://min-api.cryptocompare.com/data/histoday?fsym=NEO&tsym=USD&limit=100&aggregate=3"
    zec = "https://min-api.cryptocompare.com/data/histoday?fsym=ZEC&tsym=USD&limit=100&aggregate=3"
    xmr = "https://min-api.cryptocompare.com/data/histoday?fsym=XMR&tsym=USD&limit=100&aggregate=3"
    coins = [btc, eth, etc, ltc, dash, neo, zec, xmr]
    coinsNames = ["btc", "eth", "etc", "ltc", "dash", "neo", "zec", "xmr"]
    masterList = buildMaster(coins, coinsNames)
    returns = buildReturns()
    optimize(masterList, returns)
    
if __name__ == "__main__": main()

