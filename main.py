import os
from scripts import pipeline_etl

def process_new_file(dir):
    files = os.listdir(dir)
    for file in files:
        if file.endswith('.parquet'):
            pipeline_etl.transform_and_save("./datalake/raw", "./datalake/silver")


if __name__ == "__main__":
    directory_to_watch = "./datalake/raw/"
    process_new_file(directory_to_watch)