# Wind Farm Power Forecasting

Welcome to the Wind Farm Power Forecasting project repository! Our project is centered around the development of a web API tailored for predicting the power production of windmill farms. Accurate forecasting of renewable energy generation is vital for optimizing power systems and facilitating the integration of more renewable energy sources into the grid. Without precise forecasts, we cannot fully harness the benefits of an efficient energy management system.

Forecasting renewable energy generation is a complex task due to its inherent variability, which is heavily influenced by meteorological conditions such as wind speed, temperature, and air pressure. To tackle this challenge, our project utilizes a multi-step recursive forecasting approach with XGBoost, a powerful machine learning algorithm.


For our project, we leverage the dataset sourced from the "Solar and Wind Power Data from the Chinese State Grid Renewable Energy Generation Forecasting Competition". This dataset contains comprehensive information on power generation from six windmill farms, each equipped with various turbine types. Our focus lies on farms 1, 2, and 3. The dataset provides power generation data at a 15-minute granularity, alongside weather-related variables. 

We have included a breakdown of the wind power data across the three sites, showcasing the diversity in rotor diameters and hub heights of the windmills. Additionally, we have provided a description of the dataset columns for better understanding.

## Project Components

### Datasets
- We have included datasets for the three studied wind farms. These datasets are used for training and evaluating the forecasting model. They can be found under the ./Datasets folder

- EDA was performed on the data from the three wind farms to determine the best features to use for forecasting the power. This EDA for each can be found in the corresponding TEST1_models, TEST2_models and TEST3_models respectively. 

### Model
- The project includes the trained XGBoost model used for power forecasting. The model has been trained on historical data from the wind farms. 

- The decision to use XGBoost was made after performing EDA and metric comparison between different models, including a linear regressor, Random Forest, ARIMA, SARIMA, AR and MA. We also tested some models with dimensionality reduction. The goal was to compare the results we got from the different models and determine the best model, which was XGBoost for our final webapp. We run the XGBoost seperately in XGBoost_final.ipynb for good measure

### Notebook
- The Jupyter notebook used to train the XGBoost model is provided in the repository. You can explore the data preprocessing, model training, and evaluation steps in this notebook.

- The TEST files show the EDA for each wind farm. The ARIMA_SARIMA file specifically focuses on forecasting using those models.

### Slides
- Slides containing performance metrics and insights from the forecasting model are included. These slides provide an overview of the project and its outcomes.

### Flask Code and HTML Files
- The Flask code and HTML files constitute the web application interface for accessing the power forecasting functionality. Users can input wind farm IDs and forecasting horizons to receive power generation predictions.

### Postman Environment and Documentation
- We have created a Postman environment and documented the API endpoints for easy integration and testing. The documentation provides details on how to interact with the forecasting API. [Postman Environment and Documentation](https://documenter.getpostman.com/view/31038181/2sA3Bt3puG)

## Usage
To use the Wind Farm Power Forecasting application:
1. Clone this repository to your local machine.
2. Install the necessary dependencies as mentioned below:

#!/bin/bash
 
#### Update the package index
sudo apt update
 
#### Install necessary packages
sudo apt install python3-pip python3-dev nginx -y
 
#### Install virtualenv
sudo pip3 install virtualenv
 
#### Create a virtual environment
virtualenv env
 
#### Activate the virtual environment
source env/bin/activate
 
#### Install required Python packages
pip install uwsgi pandas xgboost Flask openpyxl scikit-learn
 
#### Deactivate the virtual environment
deactivate
 
#### Run uwsgi
uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:application

3. Run the Flask application to start the server.
4. Access the web interface through your browser and input wind farm IDs and forecasting horizons to get power generation predictions.

## Contributors
- mattdltvt5 | hussainv5253 | Ganta-Karthik1999
