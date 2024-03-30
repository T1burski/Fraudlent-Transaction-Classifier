import streamlit as st
import pickle
import numpy as np
import pandas as pd
from src.data_generator import DataGenerator
from src.model_functions import ModelFunctions


# Loading the model saved on pickle format

def load_model():
    with open('artifacts\model.pkl', 'rb') as model:
        clf_model = pickle.load(model)
    return clf_model
clf_prod = load_model()

# Start building the front-end using Streamlit

st.title("Prediction of Fraudulent Transactions: An ML Web App")
st.write("""### This is a simulator of a production environment in which a classification model predicts if a transaction is fraudulent or not""")
st.divider()

# Everytime the user interacts with the add/sub number of transactions, the are recalculated
 
number = st.number_input('Select a number of transactions to apply the prediction on:', min_value=1, step=1)
st.divider()

df = DataGenerator(number).generate_df()
st.write("""### Representation of each transaction in which we want to apply the model""")
st.write(df)
st.divider()

df_pred = df.copy()
prediction = ModelFunctions().class_threshold(clf=clf_prod, X_pred=df)
df_pred["Potential Fraud"] = prediction
df_pred["Potential Fraud"] = np.where(df_pred["Potential Fraud"]==1, "Yes", "No")
st.write("""### Results of the prediction applied to each transaction shown above""")
st.write(df_pred)
st.divider()

df_grouped = df_pred.groupby(["Potential Fraud"]).agg(Transactions=('Potential Fraud', 'count')).reset_index()
st.write("""### Report showing how many transactions were fraudulent or not""")
st.write(df_grouped)