# 📈 Bitcoin Price Prediction with TensorFlow Decision Forests

Cette application Streamlit utilise l'apprentissage automatique pour prédire le prix du Bitcoin à partir d'un jeu de données historiques.

## 🚀 Aperçu

- 📊 **Modèle** : TensorFlow Decision Forests (`RandomForestModel`)
- 📁 **Données** : Fichier CSV contenant l'historique des prix (`data/main.csv`)
- 💻 **Interface** : Application Streamlit avec visualisations et prédictions
- ☁️ **Déploiement** : Streamlit Cloud

---

## 📷 Capture d'écran

<img src="https://your-screenshot-url" alt="Aperçu de l'application" width="800">

---

## ⚙️ Fonctionnalités

- Chargement dynamique des données
- Entraînement du modèle (ou chargement depuis un dossier `models/`)
- Évaluation du modèle (MSE, RMSE, etc.)
- Visualisation des prédictions vs les valeurs réelles
- Interface interactive avec `st.slider` pour tester les prédictions

---

## 🧪 Démarrage rapide

### 1. Cloner le projet

```bash
git clone https://github.com/phil5911/bitcoin-price-prediction.git
cd bitcoin-price-prediction
