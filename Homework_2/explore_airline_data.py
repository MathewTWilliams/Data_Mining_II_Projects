import pandas as pd
import os

CWD = os.path.abspath(os.getcwd())
DATA_FILE = os.path.join(CWD, "Airline_Delay_Cause.csv")

def main(): 
    
    data_df = pd.read_csv(DATA_FILE, index_col=False)
    data_df.dropna(inplace=True)
    print(data_df.describe())


if __name__ == "__main__":
    main()