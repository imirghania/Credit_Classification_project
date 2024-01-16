# Credit Classification project 💰🤑💸💳

### Dataset

The data is included in the directory `data` within this repo and it has been downloaded from Kaggle @[this Link](https://www.kaggle.com/datasets/parisrohan/credit-score-classification/data)

This project employes Mlflow for experiments tracking and models registering.
You may run Mlflow server locally or setup it up in a remote machine, in my case, I used [_Dagshub_](https://dagshub.com/) integrated Mlflow server. At any case make sure to have a `.env` file available at the root directory and provide the following environment variables

```Bash
# In case of running Locally
MLFLOW_TRACKING_URI="http://localhost:<port-number>"
# In case of using Dagshub, provide the tracking credentials from Dagshub repo
MLFLOW_TRACKING_URI="https://dagshub.com/<account-name>/<repo-name>.mlflow"
MLFLOW_TRACKING_USERNAME="<account-name>"
MLFLOW_TRACKING_PASSWORD="<password-str>"
```
