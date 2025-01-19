import pandas as pd

class DataTransformer:
    def __init__(self, rename_map=None):
        self.dtype_map = {
        
        'UDI': 'int64',
        'Product ID': 'object',
        'Type': 'category',
        'Air temperature [K]': 'float64',
        'Process temperature [K]': 'float64',
        'Rotational speed [rpm]': 'int64',
        'Torque [Nm]': 'float64',
        'Tool wear [min]': 'float64',
        'Machine failure': 'bool',
        'TWF': 'bool',
        'HDF': 'bool',
        'PWF': 'bool',
        'OSF': 'bool',
        'RNF': 'bool'
        }
        
        
        self.rename_map = rename_map if rename_map else {
            'TWF': 'Tool wear failure',           
            'HDF': 'Head dissipation failure',
            'PWF': 'Power failure',     
            'OSF': 'Overstrain failure',  
            'RNF': 'Random failure'
        }

    def change_data_types(self, df):
        """
        The function `change_data_types` converts the data types of columns in a DataFrame according to
        a specified mapping and optionally renames columns.
        
        :param df: The `df` parameter in the `change_data_types` method is a DataFrame that contains the
        data to be processed. The method iterates over the columns of this DataFrame and changes their
        data types based on the specified `dtype_map`. Additionally, it renames the columns based on the
        `rename_map
        :return: the DataFrame `df` after changing the data types of columns based on the `dtype_map`
        and renaming columns if `rename_map` is provided.
        """
       
        
        for column, dtype in self.dtype_map.items():
            if column in df.columns:
                df[column] = df[column].astype(dtype)
                
        if self.rename_map:
            df = df.rename(columns=self.rename_map)
       
        return df            
    
    def transform_and_save(self, input_file, output_file):
        """
        The function reads a CSV file, transforms the data types, and saves the result to another CSV
        file.
        
        :param input_file: The `input_file` parameter in the `transform_and_save` function is the file
        path to the CSV file that you want to read and transform. This file should contain the data that
        you want to process and save in a different format or structure
        :param output_file: The `output_file` parameter in the `transform_and_save` function is the file
        path where the transformed data will be saved after processing. This parameter specifies the
        location and name of the output file where the transformed data will be written to in CSV format
        """
       
        df = pd.read_csv(input_file)
        df = self.change_data_types(df)

        df.to_csv(output_file, index=False)

if __name__ == '__main__':
    # Specify input and output file paths
    input_file = r'C:\Users\BoStewart-Woods\OneDrive - Climar Industries Ltd/Documents - Data\Server\My Docs\Bo SW/AI Core (Home)\Exploratory_Data_Analysis_The_Manufacturing_Process\failure_data.csv'  
    output_file = r'C:\Users\BoStewart-Woods\OneDrive - Climar Industries Ltd/Documents - Data\Server\My Docs\Bo SW/AI Core (Home)\Exploratory_Data_Analysis_The_Manufacturing_Process\Transformed_failure_data.csv'  

    # Create an instance of the DataTransformer class
    transformer = DataTransformer()

    # Perform the transformation and save the result
    transformer.transform_and_save(input_file, output_file)
