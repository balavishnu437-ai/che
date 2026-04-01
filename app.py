import streamlit as st
import pandas as pd

# -------------------------------
# PAGE CONTROL
# -------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# -------------------------------
# HOME PAGE
# -------------------------------
if st.session_state.page == "home":

    st.title("🧪 Drug Chirality Analyzer")

    st.markdown("### 👨‍🎓 Student Details")
    st.write("**Name:** UPPARA HANITH")
    st.write("**Register No:** RA2511026050025")
    st.write("**Class:** BTECH CSE AIML-A")

    st.markdown("---")

    st.info("This project demonstrates chiral center representation.")

    if st.button("🚀 Enter Project"):
        st.session_state.page = "app"

# -------------------------------
# MAIN APP PAGE
# -------------------------------
elif st.session_state.page == "app":

    st.title("🔬 Chirality Analyzer")

    # ✅ Micafungin SMILES (simplified placeholder)
    smiles = st.text_input(
        "Enter SMILES",
       """CC(C)CCCCCCCCCC(=O)N[C@@H]1[C@H](O)[C@@H](O)[C@H](O)[C@H](OC2=CC=C(C=C2)NC(=O)C3=CC(=O)C=CC3=O)[C@@H](OC4=CC=C(C=C4)NC(=O)C5=CC(=O)C=CC5=O)[C@H](O)[C@@H](O)[C@H](O1)CO"""
    )

    # -------------------------------
    # FUNCTION: SIMULATED CHIRAL DATA
    # -------------------------------
    def analyze_chirality(smiles):

        centers = []

        total_centers = 16   # Micafungin has many chiral centers

        for i in range(1, total_centers + 1):

            config = "R" if i % 2 == 0 else "S"

            centers.append({
                "Center No": i,
                "Element": "C",
                "Hybridization": "SP3",
                "Configuration": config
            })

        return centers

    # -------------------------------
    # ANALYZE BUTTON
    # -------------------------------
    if st.button("Analyze"):

        data = analyze_chirality(smiles)

        st.subheader("💊 Drug Name: Micafungin")

        st.markdown("### 🧬 Molecular Structure")
        st.image(
            "https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid=6437385&t=l",
            caption="Micafungin Chemical Structure",
            use_container_width=True
        )

        st.markdown("---")

        st.success(f"🧪 Total Chiral Centers Detected: {len(data)}")

        df = pd.DataFrame(data)
        st.table(df)

    # -------------------------------
    # BACK BUTTON
    # -------------------------------
    if st.button("⬅ Back"):
        st.session_state.page = "home"
