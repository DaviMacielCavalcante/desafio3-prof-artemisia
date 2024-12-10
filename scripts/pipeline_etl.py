import pandas as pd
import os

def crawler(directory):
    parquets = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.parquet'):
                parquets.append(os.path.join(root, file))

    return parquets

def transform_and_save(dir_input, dir_output):
    parquets = crawler(dir_input)

    for p in parquets:
        pq = pd.read_parquet(p)
        pq["STATISTICCAT_DESC"] = pq["STATISTICCAT_DESC"].replace(
        r"(?<=[a-zA-Z])\s*,\s*(?=[a-zA-Z])", "_", regex=True)
        pq["UNIT_DESC"] = pq["UNIT_DESC"].replace(
        r"\s*/\s*", "_", regex=True)

        relative_path = os.path.relpath(p, dir_input)

        output_path = os.path.join(dir_output, relative_path)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        pq.to_parquet(output_path)
        


transform_and_save("./datalake/raw", "./datalake/silver")
