import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert "status" in response.json()

def test_predict_endpoint():
    test_data = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=test_data)
    assert response.status_code == 200 or response.status_code == 503
    
    if response.status_code == 200:
        result = response.json()
        assert "species" in result
        assert "confidence" in result

def test_model_info():
    response = client.get("/model/info")
    assert response.status_code == 200 or response.status_code == 503

def test_batch_prediction():
    test_data = {
        "features": [
            {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2
            },
            {
                "sepal_length": 6.2,
                "sepal_width": 2.9,
                "petal_length": 4.3,
                "petal_width": 1.3
            }
        ]
    }
    response = client.post("/predict/batch", json=test_data)
    assert response.status_code == 200 or response.status_code == 503
