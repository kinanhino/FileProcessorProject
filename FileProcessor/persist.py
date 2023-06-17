class PersistData:

    def __init__(self, db_type):
        self.db_type = db_type

    def store_data(self):
        print(f"Storing data to {self.db_type}")
