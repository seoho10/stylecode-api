import streamlit as st
import snowflake.connector
ECHO�� �����Ǿ� �ֽ��ϴ�.
st.title("Stylecode Backend API")
ECHO�� �����Ǿ� �ֽ��ϴ�.
def get_conn():
    return snowflake.connector.connect()
        account=st.secrets["SNOWFLAKE_ACCOUNT"],
        user=st.secrets["SNOWFLAKE_USER"],
        password=st.secrets["SNOWFLAKE_PASSWORD"],
        warehouse=st.secrets["SNOWFLAKE_WAREHOUSE"],
        database=st.secrets["SNOWFLAKE_DATABASE"],
        schema=st.secrets["SNOWFLAKE_SCHEMA"],
    )
ECHO�� �����Ǿ� �ֽ��ϴ�.
conn = get_conn()
cur = conn.cursor()
cur.execute("SELECT CURRENT_TIMESTAMP()")
result = cur.fetchone()[0]
ECHO�� �����Ǿ� �ֽ��ϴ�.
st.success(f"Snowflake Connected OK : {result}")
 