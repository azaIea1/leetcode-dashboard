import streamlit as st
from lcdash.db import init_db

st.set_page_config(page_title="LeetCode Dashboard", layout="wide")
init_db()

st.title("LeetCode Practice Dashboard")
st.write("Day 1: DB initializes automatically. Check DB Status in the sidebar.")
