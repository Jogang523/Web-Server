#실행
#streamlit run streamlit_0.py

import streamlit as st

# st.title('이것은 타이틀 입니다..' )
# st.title('스마일 	:100:')

# st.header('헤더 입니다 :smile:')
# st.subheader('서브헤더 입니다 :smile:')
# st.caption('캡션 입니다 :smile:')

sample_code="""
def function():
prtin('hello ,world')
"""

st.code(sample_code, language='python')
st.text('텍스트 입니다 :smile:')

# 마크다운
st.markdown(' **마크다운 입니다** :smile:')
st.markdown('텍스트의 색상을 :green[초록색]으로 그리고 "":blue[파란색]**볼드체로 설정')
st.markdown(':green[$\sqrt(x^2+y^2)=1$]')