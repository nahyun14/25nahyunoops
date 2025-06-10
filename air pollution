import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터셋 로드
@st.cache
def load_data():
    url = "https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india/download"
    data = pd.read_csv(url)
    return data

df = load_data()

# 제목
st.title("🌍 전 세계 대기질 정보")

# 국가 선택
country = st.selectbox("국가를 선택하세요", df['Country'].unique())

# 도시 선택
city = st.selectbox("도시를 선택하세요", df[df['Country'] == country]['City'].unique())

# 선택한 도시의 데이터 필터링
city_data = df[(df['Country'] == country) & (df['City'] == city)]

# 대기질 지수(AQI) 시각화
st.subheader(f"{city}의 대기질 지수(AQI)")
fig = px.bar(city_data, x='Date', y='AQI Value', title=f"{city}의 AQI 변화")
st.plotly_chart(fig)

# 주요 오염 물질 농도 시각화
st.subheader(f"{city}의 주요 오염 물질 농도")
fig2 = px.line(city_data, x='Date', y=['PM2.5', 'CO', 'Ozone', 'NO2'], title=f"{city}의 오염 물질 농도 변화")
st.plotly_chart(fig2)

# 대기질 카테고리 분포
st.subheader(f"{city}의 대기질 카테고리 분포")
fig3 = px.pie(city_data, names='AQI Category', title=f"{city}의 대기질 카테고리 분포")
st.plotly_chart(fig3)

