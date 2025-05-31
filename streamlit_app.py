# streamlit_app.py
import streamlit as st
from PIL import Image

# --- Configuration ---
st.set_page_config(page_title="Akash Somasekharan", layout="wide")

# --- Sidebar Navigation ---
menu = st.sidebar.radio("Navigation", ["Home", "Research", "Projects", "Blog", "CV"])

# --- Home Page ---
if menu == "Home":
    st.title("👋 Hi, I'm Akash Somasekharan")
    st.write("""
    Ph.D. candidate in Physical Oceanography, passionate about climate-ocean interactions,
    OMZ dynamics, and applying AI in marine science.
    """)
    
    st.subheader("About Me")
    st.markdown("""
    I work on biogeochemical modeling, ocean transports, and data-driven analysis of the Arabian Sea OMZ.
    This site showcases my work, research, blogs, and tools.
    """)

# --- Research Page ---
elif menu == "Research":
    st.title("🔬 Research")
    st.write("Current focus:")
    st.markdown("""
    - Seasonal/interannual OMZ variability in the Arabian Sea
    - Zonal and meridional transport analysis (HYCOM-ECOSMO)
    - Scalar transport of oxygen, detritus, nitrate across regional boundaries
    - Application of ML models (e.g., XGBoost, GAM) in catch/OMZ prediction
    """)

# --- Projects Page ---
elif menu == "Projects":
    st.title("📁 Projects")
    st.markdown("""
    - `argohycom-toolbox`: Python module for BGC-Argo and HYCOM colocation
    - Ocean Transport Estimator: Zonal/meridional transport computation
    - DSL Depth Estimator: Python tool for DSL + OMZ mapping
    - Water Quality Stats Tool: Panchayat-level statistical analysis dashboard
    """)

# --- Blog Page ---
elif menu == "Blog":
    st.title("✍️ Blog")
    st.markdown("""
    **Coming Soon!**
    I'll be sharing insights, tutorials, and research notes on:
    - OMZ science and data analysis
    - Machine learning workflows
    - Remote sensing and cruise survey learnings
    """)

# --- CV Page ---
elif menu == "CV":
    st.title("📄 Curriculum Vitae")
    with open("resume.pdf", "rb") as file:
        st.download_button("Download My CV", file.read(), file_name="Akash_Somasekharan_CV.pdf")

    st.write("You can also connect with me on:")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/your-profile/)  |  [GitHub](https://github.com/your-username)")

