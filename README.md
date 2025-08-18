# FastAPI Iris Classification ML Application

A machine learning application built with FastAPI that predicts Iris flower species using a trained Random Forest model.

## Project Structure

```
fastapi-ml-app/
├── app/
│   └── main.py          # FastAPI application with API endpoints
├── models/
│   ├── iris_model.py    # Model training script
│   └── iris_classifier.pkl # Trained model (generated)
├── data/
│   └── iris.csv         # Iris dataset
├── tests/
│   └── test_api.py      # API tests
├── requirements.txt     # Python dependencies
├── run_training.py      # Script to train the model
├── start_server.py      # Script to start the server
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Features

- **Machine Learning Model**: Random Forest classifier trained on Iris dataset
- **REST API**: FastAPI-based API with multiple endpoints
- **Prediction Endpoints**: Single and batch prediction capabilities
- **Model Information**: Endpoint to get model details
- **Health Checks**: Server health monitoring
- **Interactive Documentation**: Automatic API documentation with Swagger UI

## API Endpoints

- `GET /` - Root endpoint with API information
- `GET /health` - Health check endpoint
- `POST /predict` - Single prediction endpoint
- `POST /predict/batch` - Batch prediction endpoint
- `GET /model/info` - Model information endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi-ml-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model**
   ```bash
   python run_training.py
   ```

4. **Start the server**
   ```bash
   python simple_server.py
   ```
   
   Alternative methods:
   ```bash
   # Using uvicorn directly
   python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
   
   # Using start_server.py
   python start_server.py
   ```

## Usage Examples

### Single Prediction

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "sepal_length": 5.1,
       "sepal_width": 3.5,
       "petal_length": 1.4,
       "petal_width": 0.2
     }'
```

### Batch Prediction

```bash
curl -X POST "http://127.0.0.1:8000/predict/batch" \
     -H "Content-Type: application/json" \
     -d '{
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
     }'
```

## Model Performance

The Random Forest model achieves 100% accuracy on the test set, demonstrating excellent performance on the Iris classification task.

## Development

### Running Tests

```bash
pytest tests/
```

### API Documentation

Visit `http://127.0.0.1:8000/docs` when the server is running to access the interactive API documentation.

## Dependencies

- FastAPI: Modern web framework for building APIs
- scikit-learn: Machine learning library
- numpy: Numerical computing library
- uvicorn: ASGI server
- pydantic: Data validation library

## License

This project is for educational purposes as part of a class assignment.
