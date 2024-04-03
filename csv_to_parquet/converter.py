import pandas as pd

def csv_to_parquet(input_csv, output_parquet):
    """
    Convert a CSV file to Parquet format.

    Parameters:
        input_csv (str): Path to the input CSV file.
        output_parquet (str): Path to save the output Parquet file.
    """
    df = pd.read_csv(input_csv)
    df.to_parquet(output_parquet)
