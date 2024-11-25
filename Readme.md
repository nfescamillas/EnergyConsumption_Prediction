BACKGROUND:

This is a midterm project for the DTC MLOps Zoomcamp. This is a cloud deployed ML project (PythonAnywhere) that has the objective of  predicting the actual kwh consumption of a Steel Industrial Plant . The dataset is found on kaggle for future references with the following link:

https://www.kaggle.com/datasets/csafrit2/steel-industry-energy-consumption

PROJECT WORKFLOW:

As mentioned , the dataset was downloaded from Kaggle and was imported to jupyter notebook for data preparation, analysis and modeling . From the notebook a pickle file was generated both for the model and scaler (Standard Scaler). The project was tested locally using a virtual environment and later was dockerized . 

The predict.py file contains the Flask Application and the test.py contains an instance to test the deployment . There are two urls present in the test.py that caters both local deployment and cloud deployment. The preset url for this project is set to check the model deployed on the cloud. The model was deployed on the cloud using PythonAnywhere , where the instruction for deployemnt can be found on the link :

https://github.com/nindate/ml-zoomcamp-exercises/blob/main/how-to-use-pythonanywhere.md

The project yielded good results on test data as well using plain linear regression which can also be seen on the EDA done on the notebook. Overall the project has a lot of potential for future improvement that also includes testing of other models. 




