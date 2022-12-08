import streamlit as st
import pandas as pd
import requests
import os

st.header("Todos os valores cadastrados")

url = os.getenv("URL_BACKEND")
response = requests.get(url)
json = response.json()["data"]

df = pd.DataFrame(json)
df = df[["coordinates", "name"]]

new = df["coordinates"].str.split(",", n = 1, expand = True)
df["lat"] = float(new[0])
df["lon"] = float(new[1])

st.dataframe(df)
st.map(df)

st.button("refresh")
