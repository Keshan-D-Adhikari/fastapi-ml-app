# How to Run the FastAPI ML Application

## Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Train the Model (if not already done)
```bash
python run_training.py
```

### Step 3: Start the Server
```bash
python simple_server.py
```

## Alternative Server Start Methods

### Option A: Using uvicorn directly
```bash
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

### Option B: Using the simple server script
```bash
python simple_server.py
```

### Option C: Using the start server script
```bash
python start_server.py
```

## Access Your API

Once running, visit these URLs:

- **Main API**: http://127.0.0.1:8000
- **Interactive Docs**: http://127.0.0.1:8000/docs
- **Health Check**: http://127.0.0.1:8000/health

## Test the API

### Using the Interactive Docs (Recommended)
1. Go to http://127.0.0.1:8000/docs
2. Click "Try it out" on the `/predict` endpoint
3. Enter sample data:
   ```json
   {
     "sepal_length": 5.1,
     "sepal_width": 3.5,
     "petal_length": 1.4,
     "petal_width": 0.2
   }
   ```

### Using curl
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

## Troubleshooting

### If you get import errors:
```bash
pip install fastapi uvicorn scikit-learn numpy
```

### If port 8000 is busy, use different port:
```bash
python -m uvicorn app.main:app --host 127.0.0.1 --port 8080
```

### To stop the server:
Press `Ctrl+C` in the terminal

## Project Status Check

Run these commands to verify everything is working:

```bash
# Check if model exists
ls models/iris_classifier.pkl

# Test model training
python run_training.py

# Check server startup
python simple_server.py
```
