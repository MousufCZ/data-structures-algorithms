from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize and authenticate
api = KaggleApi()
api.authenticate()

# Download a dataset
api.dataset_download_files('heptapod/titanic', path='data/', unzip=True)
