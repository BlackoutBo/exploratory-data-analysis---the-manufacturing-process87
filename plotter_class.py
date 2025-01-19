import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Plotter:
    """
    A utility class for visualizing insights from a pandas DataFrame.
    """

    def __init__(self, df: pd.DataFrame):
        """
        Initialize the Plotter instance with a DataFrame.

        Parameters:
            df (pd.DataFrame): The DataFrame to visualize.
        """
        self.df = df

    def plot_missing_values(self):
        """
        Plot the percentage of missing values for each column in the DataFrame.
        """
        missing_percentage = self.df.isnull().mean() * 100
        missing_percentage = missing_percentage[missing_percentage > 0].sort_values(ascending=False)
        
        if missing_percentage.empty:
            print("No missing values to plot.")
            return
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x=missing_percentage.index, y=missing_percentage.values, palette="viridis")
        plt.title("Percentage of Missing Values by Column")
        plt.ylabel("Percentage")
        plt.xlabel("Column")
        plt.xticks(rotation=45)
        plt.show()

    def plot_distribution(self, column):
        """
        Plot the distribution of a specified column.

        Parameters:
            column (str): The name of the column to visualize.
        """
        if column not in self.df.columns:
            print(f"Column '{column}' not found in the DataFrame.")
            return

        plt.figure(figsize=(10, 6))
        sns.histplot(self.df[column], kde=True, bins=30, color='blue')
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()

    def plot_correlation_heatmap(self):
        """
        Plot a heatmap of correlations between numeric columns in the DataFrame.
        """
        numeric_cols = self.df.select_dtypes(include=['float64', 'int64'])
        if numeric_cols.empty:
            print("No numeric columns to plot a correlation heatmap.")
            return

        correlation_matrix = numeric_cols.corr()
        plt.figure(figsize=(12, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Heatmap")
        plt.show()

    def plot_outliers(self):
        """
        Plot box plots to visualize outliers for all numeric columns in the DataFrame.
        """
        numeric_cols = self.df.select_dtypes(include=['float64', 'int64'])
        if numeric_cols.empty:
            print("No numeric columns to plot outliers.")
            return
        
        for column in numeric_cols.columns:
            plt.figure(figsize=(10, 6))
            sns.boxplot(x=self.df[column])
            plt.title(f"Box Plot for Outliers in {column}")
            plt.xlabel(column)
            plt.show()


# Example: Loading a DataFrame (replace with your actual data file or DataFrame)
df = pd.read_csv("cleaned_dataset.csv")

# Create an instance of Plotter
plotter = Plotter(df)

# Plot missing values
plotter.plot_missing_values()

# Plot outliers for all numeric columns
plotter.plot_outliers()

# Plot the correlation heatmap
plotter.plot_correlation_heatmap()
