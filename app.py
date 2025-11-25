import streamlit as st
import pandas as pd
import numpy as np
st.title("Dictionary in Python")

dataframe = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

st.write("Here is a sample DataFrame:")
st.dataframe(dataframe)

# np.random.randn() generates values from a standard normal distribution
# This means values typically range from approximately -3 to +3
# About 68% of values fall between -1 and +1
# About 95% of values fall between -2 and +2
# About 99.7% of values fall between -3 and +3
chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=['a', 'b', 'c']
)

print(chart_data.shape)
lineChart = st.line_chart(chart_data)