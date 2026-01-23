import bentoml
import numpy as np
from pydantic import Field

# Load the model reference
model_ref = bentoml.models.get("iris_clf:latest")

@bentoml.service(
    name="iris_classifier",
    resources={"cpu": "1"},
)
class IrisClassifier:
    def __init__(self):
        # Load the model as a runnable
        self.model = bentoml.sklearn.load_model(model_ref)
    
    @bentoml.api
    def classify(self, input_array: np.ndarray) -> np.ndarray:
        return self.model.predict(input_array)