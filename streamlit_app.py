# streamlit_app.py
import streamlit as st
from PIL import Image

# --- Configuration ---
st.set_page_config(page_title="AKASH. S", layout="wide")

# --- Sidebar Navigation ---
menu = st.sidebar.radio("Navigation", ["Home", "Research", "Projects", "Blog", "CV"])


st.markdown(
    """
    <div style='text-align: center;'>
        <img src='static/cover2.png' style='max-width: 100%; height: auto; border-radius: 10px;' />
    </div>
    """,
    unsafe_allow_html=False
)

# --- Home Page ---
if menu == "Home":
    #st.image("static/cover.jpg", use_column_width=True)
    #st.image("static/cover.png", width=800, caption="Data meets AI – Akash S.")
    st.title("Hi, I'm AKASH. S (AKASH SOMASEKHARAN)")
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
    st.markdown("""
    My doctoral research focuses on the **interplay between ocean physics and biogeochemistry** in shaping the Oxygen Minimum Zone (OMZ) in the Arabian Sea. By combining **numerical modeling**, **observational data**, and **machine learning**, I aim to uncover key mechanisms behind OMZ variability and its ecological implications.

    ### 🧪 Core Research Themes
    - **Seasonal and interannual OMZ variability** in the Arabian Sea  
    - Influence of **climate drivers** such as ENSO and IOD on ocean oxygenation  
    - **Circulation and scalar transport diagnostics** using HYCOM-ECOSMO outputs  
    - Vertical and lateral export of **oxygen, detritus, nitrate** through undercurrents and offshore jets  
    - Role of **intermediate water masses and upwelling** in biogeochemical redistribution  

    ### 📊 Modeling Tools & Approaches
    - High-resolution simulations with **HYCOM-ECOSMO** for coupled physical-biogeochemical analysis  
    - Development of a **physics-informed OMZ Intensity Index**  
    - Scalar transport estimators for oxygen, detritus, nitrate, and phytoplankton  
    - **Hovmöller-style diagrams**, seasonal climatologies, and transport cross-sections  

    ### 🤖 AI & Machine Learning in Ocean Science
    - Application of **XGBoost**, **Random Forests**, and **GAM models** to predict:
        - OMZ structure and seasonal shifts  
        - Myctophid catch and biomass based on ecological predictors  
    - Feature engineering from ocean circulation, productivity, and oxygen gradients  

    ---
    My research aims to bridge traditional physical oceanography with modern data science to better understand **marine oxygen variability**, its drivers, and broader implications for ecosystem functioning and fisheries.
    """)


# --- Projects Page ---
elif menu == "Projects":
    st.title("📁 Projects")

    st.markdown("""
    I actively develop scientific tools, analytical pipelines, and domain-specific machine learning models across environmental science, health, and geospatial domains. Below are selected projects reflecting both my academic research and data science consulting portfolio.

    ### 🌊 Oceanography & Climate Tools
    - [`argohycom-toolbox`](https://github.com/akashspunnayil/ClimoMarineLabProjects/tree/main/projects/argohycom_toolbox): Python module for colocation and filtering of BGC-Argo profiles with HYCOM model outputs.
    - Ocean Transport Estimator: Custom script for computing zonal and meridional transport of scalar variables. *(link coming soon)*
    - DSL Depth Estimator: Tool for mapping DSL (Deep Scattering Layer) and OMZ boundaries from cruise observations. *(link coming soon)*

    ### 🏥 Health, Water, and Urban Analytics
    - [`Air Pollution Hotspot Calculator`](https://github.com/akashspunnayil/ClimoMarineLabProjects/tree/main/projects/aph_calculator): CLI/Jupyter-based tool for identifying and ranking pollution hotspots using percentile and threshold logic.
    - [`Drinking Water Quality Dashboard`](https://github.com/akashspunnayil/ClimoMarineLabProjects/tree/main/projects/brc_stream_drinking_water_quality): Statistical analysis and visualization tool for panchayat-level water survey data.
    - Diabetes Risk Classifier: Supervised ML model with automated PDF report generation. *(link coming soon)*

    ### 🚗 ML Models & Predictive Analytics
    - Car Price Prediction Dashboard: Applied EDA and regression models for automobile pricing. *(link coming soon)*
    - Sea Level Trend Detector: Sliding window algorithm to detect long-term changes in sea level using gridded spatiotemporal data. *(link coming soon)*

    ---
    📌 Many of these tools are open-source and built with reproducibility in mind. I regularly maintain and expand them under the ClimoMarineLab GitHub workspace.
    """)


# --- Blog Page ---
elif menu == "Blog":
    st.title("✍️ Blog")
    st.markdown("""
    I regularly share tutorials, research notes, and data science experiments through my blog **[Aireen Project](https://aireenproject.wordpress.com/category/python-classes/)**.

    ### 🔍 What I Write About:
    - 🔬 Ocean science, OMZ dynamics, and data-driven marine research  
    - 🤖 Machine learning workflows for scientific and real-world problems  
    - 🛰️ Remote sensing, cruise-based survey experiences, and field insights  
    - 🛠️ Python scripting, automation, and tool building  
    - 😄 Occasionally... fun experiments with code and observations from the field

    📖 Visit: [aireenproject.wordpress.com/category/python-classes/](https://aireenproject.wordpress.com/category/python-classes/)
    """)

    st.info("New posts and internal blog integration coming soon!")


# --- CV Page ---
elif menu == "CV":
    st.title("📄 Curriculum Vitae")

    with open("resume.pdf", "rb") as file:
        st.download_button(
            label="📥 Download My CV",
            data=file.read(),
            file_name="Akash_Somasekharan_CV.pdf",
            mime="application/pdf"
        )

    st.markdown("---")
    st.subheader("📬 Connect with Me")

    st.markdown("""
    - [🔗 LinkedIn](https://www.linkedin.com/in/akash-s-1a68868b/)  
    - [💻 GitHub](https://github.com/akashspunnayil)  
    - [📚 ResearchGate](https://www.researchgate.net/profile/Akash-Somasekharan)  
    - [🛠️ Upwork – Freelance Profile](https://www.upwork.com/freelancers/~01e11e300ee896d62c?mp_source=share)
    """)

    st.info("I'm open to collaborations, freelance consulting, and research partnerships across oceanography, environmental science, and data-driven domains.")


