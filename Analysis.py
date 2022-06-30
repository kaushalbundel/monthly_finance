import pandas as pd
import numpy as np
import warnings
pd.set_option('display.expand_frame_repr', False)

warnings.filterwarnings('ignore')
def money_in(dataframe):
    return dataframe['deposit'].sum(), dataframe[dataframe['deposit']>0].sort_values(by=['deposit'], ascending=False)

def money_out(dataframe):
    return dataframe['withdrawl'].sum(), dataframe[dataframe['withdrawl']>0].sort_values(by=['withdrawl'], ascending=False).head(10)

def withdrawl_analysis(dataframe):
    table = pd.pivot_table(dataframe, values='withdrawl', index='category', aggfunc=np.sum).sort_values(by='withdrawl', ascending=False)
    table['% withdrawal']= (table['withdrawl']/table['withdrawl'].sum())*100
    table['% withdrawal']=table['% withdrawal'].round(2)
    return table

def others_analysis(dataframe):
    return dataframe[dataframe['category']=='Others'].sort_values(by=['withdrawl'], ascending=False).head(20)

def summary(dataframe):
    return dataframe['deposit'].sum()-dataframe['withdrawl'].sum()