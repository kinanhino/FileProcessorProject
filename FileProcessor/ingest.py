import logging
class FileReader:

    def __init__(self, file_type):
        logging.basicConfig(level="DEBUG")
        self.file_type = file_type

    def read_file(self):
        logging.debug(f"Reading a {self.file_type} file")
