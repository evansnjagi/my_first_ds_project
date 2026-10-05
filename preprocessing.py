# Data processing scrip
import pandas as pd

# Import data
def load_data(filepath):
	return pd.read_csv(filepath)

# Clean df
def clean_data(df):
	return df.dropna(inplace=True)
