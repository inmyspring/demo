import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 타이타닉 데이터 불러오기
titanic_data = pd.read_csv('./data/titanic.csv')

# 선택적으로 데이터 출력
if st.checkbox('Show Titanic Data'):
    st.write(titanic_data)

# 선택한 열이 숫자형일 경우에만 상관 계수 계산
numeric_columns = titanic_data.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = titanic_data[numeric_columns].corr()

# Streamlit app
st.title('타이타닉 데이터 상관 관계 시각화')

# heatmap으로 상관 계수 시각화
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
st.title('데이터 변수 간 상관 관계')
st.pyplot(fig)
