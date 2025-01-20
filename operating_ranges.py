import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Transformed_failure_data_with_no_outliers.csv')  # Update with the correct dataset name

# Columns of interest for the operating ranges
columns_of_interest = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']

# Display Operating Ranges of Key Parameters (overall)
def display_operating_ranges(df):
    # Calculate descriptive statistics (min, max, mean, std) for the columns of interest
    ranges_df = df[columns_of_interest].describe().transpose()
    return ranges_df

# Breakdown by Product Quality Types
def display_ranges_by_quality(df):
    quality_types = df['Type'].unique()
    ranges_by_quality = {}

    for quality in quality_types:
        quality_df = df[df['Type'] == quality]
        ranges_by_quality[quality] = display_operating_ranges(quality_df)

    return ranges_by_quality

# Plotting Tool Wear Distribution
def plot_tool_wear_distribution(df):
   
    plt.figure(figsize=(8, 6))
    sns.histplot(df['Tool wear [min]'], kde=True, bins=30, color='blue')
    plt.title('Distribution of Tool Wear [min]')
    plt.xlabel('Tool Wear [min]')
    plt.ylabel('Frequency')
    plt.show()

# Get overall operating ranges
operating_ranges = display_operating_ranges(df)
print("Operating Ranges (Overall):")
print(operating_ranges)

# Get breakdown by product quality type
ranges_by_quality = display_ranges_by_quality(df)
print("\nOperating Ranges by Product Quality:")
for quality, range_data in ranges_by_quality.items():
    print(f"\nRanges for Product Quality: {quality}")
    print(range_data)

# Plot the tool wear distribution
plot_tool_wear_distribution(df)








