# My Streamlit App

This is a sample project that shows the very basics of Streamlit: a simple app that connects to a PostgreSQL database and displays the rows from the `active` table in a live dataframe.

## Features

- Connects to PostgreSQL with SQLAlchemy
- Reads the active records into a pandas DataFrame
- Renders the data in a Streamlit table
- Refreshes the view automatically every 3 seconds with `st.fragment`

## Project structure

- `main.py` — app entry point and database query logic
- `pyproject.toml` — project metadata and dependencies

## Requirements

- Python 3.13+
- PostgreSQL database running and accessible
- Streamlit secrets configured for the database connection

## Setup

This project uses the dependencies declared in `pyproject.toml`.

Using `uv`:

```bash
uv sync
```

If you are not using `uv`, install the project dependencies with pip:

```bash
pip install .
```

## Database configuration

Create a `.streamlit/secrets.toml` file in the project root with the following structure:

```toml
[postgres]
host = "localhost"
port = 5432
user = "your_username"
password = "your_password"
dbname = "your_database"
```

The app expects a PostgreSQL table named `active` to exist.

## Run the app

With `uv`:

```bash
uv run streamlit run main.py
```

Or directly:

```bash
streamlit run main.py
```

The app will open a browser window and display the current rows from the `active` table.

## Notes

The database connection is cached with `@st.cache_resource`, and the data refreshes automatically every 3 seconds.
