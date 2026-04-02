import pandas as pd

def load_titanic_data(filepath):
    """
    Load Titanic dataset from CSV file.
    
    Parameters:
    -----------
    filepath : str
        Path to the titanic.csv file
    
    Returns:
    --------
    pd.DataFrame
        Titanic dataset
    """
    df = pd.read_csv(filepath)
    return df

def get_data_info(df):
    """
    Get basic information about the dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataset
    
    Returns:
    --------
    dict
        Basic dataset information
    """
    return {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'missing_values': df.isnull().sum().to_dict(),
        'dtypes': df.dtypes.to_dict()
    }
