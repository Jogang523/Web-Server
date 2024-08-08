import streamlit as st
import FinanceDataReader as fdr
import datetime
import time

st.title('종목 차트 검색')

with st.sidebar:
    date = st.date_input(
        '조회 시작일을 선택해 주세요',
        datetime.datetime(2022,1,1)
    )

    code = st.text_input(
        '종목코드',
        value='',
        placeholder='종목코드를 입력하세요'
    )

if code and date:
    df = fdr.DataReader(code,date)
    data = df.sort_index(ascending=True).loc[:,'Close']

    tab1,tab2 = st.tabs(['차트','데이터'])

    with tab1:
        st.line_chart(data)
    
    with tab2:
        st.dataframe(df.sort_index(ascending=True))

    with st.expander('칼럼설명'):
        st.markdown('''
        - Open : 시가
        - High : 고가
        - Low : 저가
        - Close : 종가
        - Adj Close : 수정종가
        - Volume : 거래량
        ''')    