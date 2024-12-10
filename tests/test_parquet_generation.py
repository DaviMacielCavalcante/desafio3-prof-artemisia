import sys
import os

# Adicionar o caminho raiz ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from scripts.parquet_generation import parquet_generator

def test_parquet_generation():
    assert callable(parquet_generator)