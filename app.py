import streamlit as st
import time
import os
print('===========================================================================')
def page():
    pages = {
        'ModernY': 'ModernY_page.py',
        'Tools': {
            'Github' : 'Github.py',
            'Command': 'Command.py',
            'PyQt5': 'PyQt5.py',
            'Strom Genie': 'Storm_genie.py',
            'Markdown': 'Markdown.py',
            'Smalltools': 'ModernY_tools'
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