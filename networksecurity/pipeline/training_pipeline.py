import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation


from networksecurity.entity.config_entity import(
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig
)

from networksecurity.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifacts
)


class TrainingPipeline:
    def __init__(self):
         self.training_pipeline_config = TrainingPipelineConfig()
    
    def start_data_ingestion(self):
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data ingestion")
            
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
    
            return data_ingestion_artifact        
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_data_validation(self,data_ingestion_artifacts = DataIngestionArtifact):
        try:
            self.data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting Data Validation")
            
            data_validation = DataValidation(data_ingestion_artifacts = data_ingestion_artifacts,data_validation_config = data_validation_config)
            data_validation_artifacts = data_validation.initiate_data_validation()
            logging.info(f"Data Validation completed and artifact: {data_validation_artifacts}")
            
            return data_validation_artifacts
            
        except Exception as e:
            print(e)
            raise NetworkSecurityException(e,sys)
    
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
     
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)   
        
    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)     
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()  # here we get artifacts as an output
            print(data_ingestion_artifact)
            
            data_validation_artifacts = self.start_data_validation()
            print(data_validation_artifact)
        except Exception as e:
            raise NetworkSecurityException(e,sys)    