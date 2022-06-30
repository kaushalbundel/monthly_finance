import pandas as pd
import numpy as np
import warnings
pd.set_option('display.expand_frame_repr', False)
warnings.filterwarnings('ignore')

def data_preprocessing(filename):
    #reading the excel input file, extracting only the data which is useful for the data analysis purposes
    df=pd.read_excel(filename, skiprows=12, usecols="C:I")
    #removing the legends in the botton of the documents
    df=df.drop(df.tail(28).index)
    #Removing blank values
    na_index=df.index[df['Balance (INR )'].isna()== True].to_list()
    df=df.drop(na_index).reset_index(drop=True)
    #renaming columns so that data processing becomes easier
    df.columns=['v_date','t_date','cheque','remarks','withdrawl','deposit','balance']
    #converting transaction date object into datetime field for analysis purposes
    df['t_date']=pd.to_datetime(df['t_date'], dayfirst=True)
    #converting remarks into lowercase so that logic can be applied to create categories
    df['remarks']=df['remarks'].apply(lambda x: x.lower())
    #logic for creating different categories
    df.insert(len(df.columns),"category","NaN") #for creating category column 
    for i in range(len(df['remarks'])):
        if "amazon" in df['remarks'][i]:
            df['category'][i]="Shoping"
        elif "bigbasket" in df['remarks'][i]:
            df['category'][i]="Shoping"
        elif "food" in df['remarks'][i]:
            df['category'][i]="Food"
        elif "ajit servic" in df['remarks'][i]:
            df['category'][i]="Fuel"
        elif "billdesk" in df['remarks'][i]:
            df['category'][i]="Utility"
        elif "indianclrcorpltd" in df['remarks'][i]:
            df['category'][i]="Investment"
        elif "sipnasdaq100" in df['remarks'][i]:
            df['category'][i]="Investment"
        elif "irctc" in df['remarks'][i]:
            df['category'][i]="Travel"
        elif "zomato" in df['remarks'][i]:
            df['category'][i]="Food"
        elif "swiggy" in df['remarks'][i]:
            df['category'][i]="Food"
        elif "medicines" in df['remarks'][i]:
            df['category'][i]="Medicines"
        elif "cash wdl" in df['remarks'][i]:
            df['category'][i]="Cash"
        elif "imps" in df['remarks'][i]:
            df['category'][i]="Money Transfer"
        elif "add-money@paytm" in df['remarks'][i]:
            df['category'][i]="Paytm Transfer"
        elif "nisha" in df['remarks'][i]:
            df['category'][i]="Nisha"
        elif "cred" in df['remarks'][i]:
            df['category'][i]="Credit Card Payment"
        else:
            df['category'][i]="Others"
    return df