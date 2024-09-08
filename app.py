import streamlit as st
import markdown
import os
import pygwalker
from pygwalker.api.streamlit import StreamlitRenderer
import time
import oss2
from io import BytesIO


# 从Streamlit的Secrets中读取OSS的密钥和存储桶信息
ACCESS_KEY_ID = st.secrets["oss"]["OSS_ACCESS_KEY_ID"]
ACCESS_KEY_SECRET = st.secrets["oss"]["OSS_ACCESS_KEY_SECRET"]
BUCKET_NAME = st.secrets["oss"]["OSS_ENDPOINT"]
ENDPOINT = st.secrets["oss"]["OSS_BUCKET_NAME"]

# 创建OSS认证和存储桶对象
auth = oss2.Auth(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
bucket = oss2.Bucket(auth, ENDPOINT, BUCKET_NAME)

def list_files():
    files = []
    for obj in oss2.ObjectIterator(bucket):
        files.append(obj.key)
    return files

def display_files():
    st.subheader('文件列表')
    files = list_files()
    if files:
        for file in files:
            st.write(file)
    else:
        st.write('没有文件可显示')

def upload_file():
    st.subheader('上传文件')
    uploaded_file = st.file_uploader("选择要上传的文件")
    if uploaded_file:
        file_name = uploaded_file.name
        bucket.put_object(file_name, uploaded_file)
        st.success(f'文件 {file_name} 上传成功')

def download_file():
    st.subheader('下载文件')
    files = list_files()
    file_name = st.selectbox('选择要下载的文件', files)
    if file_name:
        if st.button('下载'):
            obj = bucket.get_object(file_name)
            file_data = obj.read()
            st.download_button(
                label='下载文件',
                data=file_data,
                file_name=file_name,
                mime='application/octet-stream'
            )



def page():
    pages = {
        'ModernY': 'ModernY_page.py',
        'PyGWalker': 'PyGWalker.py',
        'Blogs': 'Blogs.py',
        'Papers': 'Papers.py',
        'Project': 'Project.py',
        'Tools': {
            'Github': os.path.join('ModernY_tools', 'Github.py'),
            'Command': os.path.join('ModernY_tools', 'Command.py'),
            'PyQt5': os.path.join('ModernY_tools', 'PyQt5.py'),
            'Storm Genie': os.path.join('ModernY_tools', 'Storm_genie.py'),
            'Smalltools': os.path.join('ModernY_tools', 'smalltools.py'),
            'Chatpaper': os.path.join('ModernY_tools', 'Chatpaper.py')
        },
        'Cloud Storage': 'cloud_storage.py'  # 新增页面
    }

    page_name = st.sidebar.radio('Navigation', list(pages.keys()))
    page_file = None

    if page_name == 'ModernY':
        page_file = pages[page_name]
    elif page_name == 'PyGWalker':
        page_file = pages[page_name]
    elif page_name == 'Blogs':
        page_file = pages[page_name]
    elif page_name == 'Papers':
        page_file = pages[page_name]
    elif page_name == 'Project':
        page_file = pages[page_name]
    elif page_name == 'Tools':
        tool = pages[page_name]
        page_title = st.sidebar.radio('Classification', list(tool.keys()))
        page_file = tool[page_title]
    elif page_name == 'Cloud Storage':
        page_file = pages[page_name]
        display_files()
        upload_file()
        download_file()
    
    if page_file:
        try:
            with open(page_file, encoding='utf-8') as file:
                exec(file.read())
        except FileNotFoundError:
            st.write(f'文件 {page_file} 找不到')
        except Exception as e:
            st.write(f'执行文件时出错: {e}')
    else:
        st.write('所选页面不正确')

page()