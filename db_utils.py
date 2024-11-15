import yaml
from sqlalchemy import create_engine
import pandas as pd

# Loads file containing database credentials
def load_credentials(file_path='credentials.yaml'):
    with open(file_path, 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials
    

# The class `RDSDatabaseConnector` initializes with credentials for connecting to an RDS database.
class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.host = credentials.get("RDS_HOST")
        self.port = credentials.get("RSD_PORT") or 5432
        self.user = credentials.get("RDS_USER")
        self.password = credentials.get("RDS_PASSWORD")
        self.database = credentials.get("RDS_DATABASE")

# Step 5: Define a method in your RDSDatabaseConnector class which initialises a SQLAlchemy engine from 
# the credentials provided to your class. This engine object together with the Pandas library will allow 
# you to extract data from the database.
    def get_connection(self):
        self.engine = create_engine(f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}")


#Step 6: Develop a method which extracts data from the RDS database and returns it as a Pandas DataFrame.
# The data is stored in a table called failure_data.
    def extract_data(self, table_name="failure_data"):
        query = f"SELECT * FROM {table_name};"
        with self.engine.connect() as connection:
            df = pd.read_sql(query, connection)
        return df

# Saves to a csv file
def save_to_csv(data, file_path="failure_data.csv"):
    data.to_csv(file_path, index=False)