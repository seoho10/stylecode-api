import streamlit as st
import snowflake.connector

st.title("Stylecode Backend API")

def get_conn():
    sf = st.secrets["snowflake"]  # [snowflake] 섹션
    return snowflake.connector.connect(
        account=sf["account"],
        user=sf["user"],
        password=sf["password"],
        warehouse=sf["warehouse"],
        database=sf["database"],
        schema=sf["schema"],
        role=sf.get("role"),
    )


conn = get_conn()
cur = conn.cursor()

cur.execute("SELECT CURRENT_TIMESTAMP()")
result = cur.fetchone()[0]

st.success(f"Snowflake Connected OK : {result}")
