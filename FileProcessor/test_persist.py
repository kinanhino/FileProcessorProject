import unittest

import psycopg2

from processor import persist




class PersistDataTest(unittest.TestCase):
    def test_read_from_pg(self):
        db_object = persist.PersistData("postgres")
        db_courses = db_object.read_from_pg("projectxschema.course_catalog")
        # print(db_courses[0][1])
        # print(len(db_courses[0]))
        self.assertEqual(db_courses[0][1], "Python Spark")
        self.assertEqual(len(db_courses[0]), 5)

    def test_read_from_pg2(self):
        db_object = persist.PersistData("postgres")
        with self.assertRaises(psycopg2.errors.UndefinedTable):
            db_object.read_from_pg("projectxschema.invalid_table")


if __name__ == '__main__':
    unittest.main()
