import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Global Air Pollution", layout="wide")

st.title("🌍 전세계 대기 오염 데이터 대시보드")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("global_air_pollution_dataset.csv")
        return df
    except Exception as e:
        st.error(f"데이터를 불러오는 중 오류 발생: {e}")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.stop()

# 오염 물질별 컬럼 매핑
pollutants = {
    "전체 AQI": "AQI Value",
    "CO": "CO AQI Value",
    "Ozone": "Ozone AQI Value",
    "NO2": "NO2 AQI Value",
    "PM2.5": "PM2.5 AQI Value"
}

# 사이드바 필터
with st.sidebar:
    st.header("🔍 필터 선택")
    pollutant_display = st.selectbox("오염 물질 선택", list(pollutants.keys()))
    pollutant_column = pollutants[pollutant_display]

# 선택된 오염물질 기준 국가별 평균
df_clean = df.dropna(subset=[pollutant_column])

avg_by_country = (
    df_clean.groupby("Country")[pollutant_column]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

# 상위 20개국 시각화
top_n = st.slider("상위 국가 수 선택", 5, 30, 20)

st.subheader(f"📊 국가별 평균 {pollutant_display} (상위 {top_n}개국)")

fig = px.bar(
    avg_by_country.head(top_n),
    x="Country",
    y=pollutant_column,
    color=pollutant_column,
    color_continuous_scale="Reds",
    title=f"{pollutant_display} 평균 AQI 상위 국가"
)

st.plotly_chart(fig, use_container_width=True)

# 데이터 미리보기
with st.expander("📄 원본 데이터 보기"):
    st.dataframe(df.head(100))
