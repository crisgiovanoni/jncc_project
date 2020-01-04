import pandas as pd
import numpy as np

def get_guest():
    guest = pd.read_csv("guest_logs.csv",skiprows=4)
    guest.columns = ["trans_id","timestamp","name","item","item_group","status","quantity","subtotal","discount","tax","total","paid","refund","balance","acn","sys_id"]
    return guest