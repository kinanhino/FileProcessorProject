from processor import persist, ingest
import logging
import logging.config
from flask import Flask, request

app = Flask(__name__)
@app.route('/courses', methods=['GET'])
def get_courses():
    db_object = persist.PersistData("postgres")
    db_courses = db_object.read_from_pg("projectxschema.course_catalog")
    return "courses are " + str(db_courses)

@app.route('/course', methods=['POST'])
def store_course():
    input_json = request.get_json(force=True)
    print(str(input_json))
    db_object = persist.PersistData("postgres")
    db_courses = db_object.write_from_json_to_pg("projectxschema.course_catalog",input_json)
    return "success"

class DriverProgram:
    def __init__(self, file_type):
        logging.config.fileConfig("resources/configs/logging.conf")
        logging.debug("Starting up the project")
        self.file_type = file_type

    def my(self):
        reader = ingest.FileReader(self.file_type)
        writer = persist.PersistData("postgres")
        read_json = reader.read_file()
        logging.debug(f"read the json {str(read_json)}")
        writer.store_data(read_json)


if __name__ == "__main__":
    app.run(debug=True, port=8005)
    # driver = DriverProgram("json")
    # driver.my()
