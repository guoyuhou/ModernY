import streamlit as st
import os
from Github import get_relative_path

file_path = 'D:\Project\ModernY\ModernY_tools\Github.py'  
relative_path = get_relative_path(file_path)  
print(relative_path, '=============================')



st.title('PyQt5')
st.write(f'1. __Enter the virtual envirment__')
st.code('myenv\Scripts\ activate')

