# Credit Classification project 💰🤑💸💳

### Dataset

The data is included in the `data` directory within this repo and it has been downloaded from @[Kaggle](https://www.kaggle.com/datasets/parisrohan/credit-score-classification/data)

### Objective

The objective of this project is build up a model that is capable of predicting the Credit Scores of users and being served via a web interface.

### Steps

1. **EDA** This project starts by exploring the data and applying a series of cleaning processes to put the data in a state that could be used to build classification models, the code of these operations could be found in this Notebook [credit_cls_Data_Cleansing.ipynb](credit_cls_Data_Cleansing.ipynb).
2. **Modeling** The modelling part utilizes `Mlflow` for experiments tracking and models registration. For _reproducibility_, you may run `Mlflow server` locally or setup it up in a remote machine, in my case, I used [_Dagshub_](https://dagshub.com/) integrated `Mlflow server`. At any case, make sure to have a `.env` file available at the root directory and provide the following environment variables.

```Bash

# In case of running Locally

MLFLOW_TRACKING_URI="http://localhost:<port-number>"

# In case of using Dagshub, provide the tracking credentials from Dagshub repo

MLFLOW_TRACKING_URI="https://dagshub.com/<account-name>/<repo-name>.mlflow"

MLFLOW_TRACKING_USERNAME="<account-name>"

MLFLOW_TRACKING_PASSWORD="<password-str>"

```

the code of the modelling could be found in this Notebook [credit_score_modeling.ipynb](credit_score_modeling.ipynb).

> [!NOTE]
> The results of the experiments are registered at the integrated `Mlflow server` with this [_Dagshub repo_](https://dagshub.com/imirghania/Credit_Classification_project).

Out of three classifiers, (_RandomForest, XGBoost_ and _LightGBM_), _RandomForest_ classifier resulted in a slightly better metrics than XGBoost but that was at the expense of the model size where the best model of the _RandomForest_ classifier has a size of `644.46 MB` whilist the best model of _XGBoost_ has a size of `7.36 MB`. Therefore, the model that has been set to production was the fine-tunned model of _XGBoost_.

3.  **Deployment** The chosen method for serving the final model of the experimentations is a web interface. The frontend is built using [streamlit](https://streamlit.io/), the backend is built using [FastAPI](https://fastapi.tiangolo.com/) and both of them are connected and served using [Docker](https://www.docker.com/)
    The code of the frontend could be found in [/frontend](frontend) directory and the backend as well could be found in the [/backend](backend) directory.

- To run the web service use the following code

```Bash
docker-compose up -d --build
```

Then go to the following url: http://localhost:8501/

- To stop the web service use the following code

```Bash
docker-compose down
```
