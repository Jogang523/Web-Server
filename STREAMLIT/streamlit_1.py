import streamlit as st
import pandas as pd
import numpy as np

st.title('데이터 프레임')

df = pd.DataFrame(
    {
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }
)

st.dataframe(df,use_container_width=True)

st.table(df)

st.metric(label='온도', value='10 C', delta='1.2 C')
st.metric(label='삼성전자',value='61,000 원',delta='1,200 원')

#화면 영역을 나누어서 표현
col1, col2, col3 = st.columns(3)
col1.metric(label='달러USD',value='1,228 원',delta='-12.00 원')
col2.metric(label='엔JPY',value='958.63 원',delta='-7.55 원')
col3.metric(label='유로EUR',value='1,335 원',delta='11.44 원')
