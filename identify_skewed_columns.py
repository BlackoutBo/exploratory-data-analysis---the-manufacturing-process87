import pandas as pd

class DataFrameTransform:
    """
    A utility class for performing EDA transformations on a pandas DataFrame.
    """

    def __init__(self, df: pd.DataFrame):
        """
        Initialize the DataFrameTransform instance with a DataFrame.

        Parameters:
            df (pd.DataFrame): The DataFrame to transform.
        """
        self.df = df

    def identify_skewed_columns(self, threshold=1.0):
        """
        Identify columns in the DataFrame that are skewed.

        Parameters:
            threshold (float): The skewness value threshold to identify skewed columns.
                               Columns with skewness greater than this threshold
                               are considered skewed.

        Returns:
            list: A list of column names that are skewed.
        """
        skewness = self.df.select_dtypes(include=['float64', 'int64']).skew()
        skewed_columns = skewness[abs(skewness) > threshold].index.tolist()
        
        print(f"Skewed columns (skewness > {threshold} or < -{threshold}):")
        print(skewness[abs(skewness) > threshold])
        
        return skewed_columns



if __name__ == "__main__":
    # Loads data
    df = pd.read_csv('Transformed_failure_data_modified.csv')
    
    # Create an instance of the DataFrameTransform class
    transformer = DataFrameTransform(df)
    
    # Identify skewed columns
    skewed_columns = transformer.identify_skewed_columns(threshold=1.0)
    
    print("Skewed columns:", skewed_columns)
