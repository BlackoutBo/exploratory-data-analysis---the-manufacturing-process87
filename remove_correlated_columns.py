import pandas as pd
import numpy as np

# Load DataFrame
df = pd.read_csv('Transformed_failure_data_with_no_outliers.csv')

# Select only numeric columns
numeric_df = df.select_dtypes(include=[float, int])

# Compute the correlation matrix
correlation_matrix = numeric_df.corr()

# Define a correlation threshold
threshold = 0.8  


# The line `highly_correlated_pairs = np.where(np.abs(correlation_matrix) > threshold)` is creating a
# mask to identify values in the correlation matrix that are above the defined threshold.
highly_correlated_pairs = np.where(np.abs(correlation_matrix) > threshold)


# This part of the code is iterating over the pairs of indices (i, j) where the absolute correlation
# value is above the defined threshold. It then extracts the column names corresponding to these
# indices from the correlation matrix and checks if the pair of column names is not already in the
# list `correlated_columns`. If the pair is not already in the list, it appends the pair of column
# names to the `correlated_columns` list.
correlated_columns = []
for i, j in zip(*highly_correlated_pairs):
    if i != j:  
        colname_1 = correlation_matrix.columns[i]
        colname_2 = correlation_matrix.columns[j]
        if (colname_2, colname_1) not in correlated_columns:
            correlated_columns.append((colname_1, colname_2))

# Print highly correlated pairs
print("Highly correlated columns:")
for col1, col2 in correlated_columns:
    print(f"{col1} and {col2}")


# The line `columns_to_drop = [col2 for _, col2 in correlated_columns]` is creating a list of column
# names that should be dropped from the original DataFrame based on the identified highly correlated
# pairs of columns.
columns_to_drop = [col2 for _, col2 in correlated_columns]

# Drop the columns from the original DataFrame
df_cleaned = df.drop(columns=columns_to_drop)

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cleaned_dataset.csv', index=False)

print(f"\nColumns removed: {columns_to_drop}")
print("The cleaned dataset has been saved.")
