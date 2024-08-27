import streamlit as st
import os

st.title('Command')
st.write('Clear the vision')
st.code('cls')
st.write('Check the information of your package')
st.code('python -m pip show setuptools')

# create your virual environment
st.write('Create a virual environment')
st.code('python3 -m venv NAME')