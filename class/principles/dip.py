from abc import ABC, abstractmethod
class MySQLDatabase:
    def connect(self):
        print("Connected to MySQL database")

class DataService:
    def __init__(self):
        self.database = MySQLDatabase()
    
    def fetch_data(self):
        self.database.connect()
        print("Fetched data from MySQL database")

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL database")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connected to PostgreSQL database")

class DataService:
    def __init__(self, database: Database):
        self.database = database
    
    def fetch_data(self):
        self.database.connect()
        print("Fetched data from database")

data_service = DataService(MySQLDatabase())
data_service.fetch_data()

data_service1 = DataService(PostgreSQLDatabase())
data_service1.fetch_data()