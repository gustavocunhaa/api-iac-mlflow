import mlflow
from sklearn.metrics import accuracy_score


class ExperimentMlflow():

    def __init__(self, uri_traking, nome_experimento):
        
        mlflow.set_tracking_uri(uri_traking)

        try:
            self.experiment_id = mlflow.create_experiment(nome_experimento)        
        except:
            self.experiment_id = mlflow.set_experiment(nome_experimento).experiment_id
        
    def train(self, pipeline, X_train, y_train):
        model = pipeline.fit(X_train, y_train)
        return model

    def metrics(self, model, X_test, y_test):
        predictions = model.predict(X_test)
        result_metrics = {
            "accuracy": accuracy_score(y_test, predictions)
        }
        return result_metrics

    def run_sklearn(self, nome_run, pipeline, X_train, X_test, y_train, y_test):

        with mlflow.start_run(experiment_id=self.experiment_id, run_name=nome_run):
            run = mlflow.active_run()
            run_id = run.info.run_id

            model_fit = self.train(pipeline, X_train, y_train)
            result_metrics = self.metrics(model_fit, X_test, y_test)

            mlflow.sklearn.log_model(model_fit, nome_run, input_example=X_test.sample(1))
            mlflow.log_metrics(result_metrics)

        return run_id