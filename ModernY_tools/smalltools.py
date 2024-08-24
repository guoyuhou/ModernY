import streamlit as st
import os
from Github import get_relative_path

file_path = 'D:\Project\ModernY\ModernY_tools\Github.py'  
relative_path = get_relative_path(file_path)  
print(relative_path, '=============================')


st.title('Small and interesting tools!')
st.subheader('Everything')
st.write(f'Everything is a tool that could help you quickly find the location of your files')
st.write('__Address__:https://www.voidtools.com/zh-cn/')
st.image('ModernY/Images/image.png', caption='Everything')