import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="Global Air Pollution Dashboard", layout="wide")

# 제목
st.title("🌍 전세계 대기 오염 정도 시각화")

# 데이터 불러오기
@st.cache_data
def load_data():
    return pd.read_csv("global_air_pollution_dataset.csv")

df = load_data()

# 기본 정보 확인
st.subheader("데이터 미리보기")
st.dataframe(df.head())

# 컬럼 확인
st.markdown("**📌 사용 가능한 컬럼:**")
st.write(df.columns.tolist())

# 필요한 컬럼 예시: Country, City, Latitude, Longitude, PM2.5, PM10, Year 등

# 필터
with st.sidebar:
    st.header("🔍 필터 설정")
    year = st.selectbox("년도 선택", sorted(df["Year"].unique(), reverse=True))
    pollutant = st.selectbox("대기오염 물질 선택", ["PM2.5", "PM10", "NO2", "O3", "CO"] if set(["PM2.5", "PM10", "NO2", "O3", "CO"]).intersection(df.columns) else df.columns)

# 선택한 연도 기준 필터링
filtered_df = df[df["Year"] == year]

# 지도 시각화
st.subheader(f"🗺️ {year}년도 {pollutant} 농도 지도")
fig = px.scatter_geo(
    filtered_df,
    lat="Latitude",
    lon="Longitude",
    color=pollutant,
    size=pollutant,
    hover_name="City",
    projection="natural earth",
    color_continuous_scale="OrRd",
    title=f"{year}년 세계 {pollutant} 오염 수준"
)
st.plotly_chart(fig, use_container_width=True)

# 국가별 평균 오염도 막대 그래프
st.subheader(f"📊 국가별 평균 {pollutant} 농도")
avg_pollution = filtered_df.groupby("Country")[pollutant].mean().sort_values(ascending=False).head(20)
st.bar_chart(avg_pollution)

# 참고 정보
st.markdown("---")
st.caption("데이터 출처: global_air_pollution_dataset.csv")
