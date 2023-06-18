import logging
class FileReader:

    def __init__(self, file_type):
        logging.config.fileConfig("resources/configs/logging.conf")
        self.logger = logging.getLogger("Ingest")
        self.file_type = file_type

    def read_file(self):
        self.logger.debug(f"Reading a {self.file_type} file")
