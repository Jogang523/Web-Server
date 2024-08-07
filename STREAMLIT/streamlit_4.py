import streamlit as st
import FinanceDataReader as fdr
import datetime

date = st.date_input(
    '조회할 시작일을 선택해 주세요',
    datetime.datetime(2022,1,1)
)

code = st.text_input(
    '종목코드',
    value='',
    placeholder='종목코드를 입력하세요'
)

if code and date:
    df = fdr.DataReader(code,date)
    data = df.sort_index(ascending=False).loc[:,'Close']
    st.line_chart(data)