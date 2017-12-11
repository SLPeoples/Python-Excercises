def optimize(returns):
    mean_returns = returns.mean()
    matCov = returns.cov()
    coins = ["btc", "eth", "etc", "ltc", "dash", "neo", "zec", "xmr"]
    port = 50000
    results = np.zeros((4 + len(coins)-1, port))
    for i in range(port):
        weights = np.array(np.random.random(8))
        weights /= np.sum(weights)
        port_return = np.sum(mean_returns*weights)*1140
        port_stdv = np.sqrt(np.dot(weights.T,np.dot(matCov, weights)))*np.sqrt(1140)
        #Returns based on this portfolio
        results[0,i] = port_return
        #standard deviation based on this portfolio
        results[1,i] = port_stdv
        #Variance of this portfolio
        results[2,i] = results[0,i]/ (results[1,i])
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
    pd.DataFrame(results).to_csv("sharpeRatios50kResults.csv")
    plotResults(results)

def plotResults(results):
    heat = results[0]/(results[2])
    scatter = []
    for i in range(50000):
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
        if results[0][i]/results[2][i] == max(heat):
            maxX = results[2][i]
            maxY = (results[0][i])
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
    plt.scatter(x = results[2], y = results[0], c=[str(point/255) for point in heat])
    plt.scatter(x = maxX, y = maxY, c = 200, s = 75, alpha = .2)
    plt.title('50,000 Portfolios, Sharpe Ratio')
    plt.xlabel('Volatility')
    plt.ylabel('Returns')
    plt.savefig("sharpeRatios50k.png")
    print()
    for line in recommendedPortfolio:
        print(line)
    pd.DataFrame(scatter).to_csv("scatterPoints.csv")
    pd.DataFrame(recommendedPortfolio).to_csv("recommendedPortfolio.csv")
    plt.show()
    
 def returns(path):
    returns = pd.read_csv(path)
    print ("Percent Returns on Closure:")
    print(returns.ix[-1])
    print()
    print("Average Percent Returns on Closure:")
    print(returns.mean())
    return returns
 
 def main():
    optimize(returns('returns.csv'))
    
if __name__ == "__main__": main()
