from pyspark.sql import SparkSession

def parquet_generator():
    spark = SparkSession.builder.appName("CSV to Parquet").getOrCreate()
    df = spark.read.csv("./dataset/agricultural_production_animas_products_2024.csv", header=True, inferSchema=True)

    df = df.drop(*["ASD_CODE", "ASD_DESC", "COUNTY_ANSI", "COUNTY_CODE", "COUNTY_NAME", "REGION_DESC", "ZIP_5", "WATERSHED_CODE", "WATERSHED_DESC", "CONGR_DISTRICT_CODE", "COUNTRY_CODE", "COUNTRY_NAME", "BEGIN_CODE", "END_CODE", "REFERENCE_PERIOD_DESC", "WEEK_ENDING", "LOAD_TIME", "VALUE", "CV_%"])

    df = df.drop("SECTOR_DESC")

    df_annual = df.filter((df["FREQ_DESC"] == "ANNUAL") & (df["AGG_LEVEL_DESC"] == "STATE"))

    df_annual = df_annual.drop(*["AGG_LEVEL_DESC", "FREQ_DESC", "STATE_ANSI", "STATE_FIPS_CODE", "LOCATION_DESC"])

    df_annual_2000_2024 = df_annual.filter((df_annual["YEAR"] >= 2000) & (df_annual["YEAR"] <= 2024))


    df_annual_2000_2024 = df_annual_2000_2024.drop(*["SHORT_DESC","DOMAINCAT_DESC","DOMAIN_DESC", "CLASS_DESC", "UTIL_PRACTICE_DESC"])

    df_annual_2000_2024 = df_annual_2000_2024.sort("YEAR")

    df_annual_2000_2024.write.mode("overwrite").partitionBy("YEAR").parquet("./datalake/raw")