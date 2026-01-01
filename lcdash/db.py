import sqlite3
from contextlib import contextmanager
from pathlib import Path

import streamlit as st
from lcdash.config import db_path

SCHEMA_FILE = str(Path.cwd() / "schema.sql")

def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(db_path(), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

@contextmanager
def get_conn():
    conn = _connect()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def init_db() -> None:
    if st.session_state.get("_db_initialized"):
        return

    with get_conn() as conn:
        with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
            conn.executescript(f.read())

    st.session_state["_db_initialized"] = True
