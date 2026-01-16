import streamlit as st
import snowflake.connector
ECHO가 설정되어 있습니다.
st.title("Stylecode Backend API")
ECHO가 설정되어 있습니다.
def get_conn():
    return snowflake.connector.connect()
        account=st.secrets["SNOWFLAKE_ACCOUNT"],
        user=st.secrets["SNOWFLAKE_USER"],
        password=st.secrets["SNOWFLAKE_PASSWORD"],
        warehouse=st.secrets["SNOWFLAKE_WAREHOUSE"],
        database=st.secrets["SNOWFLAKE_DATABASE"],
        schema=st.secrets["SNOWFLAKE_SCHEMA"],
    )
ECHO가 설정되어 있습니다.
conn = get_conn()
cur = conn.cursor()
cur.execute("SELECT CURRENT_TIMESTAMP()")
result = cur.fetchone()[0]
ECHO가 설정되어 있습니다.
st.success(f"Snowflake Connected OK : {result}")
