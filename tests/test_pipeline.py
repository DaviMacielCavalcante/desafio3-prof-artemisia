import sys
import os
import pandas as pd
import tempfile

# Adicionar o caminho raiz ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from scripts.pipeline_etl import transform_and_save, crawler

def test_crawler_return():
    with tempfile.TemporaryDirectory() as temp_dir:
        file1 = os.path.join(temp_dir, 'file1.parquet')
        file2 = os.path.join(temp_dir, 'file2.parquet')


        open(file1, 'w').close()
        open(file2, 'w').close()

        result = crawler(temp_dir)
        expected = [file1, file2]
        assert sorted(result) == sorted(expected)


def test_etl():
    assert callable(transform_and_save)