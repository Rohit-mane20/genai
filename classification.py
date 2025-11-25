import streamlit as st
import pandas as pd 
from  sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(data = iris.data , columns= iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df,target_names = load_data()
print(df.shape, df.hist())
# Example: use iloc to select all rows except the first one
# (i.e., skip row with index 0)


model = RandomForestClassifier()
model.fit(df.iloc[: , : -1] , df['species'])


st.sidebar.title("input features")

sepal_length = st.sidebar.slider("sepal length", float (df['sepal length (cm)'].min()), float (df['sepal length (cm)'].max()), float (df['sepal length (cm)'].mean()))
sepal_width = st.sidebar.slider("sepal width", float (df['sepal width (cm)'].min()), float (df['sepal width (cm)'].max()), float (df['sepal width (cm)'].mean()))
petal_length = st.sidebar.slider("petal length", float (df['petal length (cm)'].min()), float (df['petal length (cm)'].max()), float (df['petal length (cm)'].mean()))
petal_width = st.sidebar.slider("petal width", float (df['petal width (cm)'].min()), float (df['petal width (cm)'].max()), float (df['petal width (cm)'].mean()))   

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

prediction = model.predict(input_data)
predict_species = target_names[prediction][0]
st.write("## Prediction Result")
st.write(f"Predicted species: {predict_species}")