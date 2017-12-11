pullData2.py

Samuel L. Peoples

Interactive graphs can be found here:

https://public.tableau.com/profile/samuel.l.peoples#!/vizhome/CryptocurrencyOptimization/BacktestingAggressive1000Start

>The views contained in this post are my own and do not represent investment advise, the views of my employer or anyone else. This content is intended to be used and must be used for informational purposes only. It is very important to do your own analysis before making any investment based on your own personal circumstances. You should take independent financial advice from a professional in connection with, or independently research and verify, any information that you find in this post and wish to rely upon, whether for the purpose of making an investment decision or otherwise.

This script determines a low volatility, high returns portfolio between BTC, ETH, ETC, LTC, DASH, NEO, ZEC, XMR

Uses sharpe ratios and data from the last three months, saves files to a timestamped folder, and creates png figure for reference.

The information was then used to backtest the recommended model, as well as an aggressive model from the results. Given an initial investment of $1000.00 on 19 September 2017, the recommended portfolio would have grown to over $2100.00 during the three-month period, while the aggressive grows to over $3000.00 in value. Because of digital currencies being inherently volatile, the Sharpe ratios are less reliable than one would desire, but is a good metric for portfolio analysis in this case.

A safe conclusion to draw, regardless of discrete investment is that LTC and NEO are two low volatility, yet moderate-to-high returns currencies which should be monitored, while BTC and DASH are two highly variable currencies that have grown quickly in value over the last three months. Coupled with any other insights that can be drawn from the market, I think this was a very exciting exercise.

2017-12-10 run:

https://i.imgur.com/TdUEAkS.png

Recommended Portfolio Distribution (scatterPoints.csv [34607]):
* BTC: 0.0180410176875
* ETH: 0.00377590859407
* ETC: 0.00315474140452
* LTC: 0.366286372076
* DASH: 0.00114576353705
* NEO: 0.463456037585
* ZEC: 0.000253851426288
* XMR: 0.14388630769

Returns:

https://i.imgur.com/YbXXVMK.png

Aggressive Portfolio Distribution(scatterPoints.csv [27989]):
* BTC: 0.51007444775
* ETH: 0.0123708535254
* ETC: 0.0872447919173
* LTC: 0.0907395166206
* DASH: 0.138406313313
* NEO: 0.08129648342
* ZEC: 0.0520898783671
* XMR:  0.0277777150871

Returns: 

https://i.imgur.com/KMUYA6P.png

_____

The way it's written, it calls eight API locations, then develops their historical data individually, merges the datasets, 
then calculates and populates a returns array which has information for each date, as well as a consistent source for returns 
information, since it can vary from exchange to exchange. From there it creates fifty thousand randomized arrays of varying 
distribution, and finds the appropriate points, as well saving the data. 

If you have a similar dataset that you'd personally want to test, then you could just copy optimizePlot.py, with an input dataset 
that looks like this:

* https://i.imgur.com/D2CSV8g.png 

You then get these two:

* https://i.imgur.com/2rx5Ask.png 

as part of your output, which you can use to plot the points in another program (such as tableau) and navigate the dataset, 
such as here:

* https://i.imgur.com/cU8PrOa.png 

where I've chosen to focus on a portfolio that was not recommended, but could be chosen for its high returns, depending on a person's 
risk tolerance. 

based on John Geenty's article:

https://medium.com/@geenty/optimizing-your-cryptocurrency-portfolio-with-python-4c3d4c824a7f
