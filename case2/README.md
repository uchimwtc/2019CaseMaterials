### Case 2: Options Market Making - Documentation
---
### Education
In the Github repo, you will find an education document outlining a crash course on options, as well as an Appendix containing a deeper dive into some more mathematically advanced material that we do not require for the purposes of this competition.  This material should be thought of as background reading to understand the theoretical world of the case and not as suggestive of any particular strategy or data design - the ideas you see in the education component may or may not be implemented in the generated data.

If you are interested in learning more beyond the provided materials, a sample of useful texts for understanding options pricing and trading is provided in the Appendix.

### Case Parameters
Some case parameters have changed since the case packet release - please pay close attention to changes in **bold**, as these changes differ from the content of the case packet.
- Each round will take place over one month of real-world time, and each round will end with **two months remaining until expiry** on all options.
- **Options contracts will not expire at the end of the round and will be valued at the midpoint of best bid and best ask at the end of the round.**
- The absolute delta portfolio limit is 25, and the absolute vega portfolio limit is 25.  Note that the Greeks library we have provided scales down the Black-Scholes vega by a multiplicative factor of 100 - we are placing a bound on scaled vega, not Black-Scholes vega.
- Exceeding the portfolio risk limits will result in a penalty of $0.01 per squared excess per second for each limit.  For example, holding a portfolio that has 30 delta for a minute will lead to a penalty of (30-25)^2 * $0.01 * 60 = $15.00.  If the vega of this portfolio was -30 during the same period, the cumulative penalty would be $30.00.
- The tradable instruments are $98, $99, $100, $101, and $102 calls and puts - the tradeable asset codes on options are C98PHX, P98PHX, C99PHX, P99PHX, C100PHX, P100PHX, C101PHX, P101PHX, C102PHX, and P102PHX.  The index asset code is IDX#PHX.

### Greeks Library
[vollib](http://vollib.org/) is a helpful utility for calculating options prices, options Greeks, and implied volatility.  To install vollib, run
```
$ pip install --user py_vollib
```
on your Vagrant virtual machine (or other workspace).  You can then
```python
import py_vollib.black-scholes as bs
```
and utilize the library to calculate options prices.  (Note we are using `py_vollib.black-scholes` and not `py_vollib.black` or `py_vollib.black-scholes-merton`.)
To calculate the Greeks, you must import either the `greeks.analytical` or `greeks.numerical` subpackage:
```python
import py_vollib.black-scholes.greeks.analytical as bsga
import py_vollib.black-scholes.greeks.numerical as bsgn
```
See [this link](http://vollib.org/documentation/python/1.0.2/apidoc/py_vollib.black_scholes.html) for more detailed documentation.

