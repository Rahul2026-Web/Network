from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworksecurityException
from networksecurity.logging.logger import logging  # Keep only one logging import
import sys
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()  # Added parentheses
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)  # Using correct class
        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)

    except Exception as e:
        raise NetworksecurityException(e, sys) from e