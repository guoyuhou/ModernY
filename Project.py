# project.py  
import streamlit as st  
import os
  
# 读取同目录下的 CD_.md 文件  
def load_markdown_file(file_name):  
    with open(file_name, 'r', encoding='utf-8') as file:  
        return file.read()  
  
# 将 MD 文件内容显示在 Streamlit 网页上  
file_path = os.path.join('Project, 实验设计.md')
md_content = load_markdown_file(file_path)  
st.markdown(md_content)  
  

def download_block():
    st.subheader('文件下载：')
    # 获取Project文件夹路径  
    project_folder = os.path.join(os.path.dirname(__file__), 'Project')  
    
    # 列出Project文件夹中的所有文件  
    files = os.listdir(project_folder)  
    
    # 创建一个下拉框供用户选择文件  
    selected_file = st.selectbox("选择你想要下载的文件", files)  
    
    # 如果用户选择了文件，则提供下载链接  
    if selected_file:  
        file_path = os.path.join(project_folder, selected_file)  
        
        # 使用st.download_button提供下载功能  
        with open(file_path, 'rb') as file:  
            st.download_button(  
                label=f"下载 {selected_file}",  
                data=file,  
                file_name=selected_file,  
                mime='application/octet-stream'  # 适用于任意二进制文件，可以根据文件类型调整  
            )

download_block()