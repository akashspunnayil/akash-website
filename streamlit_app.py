# streamlit_app.py
import streamlit as st
from PIL import Image

# --- Configuration ---
st.set_page_config(page_title="AKASH. S (AKASH SOMASEKHARAN)", layout="wide")

# --- Sidebar Navigation ---
menu = st.sidebar.radio("Navigation", ["Home", "Research", "Projects", "Blog", "CV"])

# --- Home Page ---
if menu == "Home":
    st.title("Hi, I'm Akash S. (Akash Somasekharan)")
    st.subheader("Oceanography Researcher | Data Scientist | Scientific Consultant")

    st.markdown("""
    I am a multidisciplinary scientist with over 7 years of experience in **physical oceanography**, 
    **biogeochemical modeling**, and **data science consulting**. My work bridges academic research and 
    applied analytics, focusing on climate–ocean dynamics, dissolved oxygen variability, and actionable 
    insights from complex datasets.

    ### 🔬 Academic & Research Focus
    - Ocean-climate interactions: **OMZ dynamics**, **upwelling**, **circulation**, **ENSO/IOD impacts**
    - Biogeochemical and physical modeling using **HYCOM-ECOSMO**
    - High-resolution data analysis using **in-situ**, **reanalysis**, and **remote sensing** datasets

    ### 🧠 Data Science & Programming
    - Machine learning (XGBoost, Random Forests, GAMs) for predictive modeling
    - HPC, automation, and custom scripting in **Python, R, FORTRAN**
    - Interactive dashboards and visualization workflows

    ### 💼 Freelance Consulting Services
    As a consultant, I’ve delivered custom **data analytics solutions** and **scientific scripting support** 
    to M.Sc., Ph.D. students, and researchers across domains such as:
    - **Environmental and climate research**
    - **Water quality and fisheries analytics**
    - **Health and medical risk modeling**
    - **Business and geospatial insights**

    **Recent Projects** include:
    - *Air Pollution Hotspot Tool*: Ranking cities using percentile-based exposure logic  
    - *Catch Prediction Models*: AI-driven models for fishery productivity and effort optimization  
    - *Diabetes Risk Classifier*: ML-based PDF health report generator  
    - *Sea Level Trend Detector*: Sliding window tool for spatial sea level trend mapping  
    - *argohycom-toolbox*: Python module for collocating BGC-Argo profiles with HYCOM model outputs

    ---
    ### 📌 About This Website
    This website serves as my **portfolio and academic space** where I share:
    - **Research highlights** and **journal publications**
    - Selected **projects and tools**
    - **Technical blogs and notes**
    - Downloadable **CV and contact info**

    I'm passionate about bringing **scientific depth and technical fluency** to real-world problems — across oceanography, climate science, and beyond.
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

