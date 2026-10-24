import numpy as np
import pandas as pd
import pickle
import streamlit as st

# Load the trained machine learning model
infile = open(r"E:\PGCP-AI\PML\Cases\Wisconsin\svm_model.pkl", "rb")
objmodel = pickle.load(infile)
infile.close()

# Page Title
st.title("Breast Cancer Prediction App")
st.write(
    "Adjust the feature values below to predict the likelihood of cancer diagnosis."
)

# Organize inputs into 3 columns
col1, col2, col3 = st.columns([0.33, 0.33, 0.33])

with col1:
    Clump = st.slider("Clump Thickness", min_value=1, max_value=10,  step=1)

    UniCell_Size = st.slider( "Uniformity of Cell Size", min_value=1, max_value=10, value=5  )

    Uni_CellShape = st.slider("Uniformity of Cell Shape", min_value=1, max_value=10, value=5)

with col2:
    MargAdh = st.slider(
        "Marginal Adhesion", min_value=1, max_value=10, value=5
    )
    SEpith = st.slider(
        "Single Epithelial Cell Size", min_value=1, max_value=10, value=5
    )
    BareN = st.slider("Bare Nuclei", min_value=1, max_value=10, value=5)

with col3:
    BChromatin = st.slider(
        "Bland Chromatin", min_value=1, max_value=10, value=5
    )
    NoemN = st.slider("Normal Nucleoli", min_value=1, max_value=10, value=5)
    Mitoses = st.slider("Mitoses", min_value=1, max_value=10, value=5)

st.markdown("---")


df= pd.DataFrame({
    'Clump': [Clump],
    'UniCell_Size': [UniCell_Size],
    'Uni_CellShape': [Uni_CellShape],
    'MargAdh': [MargAdh],
    'SEpith': [SEpith],
    'BareN': [BareN],
    'BChromatin': [BChromatin],
    'NoemN': [NoemN],
    'Mitoses': [Mitoses],
})



pred= objmodel.predict(df)[0]
st.write('Predicted class: {}'.format(pred))