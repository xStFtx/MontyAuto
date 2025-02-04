import pandas as pd

def clean_csv(input_file: str, output_file: str) -> None:
    """
    Clean CSV file by:
    - Removing empty rows
    - Removing duplicates
    - Standardizing headers
    """
    df = pd.read_csv(input_file)
    
    # Clean headers
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Clean data
    df = df.dropna(how='all')
    df = df.drop_duplicates()
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    import sys
    clean_csv(sys.argv[1], sys.argv[2]) 