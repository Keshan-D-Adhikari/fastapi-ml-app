from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
import os
from typing import List

# Initialize FastAPI app
app = FastAPI(title="Iris Species Prediction API", version="1.0.0")

# Load the trained model
model_path = "models/iris_classifier.pkl"
if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
else:
    model = None

# Pydantic models for request/response
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class PredictionResponse(BaseModel):
    species: str
    confidence: float

class BatchPredictionRequest(BaseModel):
    features: List[IrisFeatures]

@app.get("/")
async def root():
    return {"message": "Iris Species Prediction API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model_loaded": model is not None}

@app.post("/predict", response_model=PredictionResponse)
async def predict_species(features: IrisFeatures):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    # Prepare input data
    input_data = np.array([[features.sepal_length, features.sepal_width, 
                           features.petal_length, features.petal_width]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    confidence = model.predict_proba(input_data).max()
    
    return PredictionResponse(species=prediction, confidence=float(confidence))

@app.post("/predict/batch")
async def predict_batch(request: BatchPredictionRequest):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    predictions = []
    for features in request.features:
        input_data = np.array([[features.sepal_length, features.sepal_width, 
                               features.petal_length, features.petal_width]])
        prediction = model.predict(input_data)[0]
        confidence = model.predict_proba(input_data).max()
        predictions.append({
            "species": prediction,
            "confidence": float(confidence)
        })
    
    return {"predictions": predictions}

@app.get("/model/info")
async def model_info():
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    return {
        "model_type": "RandomForestClassifier",
        "features": ["sepal_length", "sepal_width", "petal_length", "petal_width"],
        "classes": list(model.classes_) if hasattr(model, 'classes_') else []
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
