import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Load the dataset
df = pd.read_csv('Transformed_failure_data_with_no_outliers.csv')

# List of failure types and machine settings
failure_types = ['Tool wear failure', 'Head dissipation failure', 'Power failure', 
                 'Overstrain failure', 'Random failure']
machine_settings = ['Air temperature [K]', 'Process temperature [K]', 
                    'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']

# Correlation Analysis for Each Failure Type
def analyze_failure_correlations(df, failure_types, machine_settings):
    insights = {}
    
    for failure in failure_types:
        print(f"\nAnalyzing {failure}...\n")
        failure_insights = {}
        
        # Separate failure and non-failure data
        failure_data = df[df[failure] == 1]
        non_failure_data = df[df[failure] == 0]
        
        for setting in machine_settings:
            # Visualize the distribution of the machine setting for failure vs non-failure
            plt.figure(figsize=(8, 6))
            sns.kdeplot(failure_data[setting], label='Failure', color='red', fill=True, alpha=0.5)
            sns.kdeplot(non_failure_data[setting], label='Non-Failure', color='blue', fill=True, alpha=0.5)
            plt.title(f'{failure}: Distribution of {setting}')
            plt.xlabel(setting)
            plt.ylabel('Density')
            plt.legend()
            plt.show()
            
            # Statistical test to check for significant differences
            t_stat, p_val = ttest_ind(failure_data[setting], non_failure_data[setting], nan_policy='omit')
            t_stat_rounded = round(t_stat, 2)
            p_val_rounded = round(p_val, 4)
            failure_insights[setting] = {'t_stat': t_stat_rounded, 'p_val': p_val_rounded}
            print(f"{setting}: t-stat={t_stat_rounded}, p-value={p_val_rounded}")
        
        insights[failure] = failure_insights
    
    return insights

# Perform the analysis
failure_insights = analyze_failure_correlations(df, failure_types, machine_settings)

# Identify "Do Not Exceed" Limits for Each Setting
def identify_do_not_exceed_limits(df, failure_types, machine_settings):
    do_not_exceed_limits = {}
    max_settings = {setting: float('inf') for setting in machine_settings}
    
    for failure in failure_types:
        
        failure_limits = {}
        
        failure_data = df[df[failure] == 1]
        
        for setting in machine_settings:
            # Calculate the 95th percentile as the "Do Not Exceed" limit
            limit = round(failure_data[setting].quantile(0.95), 2)
            failure_limits[setting] = {'Do Not Exceed': limit}
            
            # Update the maximum settings (lowest 95th percentile across failures)
            if limit < max_settings[setting]:
                max_settings[setting] = limit
        
        do_not_exceed_limits[failure] = failure_limits
    
    return do_not_exceed_limits, max_settings

# Get "Do Not Exceed" limits and maximum settings
do_not_exceed_limits, max_settings = identify_do_not_exceed_limits(df, failure_types, machine_settings)

# Strategy Development
def develop_strategy(do_not_exceed_limits, max_settings):
    print("\nSuggested Strategy:\n")
    
    # Print the "Do Not Exceed" limits for each failure type
    for failure, settings in do_not_exceed_limits.items():
        print(f"For {failure}:")
        for setting, limit_info in settings.items():
            limit = limit_info['Do Not Exceed']
            print(f"  - Do not exceed {limit} for {setting}.")
        print()
    
    # Print the "Maximum Settings" for all failure types (lowest of the 95th percentiles)
    print("\nMaximum Settings To Reduce All Failure Types:\n")
    for setting, max_limit in max_settings.items():
        print(f"  - Maximum {setting}: {max_limit}")

# Propose strategies
develop_strategy(do_not_exceed_limits, max_settings)
