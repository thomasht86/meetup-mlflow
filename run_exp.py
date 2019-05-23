import mlflow
mlflow.set_experiment("experiment1")
## Data import and cleaning
with mlflow.start_run() as run:
    # Log params
    mlflow.log_param("SEED", 42)
    mlflow.log_metric("f1", 0.8)
