import ingest as FPI
import persist as FPP


class DriverProgram:
    def __init__(self, file_type):
        print("Starting up the project")
        self.file_type = file_type







file_type = "csv"
driver = DriverProgram(file_type)
reader = FPI.FileReader(file_type)
reader.read_file()
writer = FPP.PersistData(file_type)
writer.store_data()
