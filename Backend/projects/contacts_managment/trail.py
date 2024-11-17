import streamlit as st
import pandas as pd
import numpy as np
# Text First web based application
st.title("Text Formats ")
st.write("This is our First Application")

# Text Elements
st.header("This is a Header")
st.subheader("Im a subheader")
st.text("This is a text")
st.markdown("> This a **Markdown format**")
st.code("print('hello')")


# Display Data
st.title("Display Data Formats")

data = pd.DataFrame({
    "C1":[1,2,3,4],
    "C2":[10,20,30,40]
})
# As a dataframe
st.dataframe(data)

# As a table
st.table(data)

# Linechart
st.line_chart(data)

st.bar_chart(data)

st.title("Taking Inputs in different forms")

name = st.text_input("Enter your name: ")
st.write("Your name is ",name)

age = st.number_input("Enter Your age",min_value=16,max_value=80)
st.write("Your Age is ",age)

is_student = st.checkbox("Are you student? ")
st.write(is_student)

color = st.selectbox("Choose any color",["Red","black","White"])


# Layouts and containers

col1, col2 = st.columns(2)
with col1:
    st.header("Col 1")
    st.write("Column 1 content will be here")
with col2:
    st.header("Col 2")
    st.write("Column 2 content will be here")

with st.container():
    st.header("Container")
    st.write("Container  content will be here")

# Interactive Widgets
st.title("Progress bar")

import time

progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress_bar.progress(i+1)



