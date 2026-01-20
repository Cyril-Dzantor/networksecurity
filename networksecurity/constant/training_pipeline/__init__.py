from datetime import datetime
import numpy as np 
import pandas as pd
import sys


"""
Define common constant variables for the training pipeline

"""

TARGET_COLUMN = "Results"
PIPELINE_NAME : str = "NetworkSecurity"
ARTIFACT_DIR : str = "Artifacts"
FILE_NAME : str = "phisingData.csv"

TRAIN_FILE_NAME : str = "train.csv"
TEST_FILE_NAME : str = "test.csv"


"""
Data ingestion related constant start with var name DATA_INGESTION_VAR_NAME

"""
DATA_INGESTION_COLLECTION_NAME : str = "NetworkData" 
DATA_INGESTION_DATABASE_NAME   : str = "Cyril"
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR : str = "feature_store"
DATA_INGESTION_INGESTED_DIR : str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO : float = 0.2 

