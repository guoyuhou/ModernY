import streamlit as st
import os
from Github import get_relative_path

file_path = 'D:\Project\ModernY\ModernY_tools\Storm_genie.py'  
relative_path = get_relative_path(file_path)  
print(relative_path, '=============================')


st.title('Strom Genie')
st.subheader('Storm genie')
st.caption('by stanford')
st.write(f'__Address__: _https://storm.genie.stanford.edu/_')
st.write(f'__Introduce__:This model could help us to generate a article that include main chapter and some '
         'argument. These information is summarized by some papers so that this article have'
         'quote at the end of it. __This model could help us learn quickly in a new area__')
st.image('ModernY/Images/image001.png', caption='Application page')