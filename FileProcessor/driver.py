from processor import persist, ingest
import logging
import logging.config


class DriverProgram:
    def __init__(self, file_type):
        logging.config.fileConfig("resources/configs/logging.conf")
        logging.debug("Starting up the project")
        self.file_type = file_type

    def my(self):
        reader = ingest.FileReader(self.file_type)
        writer = persist.PersistData("postgres")
        read_json = reader.read_file()
        print(f"read the json {str(read_json)}")
        writer.store_data(read_json)


if __name__ == "__main__":
    driver = DriverProgram("json")
    driver.my()
