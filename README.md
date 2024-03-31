# Fraudulent-Transaction-Classifier

This is a ML project focused on developing a model and ML App that classifies a financial transaction as fraudulent or not. This kind of data-driven classification is key in order to guarantee the security in financial institutions.
#


![image](https://github.com/T1burski/Fraudlent-Transaction-Classifier/assets/100734219/5c644126-0198-4b64-b10e-807347e7c9f6)

## 1) The Problem to be Addressed
Financial institutions all over the world, specially the ones related to services associated with monetary transactions, suffer from security issues such as a false transaction, also named a fraudulent transaction. These happen, generally, when a client's account is accessed by a third illegal party to transfer money or buy things (products, services, etc). So, the following challenge stands for these institutions: Can we automatically detect, in real time, if a transaction is a fraud in order to cancel its execution, protecting the company and the client?

With the advance of data-driven solutions such as machine learning algorithms, this task can be done. For example, supervised classification models based on historical data that represents the behaviour and occurrance can be trained in order to judge future transactions, labeling them as fraudulent or not. With this being said, the present project tackles this challenge using the mentioned strategy: through machine learning models, we will develop a tool that predicts if a transaction is fraudulent or not based on previous occurrances.

## 2) The Data
Real data from transactions made by credit cards in September 2013 by European cardholders will be used to develop the ML model. The data can be obtained in https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud. The original dataset has 284807 transactions and 31 columns of which 30 are features regarding characteristics of the transactions and the other column states if a the transaction was fraudulent (1) or not (0) (Class column). All features from V1 - V28 were anonymized using PCA, while features Amount and Time were not. As stated in the link provided previously, this dataset is highly imbalanced regarding the Class output: only 0.172% of all transactions in the original dataset are fraudulent transactions.

Features V1 through V28 represent anonymized and various characteristics regarding the client and the transaction happening. Amount represents (hypothetically in EUR) the monetary amount of the transaction. Time represents the time elapsed between the current transaction and the first transaction in the dataset.

## 3) Technologies That Help us Solve the Problem
We have in our hands a Supervised Classification problem. Using a venv using pip, we develop the model using Visual Studio Code with Python language with various libraries such as Pandas, Numpy, XGBoost and SKLearn. Finally, we deploy our model in a web app made with Streamlit.

![image](https://github.com/T1burski/Fraudulent-Transaction-Classifier/assets/100734219/937b5676-059e-4089-9889-8671ab234608)

The Python version used was 3.9.13

## 4) Exploring and Building the Solution
All details regarding exploratory data analysis, hypothesis, statiscal findings, feature selection, model selection and model hyperparameter tuning are fully documented and explained on the eda.ipynb file within the notebook folder of the project.

## 5) Solution Architecture: Modules, Pipeline and Application

![image](https://github.com/T1burski/Fraudulent-Transaction-Classifier/assets/100734219/73f4760a-7072-457a-bb04-d72d331cb9e3)

As said before, the whole project was built in a virtual environment in order to isolate dependencies, which are available in the requirements.txt file. Every module used in order to build the final application is available in the src folder. These modules cover all the steps in order to ingest, manipulate and process data as well as train and build the ML model, all isolated in order to facilitate the app's structure management. Above, an image that shows, in a simple way, the prject's structure and pipeline.

## 6) ML Web App
Below, screenshots of the Web App with brief explanations about each of them.

![image](https://github.com/T1burski/Fraudulent-Transaction-Classifier/assets/100734219/10c565a7-680a-483a-834f-876ebf8bac44)
When you start the ML Web App, you'll see a brief presentation of it and a button that lets the user select how many transactions they want to apply the model on in order to label them as potential frauds or not.

======================================

![image](https://github.com/T1burski/Fraudulent-Transaction-Classifier/assets/100734219/f0b314ba-a7f1-40b6-b0bf-ce73a567c39e)
Below, the user will be able to see each of the features used and their respective values. These values are generated using the data_generator.py module, which produces, for each variable, a random number between the min and the max values of that variable in the original dataset. Therefore, we have a simulator of transactions which will be labeled as fraudulent or not. Everytime the user changes the number of transactions they want to label, the whole app gets updated to show that number of transactions.

======================================

![image](https://github.com/T1burski/Fraudulent-Transaction-Classifier/assets/100734219/b54e981e-32c7-416b-b063-0e3a7f1de7c9)
So, in the end, the generated transactions are print along with their classification according to the trained model. Also, a small report is printed showing, from all transactions generated, how many were and were not labeled as potential frauds. 

## 6) Financial Impacts of the Model
After traininig the model on the training data, we tested it on unseen testing data. After applying it (more details can be seen in the eda.ipynb in the notebooks folder), the following results were obtained:

Considering that a correct prediction if a transaction is a fraud provides the info necessary so that the financial institution cancels/locks the said transaction (protecting both the client and the institution), the Amount (EUR) associated with that transaction can be considered as "a value not moved in a wrong and illegal way", meaning this Amount can be seen as a financial gain. Following this logic, when the model was applied to the testing data, it correctly predicted that 52 of the 71 fraudulent transactions were potential frauds.

### The Amount associated to these 52 transactions was 7402.10 EUR, representing the financial impact of the model regarding the testing data (42559 total transactions)

## 7) How to Use the ML Web App

In order to test this tool yourself, you'll need to clone this repository in a folder in your computer and create a virtual environment using, in a terminal:

### python -m venv class_transactions

After, activate the virtual environment using in a terminal:

class_transactions\Scripts\activate

Install the necessary dependencies of the project using in a terminal:

pip install -r requirements.txt

So, run the following command to run the Web App in a terminal:

streamlit run app.py

A tab will open in your browser and you'll be able to interact with the tool!

To deactivate the virtual environment, in a terminal:

deactivate
