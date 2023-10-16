# import the streamlit library 
import streamlit as st
import streamlit.components.v1 as components

st.header("CHURN DETECTOR", divider="rainbow")

region: str = st.selectbox(
    "SELECT REGION",
    ("", "FATICK", "DAKAR", "LOUGA", "TAMBACOUNDA", "KAOLACK",
     "THIES", "SAINT-LOUIS", "KOLDA", "KAFFRINE", "DIOURBEL",
     "ZIGUINCHOR", "MATAM", "SEDHIOU", "KEDOUGOU"))

tenure: str = st.selectbox("SELECT TENURE", ("", "K > 24 month", "I 18-21 month", 
        "G 12-15 month", "H 15-18 month",
       "J 21-24 month", "F 9-12 month", "D 3-6 month", "E 6-9 month"))

montant = st.number_input('MONTANT')
frequence_rech = st.number_input("FREQUENCE RECH")
revenue = st.number_input("REVENUE")
arpu_segment = st.number_input("ARPU SEGMENT")
frequence = st.number_input("FREQUENCE")
data_volume = st.number_input("DATA VOLUME")
on_net = st.number_input("ON NET")
orange = st.number_input("ORANGE")
tigo = st.number_input("TIGO")
zone1 = st.number_input("ZONE 1")
zone2 = st.number_input("ZONE 2")

mrg = st.radio("MRG: ", ("YES", "NO"))

from top_pack import options
top_pack = st.selectbox("TOP PACK", [""] + options)
