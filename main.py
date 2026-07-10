import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

#streamlit text styling
st.set_page_config(page_title="NDHS Maps", layout="wide")

st.title("NDHS Maps")
st.markdown("## 2026 NDHS Hiking Event Guide Map")

st.markdown("# big title")
st.markdown("## small title")
st.markdown("**Bold**")
st.markdown("*Italic*")

st.header("Header")
st.subheader("Subheader")
st.caption("Caption")
st.code("for i in range(5) : \n  print('*' * (i + 1))")
st.code("* \n** \n*** \n**** \n*****")

#read data(CSV)
#df = pd.read_csv('인천광역시 남동구_고등학교_20240325.csv', encoding='cp949')
df = pd.read_csv('등산경로.csv', encoding='utf-8')
#st.map(df_latlon)

#Maps with Marker(Map Visualization Step)
m = folium.Map(
    location = [37.40583317, 126.7214872],
    zoom_start = 20
  )
for i in range(len(df)) :
    folium.Marker(
        location = [df.iloc[i]['위도'], df.iloc[i]['경도']],
        popup = f'<div style="width:300px"> <strong>{df.iloc[i]['위치명']}</strong> </div>',
        icon = folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

#output
col1, col2 = st.columns([3,1])

with col1 :
    st_folium(m, width=1920, height=600)

with col2 :
    st.subheader("정보")
    st.info("길이 미끄럽습니다. 주의하세요.")
    st.metric(label="소요시간", value="10분")
    st.write("주의사항 : 등산화를 착용하세요.")
