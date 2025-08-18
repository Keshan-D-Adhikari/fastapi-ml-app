#!/usr/bin/env python3
"""
Script to train the Iris classification model
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.iris_model import train_model

if __name__ == "__main__":
    print("Starting model training...")
    model, accuracy = train_model()
    print(f"Training completed! Model accuracy: {accuracy:.4f}")
    print("Model saved to models/iris_classifier.pkl")
