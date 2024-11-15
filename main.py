from db_utils import load_credentials, RDSDatabaseConnector, save_to_csv

# The line `if __name__=="__main__":` in Python is a common idiom used to check whether the Python
# script is being run directly by the interpreter.
if __name__=="__main__":
    
    # `loaded_credentials = load_credentials()` is a line of code that calls the `load_credentials()`
    # function to retrieve and load the credentials needed for connecting to a database. The function fetch the necessary
    # credentials like database host, username, password, and other connection details. These
    # credentials are then stored in the variable `loaded_credentials` for later use in establishing a
    # connection to the database.
    loaded_credentials = load_credentials()
    
    # The code `connector = RDSDatabaseConnector(loaded_credentials)` is creating an instance of the
    # `RDSDatabaseConnector` class with the loaded credentials passed as an argument. This instance is
    # stored in the variable `connector`.
    connector = RDSDatabaseConnector(loaded_credentials)
    connector.get_connection()

   # The code `df = connector.extract_data()` is extracting data from the database using the
   # RDSDatabaseConnector object `connector` and storing it in a DataFrame object `df`.
    df = connector.extract_data()
    save_to_csv(df)