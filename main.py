import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

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

df = pd.read_csv('인천광역시 남동구_고등학교_20240325.csv', encoding='cp949')
df_latlon = df[['위도', '경도']]
df_latlon = df_latlon.rename(columns={'위도' : 'lat', '경도' : "lon"})
st.map(df_latlon)
