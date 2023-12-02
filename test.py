#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


def convertCatToNum(df, cat_cols):
    print(f" === {'Replace categorial variable'.center(35)} ===")
    for i in cat_cols:
        df[i] = df[i].replace(np.NaN, df[i].mode()[0])

    print(f" === {'Convert categorical to numerical'.center(35)} ===")
    df_processed = pd.get_dummies(df, columns=cat_cols)
    return df_processed
    


def drop_rows_with_missing(df, columns):
    print(f" === {'drop missing values'.center(35)} ===")
    df_processed = df.dropna(subset=columns)
    return df_processed


def normalize(dff,col_name_list):
    
    print(f" === {'Normalize data'.center(35)} ===")
    result = dff.copy()
    for feature_name in col_name_list:
        max_value = dff[feature_name].max()
        min_value = dff[feature_name].min()
        result[feature_name] = (dff[feature_name] - min_value) / (max_value - min_value)
    return result



from sklearn.preprocessing import LabelEncoder
import pandas as pd

def encode_player_names(df):
    """
    Encodes 'Player1_name' and 'Player2_name' columns using LabelEncoder.
    
    Parameters:
    - df (DataFrame): Input DataFrame containing 'Player1_name' and 'Player2_name' columns
    
    Returns:
    - df_encod (DataFrame): Transformed DataFrame with encoded name columns
    """
    print("=== Encoding player names ===")
    df_copy = df.copy()
    
    label_encoder = LabelEncoder()

    combined_series_player_name = pd.concat([df_copy['Player1_name'], df_copy['Player2_name']])
    label_encoder.fit(combined_series_player_name)

    df_copy['Player1_name_encoded'] = label_encoder.transform(df_copy['Player1_name'])
    df_copy['Player2_name_encoded'] = label_encoder.transform(df_copy['Player2_name'])

    df_encod = df_copy.drop(["Player1_name", "Player2_name"], axis=1)
    
    print("Encoding completed.")
    
    return df_encod


from sklearn.model_selection import train_test_split

def split_data(df_final, target_column='y', test_size=0.33, random_state=42):
    """
    Splits the DataFrame into train and test sets for machine learning.
    """
    print("=== Splitting data into train and test sets ===")

    Y = df_final[target_column]
    X = df_final.drop([target_column], axis=1)

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=random_state)
    
    print("Data split completed.")
    
    return x_train, x_test, y_train, y_test