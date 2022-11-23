from unittest.mock import MagicMock, Mock
from unittest import TestCase
from unittest.mock import patch
import pymysql
class Test_Class(TestCase):
    
    def test_sql_cursor(self):
        with patch('pymysql.connect') as mock_connect:  
            cursor = MagicMock()
            cursor.execute.return_value = ["hello world"]
            mock_connect.return_value.cursor.return_value.__enter__.return_value = cursor
            conn = pymysql.connect()
            actual = self.execute_this(conn)
            print(actual)
            assert actual ==  ["hello world"]
            print("Test passed")
            
    def execute_this(self,connection):  
        with connection.cursor() as cur: 
            return cur.execute('')
​
testing = Test_Class()
testing.test_sql_cursor()