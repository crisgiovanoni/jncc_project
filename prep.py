import pandas as pd
import re

def normalize_dollars(series):
    series = series.str.replace(r"$","").str.replace(r",","").astype("float")
    return series

def convert_to_float(df):
    dollar_values = ["subtotal","discount","tax","total","paid","refund","balance"]
    for column in dollar_values:
        df[column] = normalize_dollars(df[column])
    return df