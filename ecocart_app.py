
import streamlit as st
import pandas as pd

# Load product data
df = pd.read_csv("ecocart_products.csv")

st.set_page_config(page_title="EcoCart", page_icon="🌿")
st.title("🛒 EcoCart - Make Greener Shopping Choices")
st.write("Type a product name to check its eco-score and discover greener alternatives.")

product_input = st.text_input("Enter product name:")

if product_input:
    product = product_input.lower().strip()
    match = df[df["Product"].str.lower() == product]

    if not match.empty:
        row = match.iloc[0]
        st.subheader(f"🌍 Eco Score: {row['Eco_Score']} / 5")
        st.write("🔴 Issues:", row["Issues"])
        st.success("✅ Greener Alternative: " + row["Alternative"])
    else:
        st.warning("❗ Product not found in our list.")
