import streamlit as st
import time
import os
print('===========================================================================')
def page():
    pages = {
        'ModernY': 'ModernY_page.py',
        'Tools': {
            'Github' : 'ModernY/ModernY_tools/Github.py',
            'Command': 'ModernY/ModernY_tools/Command.py',
            'PyQt5': 'ModernY/ModernY_tools/PyQt5.py',
            'Strom Genie': 'ModernY/ModernY_tools/Storm_genie.py',
            'Markdown': 'ModernY/ModernY_tools/Markdown.py',
            'Smalltools': 'ModernY/ModernY_tools/smalltools'   
        }
    }
    page_name = st.sidebar.radio('Navigation', list(pages.keys()))
    page_file = None

    if page_name == 'ModernY':
        page_file = pages[page_name]
    if page_name == 'Tools':
        page = pages[page_name]
        page_title = st.sidebar.radio('Classification', list(page.keys()))
        page_file = page[page_title]
    if page_file:
        exec(open(page_file, encoding='utf-8').read())
    else:
        st.write('所选页面不正确')

page()