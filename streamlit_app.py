# streamlit_app.py
import streamlit as st
from PIL import Image

# --- Configuration ---
st.set_page_config(page_title="AKASH.S", layout="wide")

# --- Sidebar Navigation ---
# menu = st.sidebar.radio("Navigation", ["Home", "Research", "Projects", "Blog", "CV"])
# --- Custom Sidebar Navigation ---
st.markdown("""
<style>
/* Ensure sidebar content is always visible in both themes */

/* Target the entire sidebar */
section[data-testid="stSidebar"] {
    background-color: transparent;
}

/* Sidebar headings and radio text */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4,
section[data-testid="stSidebar"] h5,
section[data-testid="stSidebar"] h6,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span {
    color: inherit !important;  /* ✨ ADAPTS TO THEME */
    font-size: 16px;
    font-weight: 500;
}

/* Optional: Make selected radio option bold and colored */
div[role="radiogroup"] > label[data-testid="stRadioOption"]:has(input:checked) {
    font-weight: bold;
    color: #0066cc !important;
}
</style>
""", unsafe_allow_html=True)
menu = st.sidebar.markdown("## 🧭 Navigation")


nav_options = ["Home", "Research", "Projects", "Blog", "CV"]
#menu = st.sidebar.radio("Navigation", nav_options, index=0)


# --- Cover Image ---
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

# --- Projects Page ---
from PIL import Image
from io import BytesIO
import base64

# --- Load Shared Preview Image ---
def get_base64_image(path):
    img = Image.open(path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

shared_img_base64 = get_base64_image("static/preview/preview.jpeg")  # ✅ Your current shared image

st.markdown("""
<style>
/* ✅ Fully remove Streamlit’s wrapper backgrounds */
.element-container {
    background: transparent !important;
    padding: 0 !important;
    margin: 0 !important;
    box-shadow: none !important;
}

.stMarkdown {
    background: transparent !important;
}

/* ✅ Also override column background if used */
.css-1kyxreq, .block-container {
    background: transparent !important;
}

/* ✅ Page background dark */
body {
    background-color: #0e1117 !important;
}

/* Optional: soften text color globally */
h4, p, a {
    color: #ffffffcc;
}
</style>
""", unsafe_allow_html=True)



# --- Tile Renderer with Preview ---
#def render_tile(title, url, description, img_base64):
def render_tile(title, url, description, img_base64=shared_img_base64):
    tile_height = 380
    image_height = 150
    line_clamp = 4

    return f"""
    <div class="transparent-tile" style="
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 16px;
        margin: 6px;
        height: {tile_height}px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        box-sizing: border-box;
    ">
        <img src="data:image/png;base64,{img_base64}" style="
            width: 100%;
            height: {image_height}px;
            object-fit: cover;
            border-radius: 8px;
            margin-bottom: 10px;
        " />
        <h4 style="margin-bottom: 8px; font-size: 16px; line-height: 1.3; color: #00BFFF;">
            <a href="{url}" target="_blank" style="text-decoration: none; color: #00BFFF;">{title}</a>
        </h4>
        <p style="color: #ffffffcc; font-size: 13px; line-height: 1.4; overflow: hidden;
                  display: -webkit-box; -webkit-line-clamp: {line_clamp}; -webkit-box-orient: vertical;
                  min-height: 60px;">
            {description}
        </p>
    </div>
    """



# --- Blog Page ---
import requests
from bs4 import BeautifulSoup

def get_wp_preview(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip()
        og_image = soup.find("meta", property="og:image")
        image_url = og_image["content"] if og_image else None
        description_tag = soup.find("meta", property="og:description")
        excerpt = description_tag["content"] if description_tag else "Click to read more."
        return title, excerpt, image_url
    except Exception as e:
        return "Blog Title", "Click to read more.", None

def render_blog_tile(title, url, excerpt, image_url=None):
    tile_height = 380
    image_height = 150
    line_clamp = 4

    img_tag = f"""
    <img src='{image_url}' style='
        width:100%;
        height:{image_height}px;
        object-fit:cover;
        border-radius:6px;
        margin-bottom:10px;
    '/>""" if image_url else ""

    return f"""
    <div style="
        border: 1px solid #e6e6e6;
        border-radius: 12px;
        padding: 16px;
        margin: 6px;  /* ✅ adds spacing between tiles */
        background-color: #fafafa;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.06);
        height: {tile_height}px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    ">
        {img_tag}
        <h4 style='margin-bottom: 8px; font-size: 16px; line-height: 1.3;'>
            <a href='{url}' target='_blank' style='text-decoration: none; color: #0066cc;'>{title}</a>
        </h4>
        <p style='font-size: 13px; line-height: 1.4; overflow: hidden; display: -webkit-box;
                  -webkit-line-clamp: {line_clamp}; -webkit-box-orient: vertical;'>
            {excerpt}
        </p>
    </div>
    """

# Publication tile
def render_publication_tile(title, url, authors, journal, year):
    return f"""
    <div style="
        border: 1px solid #e6e6e6;
        border-radius: 12px;
        padding: 16px;
        margin: 6px;
        background-color: #fafafa;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.06);
        height: auto;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    ">
        <h4 style='margin-bottom: 6px; font-size: 16px; line-height: 1.3; color: #1a1a1a;'>
            <a href='{url}' target='_blank' style='text-decoration: none; color: #0066cc;'>{title}</a>
        </h4>
        <p style='font-size: 13px; margin: 4px 0 0 0; color: #1a1a1a;'><i>{authors}</i></p>
        <p style='font-size: 13px; margin: 2px 0 0 0; color: #1a1a1a;'><i>{journal}, {year}</i></p>
    </div>
    """


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
        # --- Publications Section ---
    st.markdown("### 📚 Recent 5 Publications")

    # Most recent 5 publications as tiles
    publication_tiles = [
        {
            "title": "HYCOM-ECOSMO for the Indian Ocean: a simulation of oxygen minimum zone variability over the last two decades",
            "authors": "Akash, S. et al.",
            "journal": "Journal of Oceanography",
            "year": "2025",
            "doi": "https://doi.org/10.1007/s10872-025-00744-0"
        },
        {
            "title": "Distribution dynamics of kiddi prawn using multi-dimensional approach",
            "authors": "Dineshbabu A.P. et al., incl. Akash S.",
            "journal": "Regional Studies in Marine Science",
            "year": "2024",
            "doi": "https://doi.org/10.1016/j.rsma.2023.103364"
        },
        {
            "title": "Interannual variability of chlorophyll-a and impact of extreme climatic events in SE Arabian Sea",
            "authors": "Shafeeque, M. et al., incl. Akash S.",
            "journal": "Regional Studies in Marine Science",
            "year": "2021",
            "doi": "https://doi.org/10.1016/j.rsma.2021.101986"
        },
        {
            "title": "Spatio-temporal variations of chlorophyll from satellite and CMIP5 models",
            "authors": "Joseph, D. et al., incl. Akash S.",
            "journal": "Journal of Earth System Science",
            "year": "2021",
            "doi": "https://doi.org/10.1007/s12040-021-01663-6"
        },
        {
            "title": "Observed links between coastal ocean processes and Indian Oil Sardine fishery",
            "authors": "Akash, S. et al.",
            "journal": "Regional Studies in Marine Science",
            "year": "2021",
            "doi": "https://doi.org/10.1016/j.rsma.2021.101850"
        }
    ]

    for pub in publication_tiles:
        st.markdown(render_publication_tile(
            title=pub["title"],
            url=pub["doi"],
            authors=pub["authors"],
            journal=pub["journal"],
            year=pub["year"]
        ), unsafe_allow_html=True)



    # Remaining publications as list
    st.markdown("### 🗂️ Earlier Publications")
    st.markdown("""
- Sajna V.H. et al., incl. Akash S., 2021. *Impact of climate change on the fishery of Indian mackerel.* [DOI: 10.1016/j.rsma.2021.101773](https://doi.org/10.1016/j.rsma.2021.101773)
- Shah, P. et al., incl. Akash S., 2019. *A holistic approach to upwelling and downwelling along the SW coast of India.* [DOI: 10.1080/01490419.2018.1553805](https://doi.org/10.1080/01490419.2018.1553805)
    """)





# --- Projects Section ---
elif menu == "Projects":

    st.title("📁 Projects")

    st.markdown("I actively develop scientific tools, analytical pipelines, and domain-specific machine learning models across environmental science, health, and geospatial domains. Below are selected projects:")

    # 🌊 Oceanography & Climate Tools
    st.subheader("🌊 Oceanography & Climate Tools")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(render_tile(
            title="argohycom-toolbox",
            url="https://github.com/akashspunnayil/ClimoMarineLabProjects/tree/main/projects/argohycom_toolbox",
            description="Colocation and filtering of BGC-Argo profiles with HYCOM outputs.",
            img_base64=shared_img_base64  # ✅ Required fourth argument
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(render_tile(
            title="Ocean Transport Estimator",
            url="#",
            description="Compute zonal & meridional transport of scalar variables. *(link coming soon)*"
        ), unsafe_allow_html=True)

    with col3:
        st.markdown(render_tile(
            title="DSL Depth Estimator",
            url="#",
            description="Estimate OMZ/DSL depths from cruise observations. *(link coming soon)*"
        ), unsafe_allow_html=True)

    # 🏥 Health, Water, and Urban Analytics
    st.subheader("🏥 Health, Water, and Urban Analytics")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(render_tile(
            title="Air Pollution Hotspot Calculator",
            url="https://github.com/akashspunnayil/ClimoMarineLabProjects/tree/main/projects/aph_calculator",
            description="Rank urban hotspots using percentile + threshold logic."
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(render_tile(
            title="Drinking Water Quality Dashboard",
            url="https://github.com/akashspunnayil/ClimoMarineLabProjects/tree/main/projects/brc_stream_drinking_water_quality",
            description="Panchayat-level survey data analytics and visualization."
        ), unsafe_allow_html=True)

    with col3:
        st.markdown(render_tile(
            title="Diabetes Risk Classifier",
            url="https://github.com/akashspunnayil/AI_ML_DS_projects/blob/master/2_Diabetes_EDA_ML.ipynb",
            description="ML-based health risk classification with PDF reports."
        ), unsafe_allow_html=True)

    # 🚗 ML Models & Predictive Analytics
    st.subheader("🚗 ML Models & Predictive Analytics")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(render_tile(
            title="Car Price Prediction Dashboard",
            url="https://github.com/akashspunnayil/AI_ML_DS_projects/blob/master/1_Automobiles_EDA_ML.ipynb",
            description="EDA and regression modeling on automobile pricing data."
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(render_tile(
            title="Sea Level Trend Detector",
            url="#",
            description="Sliding window detection of long-term trends in sea level. *(link coming soon)*"
        ), unsafe_allow_html=True)

    # 🧠 AI/ML Practice Notebooks
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
                st.markdown(render_tile(
                    title=title,
                    url=f"https://github.com/akashspunnayil/AI_ML_DS_projects/blob/master/{link}",
                    description="Click to view notebook."
                    # In future: img_base64=get_base64_image("static/preview/your_custom.png")
                ), unsafe_allow_html=True)




# --- Blog Page ---
elif menu == "Blog":
    st.title("✍️ Blog")

    # --- Intro Section ---
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

    st.markdown("### 📚 Blog Posts")
    
    blog_links = [
        "https://aireenproject.wordpress.com/2024/07/21/python-loading-multiple-netcdf-files-and-plotting-subplots/",
        "https://aireenproject.wordpress.com/2024/06/05/python-a-guide-to-customizing-themes-in-jupyter/",
        "https://aireenproject.wordpress.com/2023/12/26/python-clipping-netcdf-data-using-shapefile/",
        "https://aireenproject.wordpress.com/2023/11/10/python-calculations-made-easy/",
        "https://aireenproject.wordpress.com/2023/11/03/handling-table-data/",
        "https://aireenproject.wordpress.com/2023/10/27/the-key-to-time-series-plotting/",
        "https://aireenproject.wordpress.com/2023/10/19/the-world-of-netcdf/",
        "https://aireenproject.wordpress.com/2023/10/10/dive-into-python-essential-tutorial-series-for-ocean-and-climate-researchers/"
    ]

    for i in range(0, len(blog_links), 2):
        cols = st.columns(3)
        for col, link in zip(cols, blog_links[i:i+2]):
            title, excerpt, img_url = get_wp_preview(link)
            with col:
                st.markdown(render_blog_tile(title, link, excerpt, img_url), unsafe_allow_html=True)



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


