import streamlit as st

st.page_link("Home.py", label="Hssssssssssfdgdg", icon="🏠")
st.page_link("pages/DTree.py", label="การทำนายข้อมูลด้วยเทคนิคต้นไม้ตัดสินใจ", icon="1️⃣")
st.page_link("pages/NaiveBaye.py", label="การทำนายข้อมูลด้วยเทคนิค Naive Baye", icon="2️⃣", disabled=False)
st.page_link("http://www.google.com", label="Google", icon="🌎")
st.header("2")


import streamlit as st

# Define page functions
def home_page():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

def page1():
    st.title("Page 1")
    st.write("This is Page 1")

def page2():
    st.title("Page 2")
    st.write("This is Page 2")

# Sidebar navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Page 1", "Page 2"])

# Display the selected page
if selection == "Home":
    home_page()
elif selection == "Page 1":
    page1()
elif selection == "Page 2":
    page2()
