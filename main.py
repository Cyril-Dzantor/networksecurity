from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.data_ingestion import DataIngestion

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact
import sys 

if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)
        dataingestion = DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info("Initiate Data Ingestion")
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
