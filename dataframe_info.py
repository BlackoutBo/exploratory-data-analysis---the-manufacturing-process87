import pandas as pd

class DataFrameInfo:
    """
    A utility class for performing Exploratory Data Analysis (EDA) on a pandas DataFrame.
    """

    def __init__(self, df: pd.DataFrame):
        """
        Initialize the DataFrameInfo instance with a DataFrame.

        Parameters:
            df (pd.DataFrame): The DataFrame to inspect.
        """
        self.df = df

    def describe_columns(self):
        """
        Describe all columns in the DataFrame to check their data types and other column properties.

        Returns:
            pd.DataFrame: A DataFrame with column names, data types, null counts, and unique value counts.
        """
        description = pd.DataFrame({
            "Column Name": self.df.columns,
            "Data Type": [self.df[col].dtype for col in self.df.columns],
            "Null Count": [self.df[col].isnull().sum() for col in self.df.columns],
            "Unique Values": [self.df[col].nunique() for col in self.df.columns]
        })
        return description

    def column_stats(self):
        """
        Extract statistical values: mean, median, standard deviation from numeric columns.

        Returns:
            pd.DataFrame: A DataFrame containing mean, median, and standard deviation for each numeric column.
        """
        numeric_cols = self.df.select_dtypes(include=['int64', 'float64'])
        stats = pd.DataFrame({
            'Mean': numeric_cols.mean(),
            'Median': numeric_cols.median(),
            'Std Dev': numeric_cols.std()
        })
        return stats

    def count_distinct(self, column):
        """
        Count the distinct values in a specified column.

        Parameters:
            column (str): The name of the column to count distinct values for.

        Returns:
            int: The number of distinct values in the column.
        """
        return self.df[column].nunique()

    def null_value_counts(self):
        """
        Generate a count of NULL values for each column and their percentage.

        Returns:
            pd.DataFrame: A DataFrame with column names, null counts, and null percentages.
        """
        null_counts = self.df.isnull().sum()
        total_rows = len(self.df)
        null_percentage = (null_counts / total_rows) * 100
        null_summary = pd.DataFrame({
            'Null Count': null_counts,
            'Null %': null_percentage
        })
        return null_summary

    def data_shape(self):
        """
        Print the shape of the DataFrame.

        Returns:
            tuple: A tuple containing the number of rows and columns.
        """
        return self.df.shape

    def describe_categorical_columns(self):
        """
        Print the count and percentage of distinct values in each categorical column.

        Returns:
            pd.DataFrame: A DataFrame summarizing the count and percentage of distinct values.
        """
        categorical_cols = self.df.select_dtypes(include=['category'])
        summary = {}
        for col in categorical_cols:
            value_counts = self.df[col].value_counts()
            total = len(self.df[col])
            summary[col] = {
                'Value Counts': value_counts,
                'Total': total,
                'Value Percentages': value_counts / total * 100
            }
        return summary

    def info(self):
        """
        Print a high-level summary of the DataFrame, including column data types and non-null counts.
        """
        return self.df.info()


csv_file_path = 'transformed_failure_data.csv'
df = pd.read_csv(csv_file_path, dtype={'Type': 'category'})


df_info = DataFrameInfo(df)


print("Column Description:")
print(df_info.describe_columns())

print("\nStatistical Summary:")
print(df_info.column_stats())

print("\nNull Value Counts:")
print(df_info.null_value_counts())

print("\nData Shape:")
print(df_info.data_shape())

print("\nCategorical Column Summary:")
print(df_info.describe_categorical_columns())

