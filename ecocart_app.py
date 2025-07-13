import streamlit as st
import pandas as pd

# Load product data
df = pd.read_csv("ecocart_products.csv")

# Set up app
st.set_page_config(page_title="EcoCart", page_icon="🌿")
st.title("🛒 EcoCart - Make Greener Shopping Choices")
st.write("Type a product name to check its eco-score and discover greener alternatives.")

# User input
product_input = st.text_input("Enter product name (e.g. shampoo bottle):")

if product_input:
    product = product_input.lower().strip()
    match = df[df["Product"].str.lower().str.contains(product)]

    if not match.empty:
        row = match.iloc[0]
        st.subheader(f"🌍 Eco Score: {row['Eco_Score']} / 5")
        st.write("🔴 Issues:", row["Issues"])
        st.success("✅ Greener Alternative: " + row["Alternative"])
        st.info(f"💨 Estimated Carbon Footprint: {row['Carbon_Footprint']} kg CO₂e")
    else:
        st.warning("❗ Product not found in our list.")
