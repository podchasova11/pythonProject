import pytest
from proka4.pytest.less_5 import connect_data_base

class TestDB:

    @pytest.mark.db
    def test_connection_is_success(self, connect_database)