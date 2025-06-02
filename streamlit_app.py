# streamlit_app.py
import streamlit as st
from PIL import Image

# --- Configuration ---
st.set_page_config(page_title="AKASH.S", layout="wide")

# --- Sidebar Navigation ---
menu = st.sidebar.radio("Navigation", ["Home", "Research", "Projects", "Blog", "CV"])


from PIL import Image
cover = Image.open("static/cover2.png")
#st.image(cover, use_container_width=True)
resized_cover = cover.resize((800, 300))  # (width, height)
st.image(resized_cover)


# import base64
# from io import BytesIO

# # --- Function to convert image to base64 ---
# def get_image_base64(image_path):
#     img = Image.open(image_path)
#     buffered = BytesIO()
#     img.save(buffered, format="PNG")
#     img_base64 = base64.b64encode(buffered.getvalue()).decode()
#     return img_base64

# # --- Embed cover image as HTML ---
# cover_base64 = get_image_base64("static/cover2.png")
# st.markdown(
#     f"""
#     <style>
#     .cover-container {{
#         width: 100%;
#          /*max-height: 300px;*/
#         /*overflow: hidden;*/
#         border-radius: 16px;
#         margin-bottom: 20px;
#     }}
#     .cover-container img {{
#         width: 100%;
#         height: auto;
#         /*object-fit: cover;*/
#         object-fit: contain;
#         border-radius: 16px;
#     }}
#     </style>
#     <div class="cover-container">
#         <img src="data:image/png;base64,{cover_base64}" alt="Cover Image">
#     </div>
#     """,
#     unsafe_allow_html=True)


# --- Home Page ---
if menu == "Home":
    #st.image("static/cover.jpg", use_column_width=True)
    #st.image("static/cover.png", width=800, caption="Data meets AI – Akash S.")
    
    st.title("Hi, I'm AKASH. S (AKASH SOMASEKHARAN)")
    st.subheader("Oceanography Researcher | Data Scientist | Scientific Consultant")

    st.markdown("""
    I am a multidisciplinary researcher with over 7 years of experience in **physical oceanography**, 
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

    st.markdown("I actively develop scientific tools, analytical pipelines, and domain-specific machine learning models across environmental science, health, and geospatial domains. Below are selected projects:")

    # --- CSS Style for Tiles ---
    tile_style = """
    <div style="
        border: 1px solid #e6e6e6;
        border-radius: 10px;
        padding: 16px;
        background-color: #fafafa;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 10px;
        height: 100%;
    ">
        <h4 style="margin-bottom: 10px;"><a href='{url}' target='_blank' style='text-decoration: none; color: #0066cc;'>{title}</a></h4>
        <p style='font-size: 14px;'>{description}</p>
    </div>
    """

    # --- Oceanography & Climate Tools ---
    st.subheader("🌊 Oceanography & Climate Tools")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(tile_style.format(
            title="argohycom-toolbox",
            url="https://github.com/akashspunnayil/ClimoMarineLabProjects/tree/main/projects/argohycom_toolbox",
            description="Colocation and filtering of BGC-Argo profiles with HYCOM outputs."
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(tile_style.format(
            title="Ocean Transport Estimator",
            url="#",
            description="Compute zonal & meridional transport of scalar variables. *(link coming soon)*"
        ), unsafe_allow_html=True)

    with col3:
        st.markdown(tile_style.format(
            title="DSL Depth Estimator",
            url="#",
            description="Estimate OMZ/DSL depths from cruise observations. *(link coming soon)*"
        ), unsafe_allow_html=True)

    # --- Health, Water, and Urban Analytics ---
    st.subheader("🏥 Health, Water, and Urban Analytics")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(tile_style.format(
            title="Air Pollution Hotspot Calculator",
            url="https://github.com/akashspunnayil/ClimoMarineLabProjects/tree/main/projects/aph_calculator",
            description="Rank urban hotspots using percentile + threshold logic."
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(tile_style.format(
            title="Drinking Water Quality Dashboard",
            url="https://github.com/akashspunnayil/ClimoMarineLabProjects/tree/main/projects/brc_stream_drinking_water_quality",
            description="Panchayat-level survey data analytics and visualization."
        ), unsafe_allow_html=True)

    with col3:
        st.markdown(tile_style.format(
            title="Diabetes Risk Classifier",
            url="https://github.com/akashspunnayil/AI_ML_DS_projects/blob/master/2_Diabetes_EDA_ML.ipynb",
            description="ML-based health risk classification with PDF reports."
        ), unsafe_allow_html=True)

    # --- ML Models & Predictive Analytics ---
    st.subheader("🚗 ML Models & Predictive Analytics")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(tile_style.format(
            title="Car Price Prediction Dashboard",
            url="https://github.com/akashspunnayil/AI_ML_DS_projects/blob/master/1_Automobiles_EDA_ML.ipynb",
            description="EDA and regression modeling on automobile pricing data."
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(tile_style.format(
            title="Sea Level Trend Detector",
            url="#",
            description="Sliding window detection of long-term trends in sea level. *(link coming soon)*"
        ), unsafe_allow_html=True)

    # --- AI/ML Practice Notebooks ---
    st.subheader("🧠 AI/ML Practice Notebooks")

    notebooks = [
        ("Automobiles EDA + ML", "1_Automobiles_EDA_ML.ipynb"),
        ("Diabetes EDA + ML", "2_Diabetes_EDA_ML.ipynb"),
        ("Housing Price Prediction", "3_Housing_EDA_ML.ipynb"),
        ("Insurance Risk Analysis", "4_Insurance_EDA_ML.ipynb"),
        ("MNIST ANN", "5_MNIST_hyperparameter_ANN.ipynb"),
        ("Fashion MNIST with ANN", "6_FASHION_MNIST_ANN.ipynb"),
        ("CIFAR-10 with ANN", "7_CIFAR_ANN.ipynb"),
        ("Fashion MNIST with CNN", "8_FASHION_MNIST_CNN.ipynb"),
        ("CIFAR-10 with CNN", "9_CIFAR_CNN.ipynb"),
    ]

    for i in range(0, len(notebooks), 3):
        cols = st.columns(3)
        for col, (title, link) in zip(cols, notebooks[i:i+3]):
            with col:
                st.markdown(tile_style.format(
                    title=title,
                    url=f"https://github.com/akashspunnayil/AI_ML_DS_projects/blob/master/{link}",
                    description="Click to view notebook."
                ), unsafe_allow_html=True)




# --- Blog Page ---
elif menu == "Blog":
    st.title("✍️ Blog")
    st.markdown("""
    I regularly share tutorials, research notes, and data science experiments through my blog under **[Aireen Project](https://aireenproject.wordpress.com/category/python-classes/)**.

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


