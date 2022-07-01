import pandas as pd
import plotly.express as px
import json
import pickle
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from pyvis.network import Network
import re
import seaborn as sns
from typing_extensions import Literal, TypedDict
import streamlit as st
pd.set_option("display.max_columns", 32)


df_apbd = pd.read_excel("belanja_apbd_full.xlsx")
df_lokasi = pd.read_csv("daftar-nama-daerah.csv") 
df_lokasi = df_lokasi.rename(columns = {'name':'nama_pemda'})
data = pd.merge(df_lokasi,df_apbd,on= 'nama_pemda')
df_data = data.copy()
df_data = df_data.drop(['parent_nid','serial','type','No'],axis=1)
fig = px.scatter_mapbox(df_data, lat="latitude", lon="longitude", size="Target_IPM", color="Target_IPM",
                  color_continuous_scale=px.colors.sequential.YlGn, size_max=12,zoom=2.5,hover_name="nama_pemda")
fig.update_layout(mapbox_style="open-street-map")

st.title("Peta Target IPM per Wilayah di Indonesia")
st.plotly_chart(fig)
