# Import the SparkSession library 
from pyspark.sql import SparkSession 
  
# Create a spark session using getOrCreate() function 
spark_session = SparkSession.builder.getOrCreate() 
  
# Read the CSV file 
data_frame=csv_file = spark_session.read.csv('content/student_data.csv', 
                           sep = ',', inferSchema = True, header = True) 
  
# Extract random sample through sample  
# function using only fraction as argument  
print(data_frame.sample(0.4).collect()) 
  
# Again extract random sample through sample function using only  
# fraction as argument to check if we get same output each time 
print(data_frame.sample(0.4).collect())

i=input()
