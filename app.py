import streamlit as st
import pandas as pd

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


df = pd.DataFrame({"col1": [1, 2, 3, 4], "col2": [-1, -2, -3, -4]})
st.dataframe(df.style.highlight_max(axis=0))

st.json(
    {
        "fruir": "apple",
        "sports": [
            "soccer",
            "basebal",
            "basketball",
        ],
    }
)
