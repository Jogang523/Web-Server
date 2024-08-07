import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt

button=st.button('press btuuon')

if button:
    st.write('버튼이 눌렸습니다')

df=pd.DataFrame({
    'first': [1, 2, 3, 4],
    'second': [10, 20, 30, 40]
})

st.dataframe(df,use_container_width=True)

st.download_button(
    label='csv로 다운로드',
    data=df.to_csv(),
    file_name='sample.csv',
    mime='text/csv')

agree=st.checkbox('체크박스')

if agree:
    st.write('동의합니다')

#라디오 버튼

mbti = st.radio(
    '당신의 MBTI 유형은?',
    ('ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP')
)

if mbti == 'ISTJ':
    st.write('당신은 논리적이고 현실적인 사람입니다.')
if mbti == 'ISFJ':
    st.write('당신은 현실적이고 현실적인 사람입니다.')
if mbti == 'INFJ':
    st.write('당신은 이상적이고 현실적인 사람입니다.')
if mbti == 'INTJ':
    st.write('당신은 논리적이고 현실적인 사람입니다.')
if mbti == 'ISTP': 
    st.write('당신은 논리적이고 현실적인 사람입니다.')

# 다중 선택
options = st.multiselect(
    '당신이 좋아하는 과일은?',
    ['사과', '바나나', '수박', '딸기']
)
st.write('당신이 좋아하는 과일은:', options)


#텍스트 입력

title = st.text_input(
    label='가고싶은 여행지는?',
    placeholder='여행지를 입력하세요'
)
st.write(f"당신이 입력한 여행지는 {title} 입니다.")

#숫자 입력

number = st.number_input(
    label='당신의 나이는?',
    min_value=10,
    max_value=130,
    value=30,
    step=1
)
st.write('당신이 입력한 숫자는: ', number)

#슬라이더

value = st.slider(
    '범위의 값을 다음과 같이 지정할 수 있어요',
    0.0,100.0,(25.0,75.0)
)
st.write('범위 값은:', value)


# 시간 구간 슬라이더
import datetime as dt
start_time = st.slider(
    '언제 약속을 시작할까요?',
    min_value=dt.datetime(2020,1,1,0,0),
    max_value=dt.datetime(2020,12,31,10,0),
    value= dt.datetime(2020,6,15,0,0),
    format='MM/DD/YY - hh:mm'
)

st.write('약속 시작 시간은:', start_time)