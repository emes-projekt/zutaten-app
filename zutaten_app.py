import streamlit as st
import pandas as pd

# Titel
st.title("📋 Zutaten-Such-App")

# Excel-Datei direkt einlesen
@st.cache_data
def lade_daten():
    return pd.read_excel("Liste.xlsx")

df = lade_daten()

# Suchfeld
search_term = st.text_input("🔍 Suche nach Bezeichnung")

# Ergebnis filtern
if search_term:
    filtered_df = df[df["Bezeichnung"].str.contains(search_term, case=False, na=False)]
else:
    filtered_df = df

# Ergebnisse anzeigen
st.write(f"🔎 Gefundene Einträge: {len(filtered_df)}")
st.dataframe(filtered_df)

# Optional: Download-Button für gefilterte Daten
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("📥 Gefilterte Daten herunterladen", csv, "gefiltert.csv", "text/csv")
