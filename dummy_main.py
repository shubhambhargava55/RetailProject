from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("TestApp") \
    .getOrCreate()

spark.range(1, 5).show()