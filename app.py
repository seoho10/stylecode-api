import streamlit as st
import snowflake.connector
from datetime import datetime
import json

st.set_page_config(page_title="Stylecode Backend API", layout="wide")
st.title("Stylecode Backend API")

def get_conn():
    sf = st.secrets["snowflake"]
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

# --- API: A브랜드 12월 매출 예시 ---
# URL 예:
# https://<your-app>.streamlit.app/?brand=A&month=2025-12&token=YOUR_TOKEN
#
# 응답은 화면에 JSON으로 표시됩니다. (다음 단계에서 HTML이 이 JSON을 fetch로 가져갑니다)

TOKEN = st.secrets.get("API_TOKEN", "")  # 없으면 토큰검증 생략
q = st.query_params

brand = q.get("brand", "A")
month = q.get("month", "2025-12")
token = q.get("token", "")

if TOKEN and token != TOKEN:
    st.error("Unauthorized")
    st.stop()

# month -> start/end 계산 (YYYY-MM)
start_date = f"{month}-01"
# Snowflake에서 month의 마지막날 계산을 SQL로 처리해도 되지만, 일단 단순히 다음달-1을 쓰는 방식으로 구현
# 여기서는 Snowflake SQL로 end_date를 계산
sql = """
SELECT
  SUM(SALE_AMT) AS SALES_AMT
FROM PRCS.DW_SALE
WHERE BRD_CD = %(brand)s
  AND SALE_DT >= %(start_date)s
  AND SALE_DT < DATEADD(month, 1, %(start_date)s)
"""

cur = conn.cursor()
cur.execute(sql, {"brand": brand, "start_date": start_date})
sales = cur.fetchone()[0] or 0

payload = {
    "brand": brand,
    "month": month,
    "sales_amt": float(sales),
    "generated_at": datetime.now().isoformat(timespec="seconds"),
}

st.json(payload)
