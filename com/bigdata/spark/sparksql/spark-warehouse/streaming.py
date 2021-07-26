from pyspark.sql import *
from pyspark.sql import functions as F
from pyspark.streaming import *

spark = SparkSession.builder.master("local").appName("testing").getOrCreate()
sc = spark.sparkContext
ssc = StreamingContext(sc, 10)
lines = ssc.socketTextStream("ubuntu@ec2-52-66-253-213.ap-south-1.compute.amazonaws.com", int(9876))

lines.pprint()
ssc.start()             # Start the computation
ssc.awaitTermination()