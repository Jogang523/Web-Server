import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame(
    {
    '이름':['영식','철수','영희'],
    '나이':[22,31,25],
    '모음계':[75.5,80.2,55.1]
}
)

#matplotlib
fig,ax=plt.subplots()
ax.bar(df['이름'],df['나이'])

st.pyplot(fig)

#seaborn
barplot = sns.barplot(x='이름',y='나이',data=df,ax=ax,palette='Set2')
fig = barplot.get_figure()

st.pyplot(fig)