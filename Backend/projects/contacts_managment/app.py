import streamlit as st
import pandas as pd
import numpy as np

# Title and Description about the application
st.title("Educational Streamlit Application")
st.write("This will give a basic idea of Streamlit application usage")


# User Inputs:
name = st.text_input("Enter your name: ")
st.write(f"hello {name}!!")

# Use Data
df= pd.DataFrame({
    "Numbers":np.arange(1,11),
    "Squares":np.arange(1,11)**3
})

st.write("Here is a table of number and their Squares")
st.dataframe(df)

# Chart
st.line_chart(df)

#check box
if st.checkbox("Show raw Data"):
    st.write(df)