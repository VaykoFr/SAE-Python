import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Analyse des données ticket')
st.header('Bienvenu sur ma page de statistique')
st.subheader('Vous trouverez ci dessous les stats pour la SAE BD')

### --- LOAD DATAFRAME

excel_file = 'Ticket.xlsx'
sheet_ticket = 'Ticket'
sheet_detail_ticket = 'DetailTicket'
sheet_produit_en_rayon = 'ProduitEnRayon'
sheet_carte_fidelite ='CarteFidelite'

df_ticket = pd.read_excel(excel_file,
                                sheet_name=sheet_ticket,
                                usecols='A:D',
                                header=0)

df_detail_ticket = pd.read_excel(excel_file,
                                 sheet_name=sheet_detail_ticket,
                                 usecols='A:E',
                                 header=0)

df_produit_en_rayon = pd.read_excel(excel_file,
                                    sheet_name=sheet_produit_en_rayon,
                                    usecols='A:P',
                                    header=0)

df_carte_fidelite = pd.read_excel(excel_file,
                                  sheet_name=sheet_carte_fidelite,
                                  usecols='A:M',
                                  header=0)

st.dataframe(df_ticket)
st.dataframe(df_detail_ticket)
st.dataframe(df_produit_en_rayon)
st.dataframe(df_carte_fidelite)





pie_caisses = px.pie(df_ticket,
                     title='Camembert des caisses les plus utilisés',
                     values='Caisse',
                     names='Caisse')

st.plotly_chart(pie_caisses)

