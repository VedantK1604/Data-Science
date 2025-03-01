import pandas as pd

def preprocess(df, region_df):
    #Filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    #Merge with region_df
    df = df.merge(region_df, on='NOC', how='left')
    #dropping duplicates
    df.drop_duplicates(inplace=True)
    #One hot encoding on medals
    dummy = pd.get_dummies(df['Medal'])
    dummy = dummy.astype(int)
    df = pd.concat([df, dummy], axis=1)
    return df
