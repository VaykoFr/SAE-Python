import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import datetime

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


st.header("Feuille Tikcet du fichier excel")
st.dataframe(df_ticket)
st.header("Feuille Détail Ticket du fichier Excel")
st.dataframe(df_detail_ticket)
st.header("Feuille Produit en Rayon du fichier Excel")
st.dataframe(df_produit_en_rayon)
st.header("Feuille Carte Fidélité du fichier Excel")
st.dataframe(df_carte_fidelite)





pie_caisses = px.pie(df_ticket,
                     title='Camembert des caisses les plus utilisés',
                     values='Caisse',
                     names='Caisse')

st.plotly_chart(pie_caisses)

date_default = datetime.date(2021, 1, 1)
date_min = datetime.date(2021, 1, 1)
date_max = datetime.date(2021, 10, 31)

#Afficher le calendrier 

date_user = st.date_input(label ="Choisissez une date pour plus de détails", 
              value=date_default, 
              min_value=date_min,
              max_value=date_max, 
              key=None, 
              help=None, 
              on_change=None, 
              args=None, kwargs=None, 
              disabled=False, 
             label_visibility="visible")

# Récupérer la date choisie par l'utilisateur
df_ticket['DateH_Ticket'] = pd.to_datetime(df_ticket['DateH_Ticket'], format='%d/%m/%Y %H:%M:%S')
df_filtered = df_ticket[df_ticket['DateH_Ticket'].dt.date == date_user]

if df_filtered.empty:
    st.write(f"Il n'y a aucun ticket pour la date choisie : {date_user}")
else:
    # Grouper les tickets par caisse et compter le nombre de tickets pour chaque caisse
    df_grouped = df_filtered.groupby(['Caisse']).agg({'No_Ticket': 'count'}).reset_index()

    # Trier les caisses par ordre décroissant du nombre de tickets
    df_sorted = df_grouped.sort_values(by='No_Ticket', ascending=False)

    # Sélectionner les 10 caisses les plus utilisées
    df_top_10 = df_sorted.head(10)

    # Afficher le camembert
    pie_caisses = px.pie(df_top_10,
                         title=f'Caisses les plus utilisées le {date_user}',
                         values='No_Ticket',
                         names='Caisse')
    st.plotly_chart(pie_caisses)



