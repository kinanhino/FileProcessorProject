class FileReader:

    def __init__(self, file_type):
        self.file_type = file_type

    def read_file(self):
        print(f"Reading a {self.file_type} file")
