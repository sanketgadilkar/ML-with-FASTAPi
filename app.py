from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import predict,model,model_version
from schema.user_input import UserInput
from schema.response import PredictionResponse

app = FastAPI()

@app.get("/")
def hello():
    return ('helo sanket')

@app.get('/health')
def health():
    return {
        'status : ok'
        'model_version': model_version,
        'model_loaded': model is not None
    }

@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data: UserInput):

    input_df = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:    
        prediction = predict(input_df)

        return JSONResponse(status_code=200, content={'response': prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))