import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Transformed_failure_data_with_no_outliers.csv')  

# Calculate Total Failures and Failure Percentage
def calculate_failure_rate(df):
    
    failure_columns = ['Machine failure', 'Tool wear failure', 'Head dissipation failure', 
                       'Power failure', 'Overstrain failure', 'Random failure']
    
    # Calculate the total number of failures
    total_failures = df[failure_columns].sum().sum()
    
    # Calculate the total number of records in the dataset
    total_records = len(df)
    
    # Calculate the failure percentage
    failure_percentage = (total_failures / total_records) * 100
    
    return total_failures, failure_percentage, total_records

# Get failure rate details
total_failures, failure_percentage, total_records = calculate_failure_rate(df)
print(f"Total Failures: {total_failures}")
print(f"Failure Percentage: {failure_percentage:.2f}% of total records ({total_records} records in total)")

# Breakdown of Failures by Product Quality Type
def failure_by_product_quality(df):
    
    failure_columns = ['Machine failure', 'Tool wear failure', 'Head dissipation failure', 
                       'Power failure', 'Overstrain failure', 'Random failure']
    
    # Group by 'Type' and sum failure causes, exclude 'Type' column from result
    quality_failures = df.groupby('Type')[failure_columns].sum().sum(axis=1)
    return quality_failures

# Get failure count by quality type
quality_failures = failure_by_product_quality(df)
print("\nFailures by Product Quality:")
print(quality_failures)

# Visualization of Failures by Product Quality Type
def plot_failures_by_quality(df):
   
    quality_failures = failure_by_product_quality(df)
    
    # Create the bar plot
    plt.figure(figsize=(8, 6))
    sns.barplot(x=quality_failures.index, y=quality_failures.values, hue=quality_failures.index, palette='viridis', legend=False)
    plt.title('Number of Failures by Product Quality Type')
    plt.xlabel('Product Quality')
    plt.ylabel('Number of Failures')
    plt.show()

# Plot failures by product quality type
plot_failures_by_quality(df)

# Leading Causes of Failures
def plot_leading_causes_of_failure(df):
    
    failure_columns = ['Machine failure', 'Tool wear failure', 'Head dissipation failure', 
                       'Power failure', 'Overstrain failure', 'Random failure']
    
    # Calculate total failures for each cause
    failure_counts = df[failure_columns].sum()
    
    # Create a bar plot of failure causes
    plt.figure(figsize=(8, 6))
    sns.barplot(x=failure_counts.index, y=failure_counts.values, hue=failure_counts.index, palette='Blues_d', legend=False)
    plt.title('Number of Failures by Cause')
    plt.xlabel('Failure Cause')
    plt.ylabel('Number of Failures')
    plt.show()

# Plot leading causes of failure
plot_leading_causes_of_failure(df)



