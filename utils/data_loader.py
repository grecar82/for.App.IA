import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Load CSV data into a Pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise FileNotFoundError(f"Error loading file {file_path}: {e}")
