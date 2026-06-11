import streamlit as st

st.set_page_config(page_title="EcoVision AI", page_icon="🌍", layout="centered")

# -----------------------------
# EcoVision AI Branding Header
# -----------------------------
st.title("🌍 EcoVision AI")
st.subheader("Smart Waste & Sustainable Consumption Assistant")
st.caption("Aligned with SDG 12 – Responsible Consumption and Production")

tabs = st.tabs(["♻️ Waste Categorization Tool", "🛍️ Sustainable Consumption Tracker"])

# -----------------------------
# 1. WASTE CATEGORIZATION TOOL
# -----------------------------
with tabs[0]:
    st.header("♻️ Waste Categorization Tool")

    waste_item = st.selectbox(
        "Select a waste item:",
        [
            "Plastic Bottle",
            "Paper Sheet",
            "Banana Peel",
            "Aluminum Can",
            "Glass Jar"
        ]
    )

    waste_map = {
        "Plastic Bottle": ("Plastic", "Recycling Bin ♻️"),
        "Paper Sheet": ("Paper", "Recycling Bin ♻️"),
        "Banana Peel": ("Organic", "Compost Bin 🌱"),
        "Aluminum Can": ("Metal", "Recycling Bin ♻️"),
        "Glass Jar": ("Glass", "Recycling Bin ♻️")
    }

    if st.button("Classify Waste"):
        category, disposal = waste_map[waste_item]

        st.success(f"Category: {category}")
        st.info(f"Recommended Disposal: {disposal}")

        st.balloons()
        st.write("💡 Tip: Proper segregation reduces landfill waste and supports circular economy.")

# -----------------------------
# 2. SUSTAINABLE CONSUMPTION TRACKER
# -----------------------------
with tabs[1]:
    st.header("🛍️ Sustainable Consumption Tracker")

    product = st.selectbox(
        "Select a common purchase:",
        [
            "Plastic Water Bottle",
            "Disposable Cup",
            "Notebook",
            "Reusable Bottle",
            "Cloth Bag"
        ]
    )

    eco_map = {
        "Plastic Water Bottle": "Switch to a reusable steel or glass bottle 💧",
        "Disposable Cup": "Use a reusable ceramic or steel cup ☕",
        "Notebook": "Choose recycled paper notebooks 📓",
        "Reusable Bottle": "Great choice! Keep using it 👍🌱",
        "Cloth Bag": "Excellent! Helps reduce plastic waste 🛍️🌿"
    }

    if st.button("Evaluate Choice"):
        suggestion = eco_map[product]

        if "Great" in suggestion or "Excellent" in suggestion:
            st.success(suggestion)
        else:
            st.warning(suggestion)

        st.write("🌍 Every small choice contributes to a sustainable future!")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("**EcoVision AI • Techno India University • Semester 6 Project • SDG 12**")
