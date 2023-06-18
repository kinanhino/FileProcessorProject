import configparser
import logging
import psycopg2


class PersistData:

    def __init__(self, db_type):
        logging.config.fileConfig("resources/configs/logging.conf")
        self.logger = logging.getLogger("Persist")
        self.config = configparser.ConfigParser()
        self.config.read('resources/fileprocessor.ini')

        self.db_type = db_type

    def store_data(self):
        try:
            target_table = self.config.get("DATABASE_CONFIGS", "PG_TABLE")
            self.logger.debug(f"target table name is {target_table}")
            self.logger.debug(f"Storing data to {self.db_type}")

        except Exception as ex:
            self.logger.error(f"An error has occured. {str(ex)}")

    def read_from_pg(self):
        connection = psycopg2.connect(user='postgres',
                                      password='12332100',
                                      host='localhost',
                                      database='postgres')
        cursor = connection.cursor()
