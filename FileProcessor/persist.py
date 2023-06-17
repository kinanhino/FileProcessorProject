import logging

class PersistData:

    def __init__(self, db_type):
        logging.basicConfig(level="DEBUG")
        self.db_type = db_type

    def store_data(self):
        logging.debug(f"Storing data to {self.db_type}")
