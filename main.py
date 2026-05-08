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
df = pd.read_csv('인천광역시 남동구_고등학교_20240325.csv', encoding='cp949')
#st.map(df_latlon)

#Maps with Marker(Map Visualization Step)
m = folium.Map(
    location = [37.40583317, 126.7214872],
    zoom_start = 12
  )
for i in range(len(df)) :
    homepage = f'{df.iloc[i]['홈페이지']}'
    folium.Marker(
        location = [df.iloc[i]['위도'], df.iloc[i]['경도']],
        popup = f'<div style="width:200px"> <strong>{df.iloc[i]['학교명']}</strong> <br> Homepage : <a href="{homepage}">{homepage}</a> <br> Phone : {school.iloc[i]['연락처']}</div>',
        icon = folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

#output
st_folium(m, width=1000, height=500)
