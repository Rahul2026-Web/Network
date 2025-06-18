import os
import sys
import numpy as np
import pandas as pd


"""
Defining common constand variable for training pipleline

"""

TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME : str ="Phising_Detection_Dataset.csv"

TRAIN_FILE_NAME: str ="train.csv"
TEST_FILE_NAME: str ="test.csv"


"""
 Data ingestion related constand start with Data_ingestion var name

"""

DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "RAHUL_YADAV"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTIED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2
# Should contain this constant definition
DATA_INGESTION_INGESTED_DIR = "data_ingestion"