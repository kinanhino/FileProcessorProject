import psycopg2
import pytest

from FileProcessor.processor import persist


def test_read_from_pg():
    db_object = persist.PersistData("postgres")
    db_courses = db_object.read_from_pg("projectxschema.course_catalog")
    # print(db_courses[0][1])
    # print(len(db_courses[0]))
    assert db_courses[0][1] == "Python Spark"
    assert len(db_courses[0]) == 5

def test_read_from_pg2():
    db_object = persist.PersistData("postgres")
    with pytest.raises(psycopg2.errors.UndefinedTable):
        db_object.read_from_pg("projectxschema.invalid_table")

