# we want to identify which functions to test
# => read_customers_df - 12435
# => read_orders_df - 68883
# => filter_closed_orders - 7556
# => read_app_config
import pytest
from lib.DataReader import read_customers,read_orders
from lib.DataManipulation import filter_closed_orders,count_orders_state,generic_filter_orders
from lib.ConfigReader import get_app_config

# @pytest.fixture
# def spark():
#     return get_spark_session("LOCAL")

def test_read_customers_df(spark):
    # spark = get_spark_session("LOCAL")
    customers_count = read_customers(spark,"LOCAL").count()
    assert customers_count == 12435

def test_read_orders_df(spark):
    # spark = get_spark_session("LOCAL")
    orders_count = read_orders(spark,"LOCAL").count()
    assert orders_count == 68884

@pytest.mark.transformation
def test_filter_closed_orders(spark):
    # spark = get_spark_session("LOCAL")
    orders_df = read_orders(spark,"LOCAL")
    filtered_orders = filter_closed_orders(orders_df).count()
    assert filtered_orders == 7556

@pytest.mark.skip("Work in progress")
def test_read_app_config():
    # spark = get_spark_session("LOCAL")
    config = get_app_config("LOCAL")
    assert config["orders.file.path"] == "data/orders.csv"

@pytest.mark.slow
def test_count_orders_state(spark,expected_results):
    customers_df = read_customers(spark,"LOCAL")
    actual_results = count_orders_state(customers_df)
    assert actual_results.collect() == expected_results.collect()

@pytest.mark.skip
def test_check_closed_count(spark):
    orders_df = read_orders(spark,"LOCAL")
    filtered_orders = generic_filter_orders(orders_df,"CLOSED").count()
    assert filtered_orders == 7556

@pytest.mark.skip
def test_check_pendingpayment_count(spark):
    orders_df = read_orders(spark,"LOCAL")
    filtered_orders = generic_filter_orders(orders_df,"PENDING_PAYMENT").count()
    assert filtered_orders == 15030

@pytest.mark.skip
def test_check_complete_count(spark):
    orders_df = read_orders(spark,"LOCAL")
    filtered_orders = generic_filter_orders(orders_df,"COMPLETE").count()
    assert filtered_orders == 22900

@pytest.mark.parametrize(
        "status,count",
        [("CLOSED",7556),
         ("PENDING_PAYMENT",15030),
         ("COMPLETE",22900)]
)

@pytest.mark.latest
def test_check_count(spark,status,count):
    orders_df = read_orders(spark, "LOCAL")
    filtered_orders = generic_filter_orders(orders_df,status).count()
    assert filtered_orders == count