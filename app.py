import streamlit as st


st.title("This is a title")
st.write("Hello **World**!")
"Hello Magic"
st.markdown(
    """
## Hello Markdown 
- item1 
- item2 
"""
)
code = """
def hello():
    a=2
    print("Hello, Streamlit!")
"""
st.code(code, language="python")
