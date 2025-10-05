import streamlit as st
import joblib
import os
import pandas as pd
from recommend import top_n_for_user

BASE = os.path.join(os.path.dirname(__file__), "..")
MODEL_FILE = os.path.join(BASE, "model_joblib.pkl")
DATA_DIR = os.path.join(BASE, "data", "ml-100k")
MOVIES_FILE = os.path.join(DATA_DIR, "u.item")

st.title("Mini Recommender Demo")

st.write("Enter an existing MovieLens user id (1–943) to get top recommendations.")

user_id = st.text_input("User id", value="1")
n = st.slider("How many recommendations?", 1, 20, 10)

if st.button("Recommend"):
    try:
        recs = top_n_for_user(user_id, n)
        st.write(f"Top {n} recommendations for user {user_id}:")
        for title,score in recs:
            st.write(f"- **{title}** (pred: {score:.2f})")
    except Exception as e:
        st.error(str(e))
