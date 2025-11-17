#!/bin/bash
# Install dependencies
pip install -r requirements.txt
# Start FastAPI with Uvicorn
uvicorn app.main:app --host 0.0.0.0 --port $PORT
