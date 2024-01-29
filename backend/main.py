import uvicorn
import joblib
import pandas as pd
from fastapi import FastAPI, UploadFile, File
from schemas import InferencePayload
from utils.columns_definitions import *
from io import BytesIO


app = FastAPI()
model = joblib.load('xgb_best.pkl')

@app.get('/')
@app.get('/home')
def index():
    return {'msg': 'System is up and running.'}


@app.post('/inference')
def inference(payload: InferencePayload):
    data_dict = payload.model_dump()
    data_df = pd.DataFrame.from_dict([data_dict])
    data_df.rename(columns={"Credit_Builder_Loan": "Credit-Builder_Loan"}, inplace=True)
    pred = model.predict(data_df).item()

    return {'inference': pred}


@app.post('/inference/file')
def inference(csv_file: UploadFile = File(...)):
    content = csv_file.file.read()
    data = BytesIO(content)
    df = pd.read_csv(data)
    pred = model.predict(df)
    
    return {
        "predictions": pred.tolist()
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)