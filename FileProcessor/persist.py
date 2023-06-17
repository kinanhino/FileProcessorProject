class PersistData:

    def __init__(self, file_type):
        self.file_type = file_type

    def store_data(self):
        print(f"Saving a {self.file_type} file")
