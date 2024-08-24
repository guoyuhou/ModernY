import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRender
import os

st.set_page_config(
    page_title = 'PyGWalker',
    layout='wide'
)   

st.title('PyGWalker')

# 创建一个文件上传器，允许用户上传CSV文件  
uploaded_file = st.file_uploader("选择你的CSV文件", type=["csv"])  
  
if uploaded_file is not None:  
    # 使用Pandas读取上传的CSV文件  
    data = pd.read_csv(uploaded_file)  
  
    # 显示数据帧的前几行  
    st.write(data.head())  
  
    # 定义一个函数来获取渲染器，确保在文件上传后才调用  
    @st.cache_resource  
    def get_pyg_renderer(df):  
        return StreamlitRender(df, spec='./gw_config.json', spec_io_mode='rw')  
  
    renderer = get_pyg_renderer(data)  
    renderer.explorer()