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
df_latlon = df[['위도', '경도']]
df_latlon = df_latlon.rename(columns={'위도' : 'lat', '경도' : "lon"})
#st.map(df_latlon)

#Maps with Marker(Map Visualization Step)
m = folium.Map(
    location=[37.40583317, 126.7214872],
    zoom_start=12
  )

folium.Marker(
    location = [37.40583317, 126.7214872],
    tooltip = "Click Here",
    popup = "NDHS",
    icon = folium.Icon(color='blue', icon='info-sign')
).add_to(m)

#output
st_folium(m, width=1000, height=500)
