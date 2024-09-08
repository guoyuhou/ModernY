import streamlit as st
import markdown
import os
import pygwalker
from pygwalker.api.streamlit import StreamlitRenderer
import time
import oss2
# OSS 配置
access_key_id = os.getenv('OSS_ACCESS_KEY_ID')
access_key_secret = os.getenv('OSS_ACCESS_KEY_SECRET')
endpoint = os.getenv('OSS_ENDPOINT')  # 你的 OSS 端点
bucket_name = os.getenv('OSS_BUCKET_NAME')  # 你的桶名称
 
# 初始化 OSS 客户端
auth = oss2.Auth(access_key_id, access_key_secret)
bucket = oss2.Bucket(auth, endpoint, bucket_name)

def list_files():
    files = [obj.key for obj in oss2.ObjectIterator(bucket)]
    return files

def upload_file(file):
    bucket.put_object(file.name, file.read())

def download_file(file_key):
    return bucket.get_object(file_key).read()

def delete_file(file_key):
    bucket.delete_object(file_key)

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
        }
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


    page_name = st.sidebar.radio('Navigation', list(pages.keys()))
    page_file = pages.get(page_name)

    if page_file:
        try:
            if page_name == 'File Manager':
                st.title('File Manager')

                # 文件上传
                uploaded_file = st.file_uploader("上传文件", type=['txt', 'csv', 'jpg', 'png'])
                if uploaded_file:
                    upload_file(uploaded_file)
                    st.success("文件上传成功")

                # 文件展示
                if st.button('显示所有文件'):
                    files = list_files()
                    st.write("云存储中的文件:")
                    for file in files:
                        st.write(file)
                        if st.button(f'下载 {file}'):
                            file_content = download_file(file)
                            st.download_button(label=f"下载 {file}", data=file_content, file_name=file)

                # 文件删除
                file_to_delete = st.text_input("输入要删除的文件名")
                if st.button("删除文件"):
                    if file_to_delete:
                        delete_file(file_to_delete)
                        st.success(f"文件 {file_to_delete} 已删除")
                    else:
                        st.error("请提供要删除的文件名")
                    
            else:
                with open(page_file, encoding='utf-8') as file:
                    exec(file.read())
        except FileNotFoundError:
            st.write(f'文件 {page_file} 找不到')
        except Exception as e:
            st.write(f'执行文件时出错: {e}')
    else:
        st.write('所选页面不正确')

page()


