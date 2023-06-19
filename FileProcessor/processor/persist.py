import configparser
import logging
import psycopg2
import json

class PersistData:

    def __init__(self, db_type):
        logging.config.fileConfig("resources/configs/logging.conf")
        self.logger = logging.getLogger("Persist")
        self.config = configparser.ConfigParser()
        self.config.read('resources/fileprocessor.ini')
        self.db_type = db_type


    def connect(self):
        connection = psycopg2.connect(user='postgres',
                                      password='12332100',
                                      host='localhost',
                                      database='postgres')
        return connection
    
    def get_max_id(self, cursor, target_table):
        cursor.execute(f"SELECT max(course_id) FROM {target_table}")
        return cursor.fetchone()[0]
    
    def store_data(self, course_json):
        try:
            target_table = self.config.get("DATABASE_CONFIGS", "PG_TABLE")
            self.logger.debug(f"target table name is {target_table}")
            self.logger.debug(f"Storing data to {self.db_type}")
            # self.write_to_pg(target_table)
            # self.read_from_pg(target_table)
            self.write_from_json_to_pg(target_table,course_json=course_json)

        except Exception as ex:
            self.logger.error(f"An error has occured. {str(ex)}")

    def write_from_json_to_pg(self, target_table, course_json):
        connection = self.connect()
        cursor = connection.cursor()
        max_course_id = self.get_max_id(cursor, target_table)
        insert_query = f"INSERT INTO {target_table}" \
                       "(course_id, course_name, author_name, course_section, creation_date)" \
                       "VALUES (%s, %s, %s, %s, %s)"
        
        insert_tuple = (max_course_id+1,
                        course_json["course_name"],
                        course_json["author_name"],
                        json.dumps(course_json["course_section"]),
                        course_json["creation_date"])

        cursor.execute(insert_query, insert_tuple)

        cursor.close()

        connection.commit()
    def write_to_pg(self, target_table):
        connection = self.connect()
        cursor = connection.cursor()
        max_course_id = self.get_max_id(cursor,target_table)
        
        insert_query = f"INSERT INTO {target_table}" \
                       "(course_id, course_name, author_name, course_section, creation_date)" \
                       "VALUES (%s, %s, %s, %s, %s)"
        insert_tuple = (max_course_id+1, 'Javascript', 'Kinan Hino', '{"section": 6, "title": "Fullstack"}', '2023-05-13')
        
        cursor.execute(insert_query, insert_tuple)

        cursor.close()

        connection.commit()

    def read_from_pg(self, target_table):
        connection = self.connect()
        cursor = connection.cursor()
        select_query = f"SELECT * FROM {target_table}"
        cursor.execute(select_query)
        # print(cursor.fetchone())
        records = cursor.fetchall()
        for item in records:
            print(item)
            print("Printed a record")

        cursor.close()

        connection.commit()

