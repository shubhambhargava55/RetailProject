import pytest

from lib.Utils import get_spark_session

@pytest.fixture
def spark():
    '''
    CREATE SPARK SESSION
    '''
    spark_session = get_spark_session("LOCAL")
    yield spark_session
    print("Unit testing done, time for teardown")
    spark_session.stop()

@pytest.fixture
def expected_results(spark):
    '''
    Gives expected results
    '''
    results_schema = "state string, count int"
    return spark.read \
                .format("csv") \
                .schema(results_schema) \
                .load("data/test_results/expected_state_aggregate.csv")