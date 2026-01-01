import streamlit as st
import pandas as pd

from lcdash.db import get_conn
from lcdash.config import db_path

st.title("DB Status")
st.write(f"DB path: `{db_path()}`")

with get_conn() as conn:
    tables = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    ).fetchall()

table_names = [t["name"] for t in tables]
st.write("Tables found:", table_names)

if table_names:
    st.subheader("Row counts")
    counts = []
    with get_conn() as conn2:
        for name in table_names:
            if name.startswith("sqlite_"):
                continue
            n = conn2.execute(f"SELECT COUNT(*) AS n FROM {name}").fetchone()["n"]
            counts.append({"table": name, "rows": int(n)})

    st.dataframe(pd.DataFrame(counts), use_container_width=True, hide_index=True)

st.success("If you see problems/attempts/redo_schedule above, Day 1 is working.")
