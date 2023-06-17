import logging
import ingest as FPI
import persist as FPP


class DriverProgram:
    def __init__(self, file_type):
        print("Starting up the project")
        self.file_type = file_type




logging.debug("this is a debug message")
logging.info("this is an info message")
logging.warning("this is a warning message")
logging.error("this is an error message")
driver = DriverProgram("csv")
reader = FPI.FileReader("csv")
reader.read_file()
writer = FPP.PersistData("postgres")
writer.store_data()
