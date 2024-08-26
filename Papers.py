import streamlit as st  
import markdown
import os  
st.title('Papers')
st.write('By Alexander')
print(markdown)
# 定义一个函数，用于读取并转换Markdown文件为HTML  
def read_markdown_file(file_path):  
    with open(file_path, "r", encoding="utf-8") as file:  
        markdown_content = file.read()  
    return markdown.markdown(markdown_content)  
  
# 设定包含Markdown文件和PDF文件的文件夹路径  
papers_folder = "paperfiles"  # 假设你的Markdown文件和PDF文件都存放在这个文件夹中  
  
# 获取文件夹中所有Markdown文件的名称  
paper_notes = [f for f in os.listdir(papers_folder) if f.endswith(".md")]  
  
# 获取文件夹中所有PDF文件的名称  
paper_pdfs = [f for f in os.listdir(papers_folder) if f.endswith(".pdf")]  
  
# 创建一个下拉菜单，让用户选择想要查看的论文笔记  
selected_paper_note = st.selectbox("请选择一篇论文笔记查看", paper_notes)  
  
# 当用户从下拉菜单中选择一篇论文笔记时，读取并显示对应的Markdown文件内容  
if selected_paper_note:  
    paper_note_path = os.path.join(papers_folder, selected_paper_note)  
    paper_content = read_markdown_file(paper_note_path)  
    st.markdown(paper_content, unsafe_allow_html=True)  
  
    # 获取与Markdown文件对应的PDF文件名（假设它们有相同的文件名前缀）  
    pdf_filename = selected_paper_note.replace(".md", ".pdf")  
    if pdf_filename in paper_pdfs:  
        pdf_path = os.path.join(papers_folder, pdf_filename)  
        # 添加一个下载按钮，让用户可以下载PDF文件  
        st.download_button(label=f"下载{pdf_filename}", data=pdf_path, file_name=pdf_filename)