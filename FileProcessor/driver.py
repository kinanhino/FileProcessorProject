import logging
import ingest as FPI
import persist as FPP


class DriverProgram:
    def __init__(self, file_type):
        logging.basicConfig(level="DEBUG")
        logging.debug("Starting up the project")
        self.file_type = file_type




driver = DriverProgram("csv")
reader = FPI.FileReader("csv")
reader.read_file()
writer = FPP.PersistData("postgres")
writer.store_data()
