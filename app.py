import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Chargement des données
df = pd.read_csv("data/sample.csv")

# Entraînement d'un modèle simple
model = LinearRegression()
model.fit(df[["x"]], df["y"])

# Interface utilisateur
st.title("Mini modèle de régression linéaire")
st.write("Données utilisées :", df)

# Saisie utilisateur
val = st.number_input("Entrer une valeur de x", min_value=0.0, value=1.0)
pred = model.predict([[val]])[0]

st.success(f"Prédiction pour x = {val} : y = {pred:.2f}")

# Affichage graphique
fig, ax = plt.subplots()
ax.scatter(df["x"], df["y"], label="Données")
ax.plot(df["x"], model.predict(df[["x"]]), color='red', label="Modèle")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)
