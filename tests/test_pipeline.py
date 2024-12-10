import sys
import os

# Adicionar o caminho raiz ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from scripts.pipeline_etl import transform_and_save

def test_etl():
    assert callable(transform_and_save)