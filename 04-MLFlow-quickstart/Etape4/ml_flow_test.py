# from mlflow.tracking import MlflowClient
# EXPERIMENT_NAME = "test_experiment"
# client = MlflowClient()
# try:
#     experiment_id = client.create_experiment(EXPERIMENT_NAME)
# except BaseException:
#     experiment_id = client.get_experiment_by_name(EXPERIMENT_NAME).experiment_id

# for model in ["linear", "Randomforest"]:
#     run = client.create_run(experiment_id)
#     client.log_metric(run.info.run_id, "rmse", 4.5)
#     client.log_param(run.info.run_id, "model", model)

import mlflow
from mlflow.tracking import MlflowClient
from memoized_property import memoized_property

EXPERIMENT_NAME = "test_experiment"

# Indicate mlflow to log to remote server
mlflow.set_tracking_uri("file:/mlruns")

client = MlflowClient()

try:
    experiment_id = client.create_experiment(EXPERIMENT_NAME)
except BaseException:
    experiment_id = client.get_experiment_by_name(EXPERIMENT_NAME).experiment_id

yourname = 'Anas'

if yourname is None:
    print("please define your name, il will be used as a parameter to log")

for model in ["linear", "Randomforest"]:
    run = client.create_run(experiment_id)
    client.log_metric(run.info.run_id, "rmse", 4.5)
    client.log_param(run.info.run_id, "model", model)
    client.log_param(run.info.run_id, "student_name", yourname)



# class Trainer():
    

#     @memoized_property
#     def mlflow_client(self):
#         mlflow.set_tracking_uri(MLFLOW_URI)
#         return MlflowClient()

#     @memoized_property
#     def mlflow_experiment_id(self):
#         try:
#             return self.mlflow_client.create_experiment(self.experiment_name)
#         except BaseException:
#             return self.mlflow_client.get_experiment_by_name(self.experiment_name).experiment_id

#     @memoized_property
#     def mlflow_run(self):
#         return self.mlflow_client.create_run(self.mlflow_experiment_id)

#     def mlflow_log_param(self, key, value):
#         self.mlflow_client.log_param(self.mlflow_run.info.run_id, key, value)

#     def mlflow_log_metric(self, key, value):
#         self.mlflow_client.log_metric(self.mlflow_run.info.run_id, key, value)