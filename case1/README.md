# Case 1 Documentation

## Education Materials

In order to get acquainted with interest rates and interest rate derivatives we recommend reading Chapters 4, 6, and 7 in Options, Futures, and Other Derivatives by Hull, eighth edition.
We also recommend reading the following blog post: 

https://www.clarusft.com/mechanics-and-definitions-of-spread-and-butterfly-swap-packages/

Both the blog post and Hull readings include information about a very related instrument to interest rate futures: interest rate swaps.  We do not recommend ignoring the swap related readings.  The difference between a vanilla interest rate swap and an interest rate future is that a swap is payed for at the time of expiry while futures are paid for up front.  You can assume for this case that the cost of financing a cash position is negligible (i.e. market participants can borrow/lend money at ~0% rate; remember that this is only true in a theoretical sense; your positions will be liquidated and so you cannot carry a position that would require financing).  Thus, the futures can be treated like swaps in this market.  Nonetheless, we do not recommend directly using any strategies in the readings, but rather we encourage you to think about how they could be adapted to this market given the data you will be provided.  

## Price Setter Documentation

In the Case 1 release (see [here](https://drive.google.com/open?id=1_DhkZVWRar_6GntGGYfyRt_zdi7C7oA2)) we have provided you with a trading bot that sets prices on a locally-running deployment of an χChange exchange server to match theoretical prices in a hidden set of training data. This bot is provided in a case_one_bot.tar file that, when unzipped (tar -xvf case_one_bot.tar) provides two files: case_one_bot.par and price_setter_config.json. The former is a compiled binary of the aforementioned trading bot and can be run
in the standard manner (python case_one_bot.par). Ensure that a χChange exchange server is simultaneously running locally when you run the case_one_bot.par. The second file is a configuration file that the Case 1 bot uses and provides information such as the expected amount of liquidity at the best bid and ask. Feel free to modify this file to see how your solution to Case 1 performs under different liquidity levels but bear in mind that the parameters set in this file are
representative of the configuration that the Case 1 bot will be run with on competition day.


Note that we do not provide you with raw data files with a timeseries of the theoretical values of the assets traded in Case 1. We expect you to collect this data yourself directly from the exchange. This requirement was a conscious choice on the part of the case writers: because the behavior of the Case 1 bot is non-deterministic at the level of market microstructure, it allows you to collect many different variations in how the theoretical data might be played back, and especially
allows you to analyze how the data playback responds to your own market activity. Remember that you will be trading directly against all the other competitors on competition day, so the ability of your bot to respond to changes in market microstructure and liquidity will be essential to a robust performance on this case.


One further note: keep in mind that, due to speed of light constraints when communicating with the datacenter in which χChange will be hosted, you will experience significantly more latency on competition day than when testing your bots locally. In our own testing, we have experienced approximately 30-40ms Round-Trip Latency when communicating with the χChange datacenter from the UChicago network. Compare this to the tenths of a millisecond Round-Trip latency experienced when testing
locally. Successful competitors will thus take this latency into account in their implementation.
