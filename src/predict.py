import os
from pathlib import Path
import pickle
import pandas as pd

class ModelPredict():

    def __init__(self):
        
        MODEL_PATH = Path(f"{os.getcwd()}/src/model/model.pkl")
        with open(MODEL_PATH, "rb") as input_file:
            self.loaded_model = pickle.load(input_file)

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