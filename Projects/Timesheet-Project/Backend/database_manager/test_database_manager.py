# imports
import unittest
from unittest.mock import MagicMock
from manager import Manager


class TestManager(unittest.TestCase):
    def setUp(self):
        # Set up a mock connection to the database for testing purposes
        self.mock_con = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_con.cursor.return_value = self.mock_cursor
        print(self.mock_con.cursor())  # Debug statement
        self.database = Manager(server_name='DESKTOP-OP7DVNI',
                                database_name='ChronoSync',
                                database_user='api',
                                database_userpass='Qwerty1!')
        self.database.con = self.mock_con

    def test_connect(self):
        # Test connecting to the database
        self.database.connect()
        self.assertIsNotNone(self.database.con)
        self.assertIsNotNone(self.database.cursor)

    def test_create_table(self):
        # Test creating a new table
        self.database.query = MagicMock()
        self.database.query.return_value = []
        self.database.query("USE ChronoSync; CREATE TABLE test_table (id INT PRIMARY KEY, name VARCHAR(50))")
        self.database.query.assert_called_with("USE ChronoSync; CREATE TABLE test_table (id INT PRIMARY KEY, "
                                               "name VARCHAR(50))")

    def test_update_table(self):
        # Test updating an existing table
        self.database.query = MagicMock()
        self.database.query.return_value = []
        self.database.query("USE ChronoSync; UPDATE test_table SET name = 'John' WHERE id = 1")
        self.database.query.assert_called_with("USE ChronoSync; UPDATE test_table SET name = 'John' WHERE id = 1")

    def test_insert_into_table(self):
        # Test inserting a new row into a table
        self.database.query = MagicMock()
        self.database.query.return_value = []
        self.database.query("USE ChronoSync; INSERT INTO test_table (id, name) VALUES (1, 'John')")
        self.database.query.assert_called_with("USE ChronoSync; INSERT INTO test_table (id, name) VALUES (1, 'John')")

    def test_delete_from_table(self):
        # Test deleting a row from a table
        self.database.query = MagicMock()
        self.database.query.return_value = []
        self.database.query("USE ChronoSync; DELETE FROM test_table WHERE id = 1")
        self.database.query.assert_called_with("USE ChronoSync; DELETE FROM test_table WHERE id = 1")

    def test_alter_table(self):
        # Test altering an existing table
        self.database.query = MagicMock()
        self.database.query.return_value = []
        self.database.query("USE ChronoSync; ALTER TABLE test_table ADD age INT")
        self.database.query.assert_called_with("USE ChronoSync; ALTER TABLE test_table ADD age INT")

    def test_truncate_table(self):
        # Test truncating a table
        self.database.query = MagicMock()
        self.database.query.return_value = []
        self.database.query("USE ChronoSync; TRUNCATE TABLE test_table")
        self.database.query.assert_called_with("USE ChronoSync; TRUNCATE TABLE test_table")

    def test_drop_table(self):
        # Test dropping a table
        self.database.query = MagicMock()
        self.database.query.return_value = []
        self.database.query("USE ChronoSync; DROP TABLE test_table")
        self.database.query.assert_called_with("USE ChronoSync; DROP TABLE test_table")

    def tearDown(self):
        self.database.close()


if __name__ == '__main__':
    unittest.main()
