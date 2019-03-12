import py_vollib.black_scholes.greeks.analytical as bsg

"""
2019 Midwest Trading Competition - Case 2
Library for calculating Greeks for options

***Note for more clarification on the provided functions, please visit 
http://vollib.org/documentation/python/1.0.2/apidoc/py_vollib.black.greeks.html#py-vollib-black-greeks-analytical
***Note: make sure you have py_vollib installed. 
To use, simply:

>>> import mwtc_case2_greeks as greeks
#example usage
>>> S = 49
>>> K = 50 
>>> t = 0.3846
>>> sigma = 0.2
>>> flag = 'c'
>>> greeks.delta(flag, S, K, t, sigma)
0.459828192740054
"""

#important for this case
def delta(flag, S, K, t, sigma):
    """
    Returns the Black-Scholes delta of an option, flagged as either 'c' (call) or 'p' (put)
    :param flag: 'c' for call, 'p' for put
    :param S: underlying price
    :param K: strike price
    :param t: time to expiration in years
    :param sigma: volatility
    :return: delta on a call or put option
    """
    return bsg.delta(flag, S, K, t, 0, sigma)

#important for this case
def vega(flag, S, K, t, sigma):
    """
    Returns the Black-Scholes vega of an option, flagged as either 'c' (call) or 'p' (put)
    :param flag: 'c' for call, 'p' for put
    :param S: underlying price
    :param K: strike price
    :param t: time to expiration in years
    :param sigma: volatility
    :return: vega on a call or put option
    """
    return bsg.vega(flag, S, K, t, 0, sigma)

def gamma(flag, S, K, t, sigma):
    """
    Returns the Black-Scholes gamma of an option, flagged as either 'c' (call) or 'p' (put)
    :param flag: 'c' for call, 'p' for put
    :param S: underlying price
    :param K: strike price
    :param t: time to expiration in years
    :param sigma: volatility
    :return: gamma on a call or put option
    """
    return bsg.gamma(flag, S, K, t, 0, sigma)

def theta(flag, S, K, t, sigma):
    """
    Returns the Black-Scholes theta of an option, flagged as either 'c' (call) or 'p' (put)
    :param flag: 'c' for call, 'p' for put
    :param S: underlying price
    :param K: strike price
    :param t: time to expiration in years
    :param sigma: volatility
    :return: theta on a call or put option
    """
    return bsg.theta(flag, S, K, t, 0, sigma)


