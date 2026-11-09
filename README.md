# Network Security System

A machine learning-based network security project for detecting malicious or phishing URLs using URL structure and website characteristics. The project combines a Python ML training pipeline with a FastAPI service for training and prediction workflows.

## Overview

This system uses a phishing URL dataset with features such as:

- IP address presence
- URL length
- presence of shortening services
- special characters like `@` and `//`
- domain registration age
- HTTPS usage
- anchor and tag-based URL properties
- page rank and index information

The target label is `Result`, where the model predicts whether a URL is benign or malicious.

## Features

- End-to-end ML training pipeline
- Data ingestion from MongoDB
- Data validation and schema checking
- Data transformation and preprocessing
- Model comparison and training using multiple classifiers
- MLflow experiment tracking
- Saved model export for prediction
- REST API for model training and prediction
- CSV-based inference endpoint

## Project Structure

```text
Network Security/
├── app.py                     # FastAPI service entry point
├── main.py                    # Training pipeline runner
├── requirements.txt           # Python dependencies
├── setup.py                   # Package configuration
├── data_schema/
│   └── schema.yaml            # Dataset schema and expected columns
├── networksecurity/           # Core ML package
│   ├── cloud/
│   ├── components/
│   ├── constants/
│   ├── entity/
│   ├── exception/
│   ├── logging/
│   ├── pipeline/
│   └── utils/
├── templates/
│   └── table.html             # HTML template for prediction output
├── final_model/               # Final trained model files
├── saved_models/               # Training artifacts and model objects
├── prediction_output/         # Prediction CSV output
├── valid_data/                 # Validated datasets
├── notebooks/                  # Optional notebooks / experiments
├── logs/                      # Application logs
├── Network_Data/               # Data source or local dataset folder
├── .env                       # Local environment variables (not tracked in some setups)
└── README.md
```

## Tech Stack

- Python 3.x
- FastAPI
- Uvicorn
- Pandas / NumPy
- Scikit-learn
- MongoDB
- MLflow
- Dagshub
- Docker (included via Dockerfile)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mananpanwar600-gif/Network-Security-System.git
cd "Network Security"
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables:

Create a `.env` file in the project root and set your MongoDB connection string:

```env
MONGODB_URL_KEY=mongodb+srv://<username>:<password>@<cluster-url>
```

## Running the Project

### Train the model

Run the training pipeline:

```bash
python main.py
```

This performs:

- data ingestion
- validation
- transformation
- model training
- artifact generation

### Start the API

```bash
python app.py
```

The API will start on:

```text
http://0.0.0.0:8080
```

Open the docs at:

```text
http://localhost:8080/docs
```

## API Endpoints

### GET `/`

Redirects to the Swagger UI documentation.

### GET `/train`

Starts the training pipeline and returns a success message when training completes.

### POST `/predict`

Uploads a CSV file containing URL feature columns and returns a prediction table with a new `predicted_column`.

Example request:

- Method: `POST`
- URL: `/predict`
- Form field: `file`

The uploaded CSV needs to match the dataset schema defined in `data_schema/schema.yaml`.

## Model Behavior

The project evaluates several classifiers, including:

- Random Forest
- Decision Tree
- Gradient Boosting
- Logistic Regression
- AdaBoost

The best-performing model is selected and saved as the final trained model for inference.

## Output Files

- `final_model/model.pkl` - final trained model
- `final_model/preprocessor.pkl` - preprocessing object
- `prediction_output/output.csv` - prediction results
- `saved_models/` - model artifacts and training outputs
- `Artifacts/` - pipeline artifacts (generated during training)

## Notes

- The project is designed for URL-based phishing detection and network security analysis.
- MongoDB connectivity is required for the ingestion stage.
- The API expects a CSV file matching the schema used by the training pipeline.
- MLflow and Dagshub are used for experiment tracking and model logging.

## License

This project is provided as-is for educational and experimental use.

## Author

Manan Singh Panwar
