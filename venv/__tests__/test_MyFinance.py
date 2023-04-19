import pytest
import usrsjob

def test():
    assert usrsjob.User.show_operation.date_to_sql("") == ""


if __name__ == '__main__':
    pytest.main()