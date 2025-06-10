
import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv('global_air_pollution_dataset.csv')
    return df

df = load_data()

st.title("🌍 전 세계 대기질 정보")

country = st.selectbox("국가를 선택하세요", df['Country'].unique())
city = st.selectbox("도시를 선택하세요", df[df['Country'] == country]['City'].unique())
city_data = df[(df['Country'] == country) & (df['City'] == city)]

st.subheader(f"{city}의 대기질 지수(AQI)")
fig = px.bar(city_data, x='Date', y='AQI Value', title=f"{city}의 AQI 변화")
st.plotly_chart(fig)

st.subheader(f"{city}의 주요 오염 물질 농도")
fig2 = px.line(city_data, x='Date', y=['PM2.5', 'CO', 'Ozone', 'NO2'], title=f"{city}의 오염 물질 농도 변화")
st.plotly_chart(fig2)

st.subheader(f"{city}의 대기질 카테고리 분포")
fig3 = px.pie(city_data, names='AQI Category', title=f"{city}의 대기질 카테고리 분포")
st.plotly_chart(fig3)
