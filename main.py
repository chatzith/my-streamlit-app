"""Streamlit app for viewing the current active database records."""

import pandas as pd
import streamlit as st
from sqlalchemy import create_engine, text


@st.cache_resource
def get_db_engine():
    """Create and cache the SQLAlchemy engine used to access the app database."""
    secrets = st.secrets["postgres"]
    url = f"postgresql+psycopg2://{secrets['user']}:{secrets['password']}@{secrets['host']}:{secrets['port']}/{secrets['dbname']}"
    return create_engine(url, pool_size=10, max_overflow=20, pool_pre_ping=True)


def fetch_users(search_term: str | None = None) -> pd.DataFrame:
    """Fetch rows from the active table, optionally filtering by a search term.

    Args:
        search_term: Optional text used to match rows in the active dataset.

    Returns:
        A pandas DataFrame containing the current active records.
    """
    engine = get_db_engine()
    query = text("SELECT * FROM active")

    with engine.connect() as conn:
        df = pd.read_sql(query, conn, params={"search": f"%{search_term or ''}%"})
    return df


@st.fragment(run_every=3)
def entries():
    """Render the latest active records in a refreshable Streamlit dataframe."""
    st.dataframe(fetch_users(), use_container_width=True)


entries()
