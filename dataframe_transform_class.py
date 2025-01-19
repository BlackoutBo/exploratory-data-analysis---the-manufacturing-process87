import pandas as pd
import numpy as np

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

    def missing_value_summary(self):
        """
        Summarize missing values in the DataFrame.

        Returns:
            pd.DataFrame: A DataFrame with column names, null counts, and null percentages.
        """
        null_counts = self.df.isnull().sum()
        total_rows = len(self.df)
        null_percentage = (null_counts / total_rows) * 100
        summary = pd.DataFrame({
            'Null Count': null_counts,
            'Null %': null_percentage
        }).sort_values(by='Null %', ascending=False)
        return summary

    def drop_missing_data(self, threshold=50.0, axis=0):
        """
        Drop rows or columns with missing data above a certain threshold.

        Parameters:
            threshold (float): The percentage threshold for missing data. Defaults to 50% for dropping.
            axis (int): Whether to drop rows (0) or columns (1). Defaults to 0 (rows).

        Returns:
            pd.DataFrame: A DataFrame after dropping the specified data.
        """
        missing_percentage = self.df.isnull().mean() * 100
        if axis == 1:
            to_drop = missing_percentage[missing_percentage > threshold].index
            self.df.drop(columns=to_drop, inplace=True)
        elif axis == 0:
            self.df.dropna(thresh=int((100-threshold)/100 * self.df.shape[1]), inplace=True)

    def impute_missing_values(self, method='mean', columns=None):
        """
        Impute missing values in the DataFrame using specified statistical methods.

        Parameters:
            method (str): The method to use for imputation ('mean', 'median', 'mode').
            columns (list): The columns to impute. If None, impute all columns with missing values.

        Returns:
            None: Modifies the DataFrame in-place.
        """
        if columns is None:
            columns = self.df.columns[self.df.isnull().any()]

        for column in columns:
            if method == 'mean':
                self.df[column].fillna(self.df[column].mean(), inplace=True)
            elif method == 'median':
                self.df[column].fillna(self.df[column].median(), inplace=True)
            elif method == 'mode':
                self.df[column].fillna(self.df[column].mode()[0], inplace=True)
            else:
                print(f"Unknown method: {method}. Supported methods are 'mean', 'median', and 'mode'.")

    def drop_columns_with_nulls(self, threshold=20.0):
        """
        The function `drop_columns_with_nulls` drops columns from a DataFrame based on a specified
        threshold percentage of NULL values.
        
        :param threshold: The `threshold` parameter in the `drop_columns_with_nulls` function represents
        the percentage of null values in a column above which that column will be dropped from the
        DataFrame. By default, the threshold is set to 20.0%, but you can adjust this threshold value as
        needed when calling the
        :return: the DataFrame after dropping columns with a NULL percentage greater than the specified
        threshold.
        """
        
        
        null_percentage = self.df.isnull().mean() * 100
        
        
        columns_to_drop = null_percentage[null_percentage > threshold].index.tolist()
        
        
        if columns_to_drop:
            print(f"Dropping the following columns with NULL percentage > {threshold}%:")
            print(columns_to_drop)
        else:
            print(f"No columns have NULL percentage > {threshold}%. No columns will be dropped.")
        
        
        self.df.drop(columns=columns_to_drop, inplace=True)

        return self.df

    def identify_skewed_columns(self, threshold=1.0):
        """
        The function `identify_skewed_columns` identifies columns in a DataFrame that have skewness
        greater than a specified threshold.
        
        :param threshold: The `identify_skewed_columns` function takes a DataFrame as input and
        identifies columns that are skewed based on a specified threshold value. The threshold parameter
        is used to determine the level of skewness at which a column is considered skewed. Columns with
        skewness values greater than the threshold are identified as skewed columns
        :return: The function `identify_skewed_columns` returns a list of column names from the
        DataFrame `self.df` that have a skewness value greater than the specified threshold (default
        threshold is 1.0).
        """
        
        numeric_columns = self.df.select_dtypes(include=[np.number])
        
        
        skewed_columns = numeric_columns.skew().index[numeric_columns.skew().abs() > threshold].tolist()
        
        return skewed_columns

    def transform_skewed_columns(self, skewed_columns):
        """
        The function `transform_skewed_columns` applies a logarithmic transformation to columns with
        minimum values less than or equal to 0, and a square root transformation to other columns in a
        DataFrame.
        
        :param skewed_columns: The `skewed_columns` parameter in the `transform_skewed_columns` method
        is a list of column names in a DataFrame that are considered to be skewed. The method applies a
        transformation to these columns to reduce skewness in the data
        :return: the DataFrame after transforming the skewed columns.
        """
        
        for column in skewed_columns:
            if self.df[column].min() <= 0:  
                self.df[column] = np.log1p(self.df[column])
            else:
                
                self.df[column] = np.sqrt(self.df[column])
        
        return self.df

    def remove_outliers_iqr(self, threshold=1.5):
        """
        The function `remove_outliers_iqr` removes outliers from numeric columns in a DataFrame using
        the interquartile range method with a specified threshold.
        
        :param threshold: The `threshold` parameter in the `remove_outliers_iqr` function is used to
        determine how far away from the IQR (Interquartile Range) the data points need to be in order to
        be considered outliers. By default, the threshold is set to 1.5, but
        :return: The function `remove_outliers_iqr` is returning the DataFrame `self.df` after removing
        the outliers based on the interquartile range (IQR) method with the specified threshold value.
        """
    
        
        numeric_columns = self.df.select_dtypes(include=[np.number])

        
        Q1 = numeric_columns.quantile(0.25)
        Q3 = numeric_columns.quantile(0.75)
        IQR = Q3 - Q1

        
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR

        
        self.df = self.df[~((numeric_columns < lower_bound) | (numeric_columns > upper_bound)).any(axis=1)]

        return self.df


# The code block you provided is the main part of the script that performs various data
# transformations on a DataFrame loaded from a CSV file named 'Transformed_failure_data_modified.csv'.
# Here is a breakdown of what each step is doing:
if __name__ == "__main__":
    
   # The line `df = pd.read_csv('Transformed_failure_data_modified.csv')` is reading a CSV file named
   # 'Transformed_failure_data_modified.csv' into a pandas DataFrame called `df`. The data in the CSV
   # file is being loaded into memory and stored in the variable `df` for further data transformations
   # and analysis using pandas and other methods defined in the script.
    df = pd.read_csv('Transformed_failure_data_modified.csv')
    
    
    # `transformer = DataFrameTransform(df)` is creating an instance of the `DataFrameTransform` class
    # by passing the pandas DataFrame `df` as an argument to the constructor of the class. This
    # instance, named `transformer`, will allow you to perform various data transformation operations
    # defined within the `DataFrameTransform` class on the DataFrame `df`. This approach encapsulates
    # the DataFrame and the transformation methods within a single object, making it easier to apply
    # multiple transformations to the DataFrame using the methods provided by the class.
    transformer = DataFrameTransform(df)
    
   
    # The line `skewed_columns = transformer.identify_skewed_columns(threshold=1.0)` is calling the
    # method `identify_skewed_columns` from the `DataFrameTransform` class instance `transformer`.
    skewed_columns = transformer.identify_skewed_columns(threshold=1.0)
    
    
    # The line `df_transformed = transformer.transform_skewed_columns(skewed_columns)` is calling the
    # `transform_skewed_columns` method from the `DataFrameTransform` class instance `transformer`.
    df_transformed = transformer.transform_skewed_columns(skewed_columns)
    
    
    # The line `df_no_outliers = transformer.remove_outliers_iqr(threshold=1.5)` is calling the
    # `remove_outliers_iqr` method from the `DataFrameTransform` class instance `transformer` with a
    # threshold value of 1.5.
    df_no_outliers = transformer.remove_outliers_iqr(threshold=1.5)
    
   
    # The line `df_no_outliers.to_csv('Transformed_failure_data_with_no_outliers.csv', index=False)`
    # is saving the modified DataFrame `df_no_outliers` to a CSV file named
    # 'Transformed_failure_data_with_no_outliers.csv' without including the index column in the CSV
    # file.
    df_no_outliers.to_csv('Transformed_failure_data_with_no_outliers.csv', index=False)
    
    # The line `print("Transformation complete. The modified DataFrame has been saved.")` is simply
    # displaying a message to the user indicating that the data transformation process has been
    # completed successfully and the modified DataFrame has been saved to a CSV file named
    # 'Transformed_failure_data_with_no_outliers.csv'. This message serves as a notification to inform
    # the user that the operations defined in the script have been executed without any errors and the
    # final transformed data is available for further analysis or use.
    print("Transformation complete. The modified DataFrame has been saved.")
