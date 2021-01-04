'''
Timeseries operation
Conform to HEC-convention.
'''
from scipy import stats
import numpy as np
import pandas as pd


def resample_hec_style(df, interval='D'):
    '''
    Resampling of time series in DataFrame provided for the interval (see Pandas resample for codes)
    In addition to conform to HEC-conventions the resampling is done with closed="right" and label="right"
    see pandas resample documentation to understand these arguments
    '''
    return df.resample(interval, closed='right', label='right')


def per_aver(df, interval='D'):
    '''
    PermissionErroriod averages of the time series in DataFrame provided for the interval (see Pandas resample for codes)
    In addition to conform to HEC-conventions the resampling is done with closed="right" and label="right"
    '''
    return resample_hec_style(df, interval).mean()


def per_max(df, interval='D'):
    return resample_hec_style(df, interval).max()


def per_min(df, interval='D'):
    return resample_hec_style(df, interval).min()


def mse(series1: pd.Series, series2: pd.Series):
    """Mean Squared Error (MSE)

    Args:

        series1 (Series or single value): 
        series2 (Series or single value): 

    Returns:

        Mean squared error
    """
    diff = series1-series2
    diff2=diff*diff
    try:
        return diff2.mean()/len(diff2)
    except (AttributeError,TypeError):
        return diff2

def rmse(series1, series2):
    return np.sqrt(mse(series1, series2))


def mean_error(series1, series2):
    return (series1-series2).mean()


def nash_sutcliffe(series1, series2):
    """https://en.wikipedia.org/wiki/Nash%E2%80%93Sutcliffe_model_efficiency_coefficient


    Args:

        series1 (Series): Can be considered as model in the URL above
        series2 (Series): Can be considered the observed in the URL above

    Returns:

        Nash Sutcliffe Efficiency
    """
    return 1-mse(series1, series2)/mse(series2, series2.mean())


def percent_bias(series1, series2):
    """Percent bias (PBIAS) measures the average tendency 
    of the simulated values to be larger or smaller than their observed ones.

    https://rdrr.io/cran/hydroGOF/man/pbias.html#:~:text=Percent%20bias%20(PBIAS)%20measures%20the,values%20indicating%20accurate%20model%20simulation

    Args:

        series1 (Series): can be considered as model
        series2 (Serie): can be considered as observed or target

    Returns:

        float : percent bias
    """    
    return 100*((series1.sum()-series2.sum())/series2.sum())

def linregress(xseries, yseries):
    return stats.linregress(xseries, yseries)
