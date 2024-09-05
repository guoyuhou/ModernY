import streamlit as st
import markdown
import os
import pygwalker
from pygwalker.api.streamlit import StreamlitRenderer
import time
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
            'Smalltools': os.path.join('ModernY_tools', 'smalltools.py')
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

page()
