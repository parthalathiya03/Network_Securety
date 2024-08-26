import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.components.data_ingestion import DataIngestion


from networksecurity.entity.config_entity import(
    TrainingPipelineConfig,
    DataIngestionConfig,
)

from networksecurity.entity.artifact_entity import (
    DataIngestionArtifact,
)


class TrainingPipeline:
    def __init__(self):
         self.training_pipeline_config = TrainingPipelineConfig()
    
    def start_data_ingestion(self):
        try:
            self.data_ingestion_config=DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data ingestion")
            
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
    
            return data_ingestion_artifact        
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            print(data_ingestion_artifact)
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)    