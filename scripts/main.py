from pyspark.sql.dataframe import DataFrame


def create_spark_session(app_name: str) -> SparkSession:
    """ Create a spark session.
    """
    ss = SparkSession.builder.master('local').appName(app_name).getOrCreate()
    return ss


def read_in_data(sc: SparkSession, file: str):
    """ Return a spark DataFrame of the csv file <file>.
    """
    return sc.read.csv(file, header='true', sep=',', inferSchema=False)


if __name__ == '__main__':

    # create a spark session
    spark = create_spark_session("average salary")

    #### EXTRACT ####

    # read in the weather.csv as a spark DataFrame
    weather_df = read_in_data(spark, 's3://  .csv')


