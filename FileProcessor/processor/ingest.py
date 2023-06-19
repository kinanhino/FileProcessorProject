import logging
import json

class FileReader:

    def __init__(self, file_type):
        logging.config.fileConfig("resources/configs/logging.conf")
        self.logger = logging.getLogger("Ingest")
        self.file_type = file_type

    def read_file(self):
        self.logger.debug(f"Reading a {self.file_type} file")
        with open('course.json') as f:
            new_course = json.load(f)
        print(f"new course is {str(new_course)}")
        return new_course
