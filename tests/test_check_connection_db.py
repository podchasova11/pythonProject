import pytest
from proka4.pytest.less_5 import connect_data_base

class TestDB:

    @pytest.mark.db
    @pytest.mark.usefixtures("generate_data_way_2")
    def test_login_2(self):
        print(self.login)
        print(self.password)

    @pytest.mark.db
    def test_connection_is_success(self, connect_database):
        cursor = connect_database.cursor()
        cursor.execute("SELECT * FROM employess")
        print(cursor.fetchall())
        #connect_database.close

