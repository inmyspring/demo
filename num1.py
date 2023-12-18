import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# 타이타닉 데이터 불러오기
titanic_data = pd.read_csv('./data/titanic.csv')

numeric_columns = titanic_data.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = titanic_data[numeric_columns].corr()

st.title('타이타닉 데이터 상관 관계 시각화')

plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('데이터 변수 간 상관 관계')

st.pyplot()

st.markdown('이 히트맵은 타이타닉 데이터의 숫자형 변수 간 상관 관계를 보여줍니다.')
