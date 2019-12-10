import pandas as pd
import time
from datetime import datetime

def lp(df,measurement,tag_key,field,value,datetime):
    lines= [str(df[measurement][d]) + "," 
            + str(tag_key) + "=" + str(df[tag_key][d]) 
            + " " + str(df[field][d]) + "=" + str(df[value][d]) 
            + " " + str(int(time.mktime(df[datetime][d].timetuple()))) + "000000000" for d in range(len(df))]
    return lines