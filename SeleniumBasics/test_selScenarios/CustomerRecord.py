import pytest

@pytest.fixture
def make_customer_record():

    def _make_customer_record(name,orderId):
        return {
            "name": name,
            "orders": orderId
        }

    return _make_customer_record


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa","654")
    customer_2 = make_customer_record("Mike","741")
    customer_3 = make_customer_record("Meredith","854")
