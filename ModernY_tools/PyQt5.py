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
file_path = 'D:\Project\ModernY\ModernY_tools\PyQt5.py'  
relative_path = get_relative_path(file_path)  
print(relative_path, '=============================')

st.title('PyQt5')
st.write(f'1. __Enter the virtual envirment__')
st.code('myenv\Scripts\ activate')

