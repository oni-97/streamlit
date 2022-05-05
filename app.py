import streamlit as st
import pandas as pd
import numpy as np

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

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data)

if st.button("Click me"):
    st.write("Thanks to click")

agree = st.checkbox("I agree")
if agree:
    st.write("Great!")

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)
st.write("You selected:", options)


age = st.slider("How old are you?", 0, 130, 20)
st.write("I'm ", age, "years old")
