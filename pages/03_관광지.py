
import streamlit as st
import folium
from folium import plugins
from folium.plugins import MarkerCluster

# 서울 주요 관광지 Top 10 좌표 (위도, 경도)
locations = [
    {"name": "경복궁", "lat": 37.5778, "lon": 126.9769},
    {"name": "N서울타워", "lat": 37.5512, "lon": 126.9882},
    {"name": "명동", "lat": 37.5631, "lon": 126.9882},
    {"name": "북촌한옥마을", "lat": 37.5824, "lon": 126.9857},
    {"name": "인사동", "lat": 37.5740, "lon": 126.9896},
    {"name": "청계천", "lat": 37.5706, "lon": 126.9770},
    {"name": "롯데월드타워", "lat": 37.5123, "lon": 127.1021},
    {"name": "동대문디자인플라자(DDP)", "lat": 37.5660, "lon": 127.0098},
    {"name": "서울숲", "lat": 37.5444, "lon": 127.0390},
    {"name": "한강공원", "lat": 37.5200, "lon": 126.9430}
]

# 서울의 중심을 기준으로 맵을 초기화
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

# 관광지에 마커와 폴리곤 추가
for loc in locations:
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=loc["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

    # 폴리움 - 각 관광지 주변에 원형 폴리곤 추가
    folium.Circle(
        location=[loc["lat"], loc["lon"]],
        radius=300,  # 반경 300m
        color='crimson',
        fill=True,
        fill_color='crimson',
        fill_opacity=0.2
    ).add_to(m)

# 스트림릿 앱에 지도 표시
st.title("서울 주요 관광지 Top 10")
st.markdown("서울의 인기 관광지들을 폴리움으로 표시한 지도입니다.")
st.folium_map(m)

