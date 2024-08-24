import streamlit as st
st.title('GitHub')

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
relative_path = get_relative_path(file_path)  
print(relative_path, '=============================')



# Github
st.title('Github')
st.write(f'__Address__:https://github.com/dashboard')
st.write(f'__Introduce__: Github is the largest computer community.We could find project or package'
         'and you can also learn here no matter what you want to learn.'
         '_This is truly useful!_')
# Transform code in repository
st.subheader('Update Code In Your repository')
st.write(f'1. Initialize a git')
st.code('git init')
st.write(f'2. Add your files in staging area')
st.code('git add .')
st.write(f'3. Add your files in local repository')
st.code('git commit -m "Initial commit"')
st.write('4. Connect remote GitHub repository and push files')
st.code('git remote add origin URL')
st.code('git push -u origin main')

st.text('__My default config__'
         'git config --global user.email "17806067729@163.com"'
         'git config --global user.name"Alexander"')

# Update code in repository
st.subheader('Update code in repository')
st.write('1. config your name and email')
st.code('git config ==global user.name "uesr name"')
st.code('git config ==global user.email "uesr eamil"')
st.write('2. ###Generate your SSH key'
         '\d your SSH key will be solved in id_rsa.pub')
st.code('ssh-keygen -t rsa -C "17806067729@163.com"') 
st.write('3. Config your SSH in Github')
st.write('4. Check the status')
st.code('git status')
st.write('5. Commit your files')
st.code('git commit -m "Your note"')
st.write('4. Push your code')
st.code('git push')
st.write('### My SHH keys: C:\\Users\\14526\\.ssh ')