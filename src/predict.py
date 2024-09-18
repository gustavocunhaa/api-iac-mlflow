import yaml
import mlflow
import pandas as pd

class ModelPredict():

    def __init__(self, logged_model='runs:/847d65c741014c9cad0a4fd7c86ba72f/iris_classifier'):
        
        with open("src/config.yaml", 'r') as f:
            try:
                configs = yaml.safe_load(f)
            except yaml.YAMLError as exc:
                print(exc)

        mlflow.set_tracking_uri(configs['traking_uri'])
        
        self.loaded_model = mlflow.pyfunc.load_model(logged_model)

    def process_input(self, features):
        df = pd.DataFrame(features, index=[0])
        return df
    
    def make_predict(self, data):
        predictions = self.loaded_model.predict(data)
        return predictions[0]
    
    def evaluate(self, features):
        input_features = self.process_input(features)
        predict = self.make_predict(input_features)
        response = {
            "predict": str(predict)
        }
        return response