import streamlit as st
import os
def get_relative_path(file_path, base_path='.'):  
    """  
    获取文件的相对路径。  
      
    :param file_path: 目标文件的绝对路径  
    :param base_path: 基路径，默认为当前工作目录  
    :return: 相对路径  
    """  
    # 获取当前工作目录的绝对路径  
    if base_path == '.':  
        base_path = os.getcwd()  
      
    # 获取目标文件的绝对路径  
    file_path = os.path.abspath(file_path)  
      
    # 计算相对路径  
    relative_path = os.path.relpath(file_path, base_path)  
      
    return relative_path  
  
# 示例  
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
st.image('Images/image001.png', caption='Application page')