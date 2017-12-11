pullData2.py

Samuel L. Peoples

Interactive graphs can be found here:

https://public.tableau.com/profile/samuel.l.peoples#!/vizhome/CryptocurrencyOptimization/BacktestingAggressive1000Start

This script determines a low volatility, high returns portfolio between BTC, ETH, ETC, LTC, DASH, NEO, ZEC, XMR

Uses sharpe ratios and data from the last three months, saves files to a timestamped folder, and creates png figure for reference.

The information was then used to backtest the recommended model, as well as an aggressive model from the results. Given a $1000.00 investment, the recommended portfolio would have grown to over $2100.00 during the three-month period, while the aggressive grows to over $3000.00 in value. Because of digital currencies being inherently volatile, the Sharpe ratios are less reliable than one would desire, but is a good metric for portfolio analysis in this case.

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



based on John Geenty's article:

https://medium.com/@geenty/optimizing-your-cryptocurrency-portfolio-with-python-4c3d4c824a7f
