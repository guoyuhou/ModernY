import streamlit as st
import os
from Github import get_relative_path

file_path = 'D:\Project\ModernY\ModernY_tools\Github.py'  
relative_path = get_relative_path(file_path)  
print(relative_path, '=============================')

st.title('Command')
st.write('Clear the vision')
st.code('cls')
st.write('Check the information of your package')
st.code('python -m pip show setuptools')