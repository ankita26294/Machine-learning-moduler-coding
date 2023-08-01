import os,sys
from datetime import datetime

#artifact -> pipeline folder ->timestamp -> output


def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"


CURRENT_TIME_STAMP = get_current_time_stamp()


ROOT_DIR_KEY = os.getcwd()
DATA_DIR="Data"
DATA_DIR_KEY ="finalTrain.csv"

# machine-learning/DATA_DIR/DATA_DIR_KEY

ARTIFACT_DIR_KEY = "Artifact"

# Data ingestion realated variable(creating a folder data ingestion.in data ingestion create 2 folder raw_data_dir->raw.csv and ingested_dir->train.csv and test.csv)
DATA_INGESTION_KEY = "data_ingestion"
DATA_INGESTION_RAW_DATA_DIR =" raw_data_dir"
DATA_INGESTION_INGESTED_DATA_DIR_KEY ="ingested_dir"
RAW_DATA_DIR_KEY ="raw.csv"
TRAIN_DATA_DIR_KEY ="train.csv"
TEST_DATA_DIR_KEY="test.csv"


# Data Transformation related variable

DATA_TRANSFORMATION_ARTIFACT = "data_transformation"
DATA_PREPROCCED_DIR = "procceor"
DATA_TRANSFORMTION_PROCESSING_OBJ = "processor.pkl"
DATA_TRANSFORM_DIR = "transformation"
TRANSFORM_TRAIN_DIR_KEY = "train.csv"
TRANSFORM_TEST_DIR_KEY = "test.csv"
#os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_TRANSFORMATION_ARTIFACT,
       #                                  DATA_TRANSFORM_DIR)

#
# artifact / data_transformation / procceor->processor.pkl abnd transformation -> train.csv and test.csv

