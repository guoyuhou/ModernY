import streamlit as st
import os

from Github import get_relative_path

file_path = 'D:\Project\ModernY\ModernY_tools\Github.py'  
relative_path = get_relative_path(file_path)  
print(relative_path, '=============================')


st.title('Markdown')
st.text(f'1. Title:'
         '\n # First level title'
         '\n ## Second level title'
         '\n ### Third level title')

