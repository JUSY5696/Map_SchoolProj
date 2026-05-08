import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

st.set_page_config(page_title="NDHS Maps")
for i in range(10) :
  print('*' * (i+1))
st.header("NDHS Maps")
