# streamlit_app.py
import streamlit as st
# from streamlit_scroll_navigation import scroll_navbar
from PIL import Image
import os


# --- Configuration ---
st.set_page_config(page_title="AKASH.S", layout="wide") # centered # wide

# st.markdown("""
#     <style>
#     [data-testid="stAppViewContainer"] {
#         background-image: url('https://www.transparenttextures.com/patterns/cubes.png');
#         background-repeat: repeat;
#         # background-size: auto;
#         # background-color: rgba(255,255,255,0.95);
#         background-size: 60px 60px;


#     }
#     </style>
# """, unsafe_allow_html=True)

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background: linear-gradient(to bottom right, #f8f9fa, #e9ecef);
    }
    </style>
""", unsafe_allow_html=True)





# # --- Sidebar Navigation ---
# # menu = st.sidebar.radio("Navigation", ["Home", "Research", "Projects", "Blog", "CV"])
# # --- Custom Sidebar Navigation ---
# st.markdown("""
# <style>
# /* Ensure sidebar content is always visible in both themes */

# /* Target the entire sidebar */
# section[data-testid="stSidebar"] {
#     background-color: transparent;
# }

# /* Sidebar headings and radio text */
# section[data-testid="stSidebar"] h1,
# section[data-testid="stSidebar"] h2,
# section[data-testid="stSidebar"] h3,
# section[data-testid="stSidebar"] h4,
# section[data-testid="stSidebar"] h5,
# section[data-testid="stSidebar"] h6,
# section[data-testid="stSidebar"] p,
# section[data-testid="stSidebar"] label,
# section[data-testid="stSidebar"] span {
#     color: inherit !important;  /* ✨ ADAPTS TO THEME */
#     font-size: 16px;
#     font-weight: 500;
# }

# /* Optional: Make selected radio option bold and colored */
# div[role="radiogroup"] > label[data-testid="stRadioOption"]:has(input:checked) {
#     font-weight: bold;
#     color: #0066cc !important;
# }
# </style>
# """, unsafe_allow_html=True)
# st.sidebar.markdown("## 🧭 Navigation")

# # nav_options = ["🏠 Home", "🔬 Research", "🛠️ Projects", "✍️ Blog", "📄 CV"]
# nav_options = ["Home", "Research", "Projects", "Blog", "CV"]
# #menu = st.sidebar.radio("Navigation", nav_options, index=0)
# menu = st.sidebar.radio(" ", nav_options, index=0)

# --- Top bar Navigation ---
# --- Define nav options with emojis ---
nav_options = ["🏠 Home", "🔬 Research", "🛠️ Projects", "✍️ Blog", "📄 CV"]
labels = {
    "🏠 Home": "Home",
    "🔬 Research": "Research",
    "🛠️ Projects": "Projects",
    "✍️ Blog": "Blog",
    "📄 CV": "CV"
}

# --- Get current query param ---
params = st.query_params
nav = params.get("nav", "🏠 Home")

# Ensure the current nav is valid
if nav not in nav_options:
    nav = "🏠 Home"

# This is your main navigation variable
menu = nav  # ✅ just like your original code

# --- HTML Top Navigation Bar ---
def nav_link(name, href):
    active = "active" if name == menu else ""
    return f'<a href="{href}" class="{active}" target="_self">{name}</a>'  # ✅ no new tab

nav_links = {
    name: f"/?nav={name}"
    for name in nav_options
}

# --- Inject HTML + CSS ---
st.markdown(f"""
<style>
:root {{
    --bg-color: var(--background-color);
    --text-color: var(--text-color);
}}

.topnav {{
    background-color: var(--bg-color);
    color: var(--text-color);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 44px;
    border-bottom: 1px solid #e0e0e0;
    margin-bottom: 12px;
    font-size: 15px;
    font-family: "Segoe UI", sans-serif;
}}

.topnav a {{
    display: inline-block;
    padding: 6px 14px;
    color: var(--text-color);
    text-decoration: none;
    border-radius: 5px;
    transition: background 0.2s;
}}

.topnav a:hover {{
    background-color: rgba(128, 128, 128, 0.1);
}}

.topnav a.active {{
    background-color: #0a58ca;
    color: white !important;
    font-weight: bold;
}}
</style>

<div class="topnav">
    {''.join([nav_link(name, href) for name, href in nav_links.items()])}
</div>
""", unsafe_allow_html=True)



st.markdown("""
<style>
/* 🌞 Light theme defaults */
.blog-tile {
    background-color: #fafafa;
    color: #1a1a1a;
    border: 1px solid #ddd;
    border-radius: 12px;
    padding: 16px;
    margin: 6px;
    height: 380px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

.blog-tile h4 {
    margin-bottom: 8px;
    font-size: 16px;
    line-height: 1.3;
    color: #1a1a1a;
}

.blog-tile p {
    font-size: 13px;
    line-height: 1.4;
    color: #1a1a1a;
    overflow: hidden;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    min-height: 60px;
}

/* 🌚 Dark theme overrides */
@media (prefers-color-scheme: dark) {
    .blog-tile {
        background-color: #1e1e1e;
        color: #eeeeee;
        border: 1px solid #444;
    }

    .blog-tile h4,
    .blog-tile p {
        color: #eeeeee;
    }

    .blog-tile a {
        color: #66b3ff;
    }
    
    /* Hover effect */
.blog-tile:hover, .publication-tile:hover, .transparent-tile:hover {
    transform: translateY(-3px);
    box-shadow: 2px 4px 12px rgba(0, 0, 0, 0.2);
    
}
</style>
""", unsafe_allow_html=True)



# --- Cover Image ---
from PIL import Image
## cover = Image.open("static/cover2.png")
#cover = Image.open("static/croped.png")
##st.image(cover, use_container_width=True)
#resized_cover = cover.resize((1200, 300))  # (width, height)
#st.image(resized_cover)

#cover = Image.open("static/croped.png")
#st.image(cover, use_container_width=True)


import base64
from io import BytesIO
cover = Image.open("static/croped.png")
buffered = BytesIO()
cover.save(buffered, format="PNG")
img_b64 = base64.b64encode(buffered.getvalue()).decode()

st.markdown(f"""
    <div style="width: 100%; overflow: hidden;">
        <img src="data:image/png;base64,{img_b64}" 
             style="width: 100%; height: 300px; object-fit: cover; border-radius: 6px;" />
    </div>
""", unsafe_allow_html=True)



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
        <img src="data:image/png;base64,{img_base64}" alt="{title} image" style="
            width: 100%;
            height: {image_height}px;
            object-fit: cover;
            border-radius: 8px;
            margin-bottom: 10px;
        " />
        <h4 style="margin-bottom: 8px; font-size: 16px; line-height: 1.3;">
            <a href="{url}" target="_blank" rel="noopener noreferrer" style="text-decoration: none; color: inherit; font-weight:600;">{title}</a>
        </h4>
        <p style="
            color: inherit;
            font-size: 13px;
            line-height: 1.4;
            overflow: hidden;
            display: -webkit-box;
            -webkit-line-clamp: {line_clamp};
            -webkit-box-orient: vertical;
            min-height: 60px;
        ">
            {description}
        </p>
        <div style="margin-top: auto; text-align: right;">
            <a href="{url}" target="_blank" rel="noopener noreferrer" style="font-size: 12px; text-decoration: none; color: #00BFFF;">→ Learn more</a>
        </div>
    </div>
    """
import html
def render_tile_highlight(title, url, description, img_base64=shared_img_base64):
    tile_height = 380
    image_height = 150
    line_clamp = 4

    return f"""
    <div style="
        background: rgba(255, 245, 200, 0.12);
        border: 2px solid #ffd700;
        border-radius: 12px;
        padding: 16px;
        margin: 6px;
        height: {tile_height}px;
        box-shadow: 0 4px 14px rgba(255, 215, 0, 0.4);
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        box-sizing: border-box;
    ">
        <img src="data:image/png;base64,{img_base64}" alt="{title} image" style="
            width: 100%;
            height: {image_height}px;
            object-fit: cover;
            border-radius: 8px;
            margin-bottom: 10px;
            border: 2px solid #ffd700;
        " />
        <h4 style="margin-bottom: 8px; font-size: 16px; line-height: 1.3; color: #e69a00;">
            🌟 {title}
            <span style='font-size:12px; background:#e69a00; color:white; padding:2px 6px; border-radius:6px; margin-left:8px;'>NEW</span>
        </h4>
        <p style="
            color: #e69a00;
            font-size: 13px;
            line-height: 1.4;
            text-shadow: 0 0 4px rgba(255, 215, 0, 0.3);
            overflow: hidden;
            display: -webkit-box;
            -webkit-line-clamp: 4;
            -webkit-box-orient: vertical;
            min-height: 60px;
        ">
            {html.escape(description)}
        </p>
        <div style="margin-top: auto; text-align: right;">
            <a href="{url}" target="_blank" rel="noopener noreferrer" style="font-size: 12px; text-decoration: none; color: #e69a00;">→ Launch App</a>
        </div>
    </div>
    """





# --- Blog Page ---
import requests
from bs4 import BeautifulSoup
import re

def get_wp_preview(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string.strip() if soup.title else "Untitled"
        
        # Image
        og_image = soup.find("meta", property="og:image")
        image_url = og_image["content"] if og_image else None

        # Description logic
        description_tag = soup.find("meta", property="og:description")
        if description_tag and len(description_tag.get("content", "").strip()) > 50:
            excerpt = description_tag["content"].strip()
        else:
            first_p = soup.find("p")
            excerpt = first_p.get_text(strip=True) if first_p else "Click to read more."

        # Clean up text
        excerpt = re.sub(r'\s+', ' ', excerpt)
        excerpt = excerpt.replace('…', '...').replace('\u00a0', ' ')

        # Trim to 200 characters
        if len(excerpt) > 200:
            excerpt = excerpt[:197].rsplit(' ', 1)[0] + "..."

        return title, excerpt, image_url

    except Exception as e:
        return "Blog Title", "Click to read more.", None


st.markdown("""
<style>
.blog-tile {
    border-radius: 12px;
    padding: 16px;
    margin: 6px;
    box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.15);
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
    transition: transform 0.2s ease;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

/* Light Theme */
@media (prefers-color-scheme: light) {
    .blog-tile {
        background: rgba(0, 0, 0, 0.03);
        border: 1px solid rgba(0, 0, 0, 0.08);
        color: #111;
    }
    .blog-tile a {
        color: #0056cc;
    }
    .blog-tile p {
        color: #444;
    }
}

/* Dark Theme */
@media (prefers-color-scheme: dark) {
    .blog-tile {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #fff;
    }
    .blog-tile a {
        color: #00BFFF;
    }
    .blog-tile p {
        color: #fff;
    }
}
</style>
""", unsafe_allow_html=True)



import streamlit as st

# Detect Streamlit theme (available from config)
theme = st.get_option("theme.base")
text_color = "#eeeeee" if theme == "dark" else "#444444"
link_color = "#00BFFF" if theme == "dark" else "#0056cc"


# Blog tile
def render_blog_tile(title, url, excerpt, image_url=None, text_color="#444444", link_color="#0056cc"):
    image_height = 150

    img_tag = f"""
    <img src="{image_url}" alt="{title} image" style="
        width: 100%;
        height: {image_height}px;
        object-fit: cover;
        border-radius: 8px;
        margin-bottom: 10px;
    " />""" if image_url else ""

    return f"""
    <div class="blog-tile" style="
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 16px;
        margin: 6px;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.15);
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        transition: transform 0.2s ease;
    ">
        {img_tag}
        <h4 style="margin-bottom: 8px; font-size: 16px; line-height: 1.3;">
            <a href="{url}" target="_blank" rel="noopener noreferrer" style="
                text-decoration: none;
                color: {link_color};
                font-weight: 600;
            ">
                {title}
            </a>
        </h4>
        <p style="
            color: {text_color};
    	    font-size: 13px;
            line-height: 1.4;
            margin: 0;
            display: -webkit-box;
            -webkit-line-clamp: 4;
            -webkit-box-orient: vertical;
            overflow: hidden;
            min-height: 72px;
        ">
            {excerpt}
        </p>
    </div>
    """


# Publication tile
def render_publication_tile(title, url, authors, journal, year):
    return f"""
    <div class="publication-tile" style="
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 16px;
        margin: 6px;
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        transition: transform 0.2s ease;
    ">
        <h4 style="margin-bottom: 6px; font-size: 16px; line-height: 1.3;">
            <a href="{url}" target="_blank" rel="noopener noreferrer" style="text-decoration: none; color: inherit; font-weight: 600;">
                {title}
            </a>
        </h4>
        <p style="font-size: 13px; margin: 4px 0 0 0; color: inherit;"><i>{authors}</i></p>
        <p style="font-size: 13px; margin: 2px 0 0 0; color: inherit;"><i>{journal}, {year}</i></p>
    </div>
    """



# --- Home Page ---
#if menu == "Home":
    ##st.image("static/cover.jpg", use_column_width=True)
    ##st.image("static/cover.png", width=800, caption="Data meets AI – Akash S.")
    
    #st.title("Hi, I'm AKASH. S (AKASH SOMASEKHARAN)")
    #st.subheader("Oceanography Researcher | Data Scientist | Scientific Consultant")

if menu == "🏠 Home":
    st.title("✴️ Welcome")

    col1, col2 = st.columns([2, 1])  # Wider text on the left, image on the right

    with col1:
        st.markdown("""
        <h2 style='margin-bottom: 0;'>I'm <span style="color:#007acc;">AKASH. S</span> <br><small>(AKASH SOMASEKHARAN)</small></h2>
        <p style='font-size: 16px; margin-top: 4px;'>
        Oceanography Researcher | Data Scientist | Scientific Consultant
        </p>
        """, unsafe_allow_html=True)

    with col2:
        st.image("static/akash_profile.jpg", width=150, caption=None)
    
    #st.markdown("""
    #I am a multidisciplinary researcher with over 7 years of experience in **physical oceanography**, 
    #**biogeochemical modeling**, and **data science consulting**. My work bridges academic research and 
    #applied analytics, focusing on climate–ocean dynamics, dissolved oxygen variability, and actionable 
    #insights from complex datasets.

    st.markdown("""
    <div style='font-size: 16px; line-height: 1.7; color: inherit;'>
    
    <p style="color: inherit;">
    I am a multidisciplinary researcher with over 7 years of experience in <strong>physical oceanography</strong>, 
    <strong>biogeochemical modeling</strong>, and <strong>data science consulting</strong>. My work bridges academic research and 
    applied analytics, focusing on climate–ocean dynamics, dissolved oxygen variability, and actionable 
    insights from complex datasets.
    </p>
    
    <h4 style='margin-top: 2em;'>🔬 Academic & Research Focus</h4>
    <ul>
        <li>Ocean-climate interactions: <strong>OMZ dynamics</strong>, <strong>upwelling</strong>, <strong>circulation</strong>, <strong>ENSO/IOD impacts</strong></li>
        <li>Biogeochemical and physical modeling using <strong>HYCOM-ECOSMO</strong></li>
        <li>High-resolution data analysis using <strong>in-situ</strong>, <strong>reanalysis</strong>, and <strong>remote sensing</strong> datasets</li>
    </ul>
    
    <h4 style='margin-top: 2em;'>🧠 Data Science & Programming</h4>
    <ul>
        <li>Machine learning (XGBoost, Random Forests, GAMs) for predictive modeling</li>
        <li>HPC, automation, and custom scripting in <strong>Python, R, FORTRAN</strong></li>
        <li>Interactive dashboards and visualization workflows</li>
    </ul>
    
    <h4 style='margin-top: 2em;'>💼 Freelance Consulting Services</h4>
    <p style="color: inherit;">
    As a consultant, I’ve delivered custom <strong>data analytics solutions</strong> and <strong>scientific scripting support</strong> 
    to M.Sc., Ph.D. students, and researchers across domains such as:
    </p>

    <ul>
        <li><strong>Environmental and climate research</strong></li>
        <li><strong>Water quality and fisheries analytics</strong></li>
        <li><strong>Health and medical risk modeling</strong></li>
        <li><strong>Business and geospatial insights</strong></li>
    </ul>
    
    <h4 style='margin-top: 2em;'>Recent Projects</h4>
    <ul>
        <li><em>Air Pollution Hotspot Tool</em>: Ranking cities using percentile-based exposure logic</li>
        <li><em>Catch Prediction Models</em>: AI-driven models for fishery productivity and effort optimization</li>
        <li><em>Diabetes Risk Classifier</em>: ML-based PDF health report generator</li>
        <li><em>Sea Level Trend Detector</em>: Sliding window tool for spatial sea level trend mapping</li>
        <li><em>argohycom-toolbox</em>: Python module for collocating BGC-Argo profiles with HYCOM model outputs</li>
    </ul>
    
    <hr>
    
    <p style="color: inherit;"><strong>📌 About This Website</strong></p>
    <p style="color: inherit;">
    This website serves as my <strong>portfolio and academic space</strong> where I share:
    </p>
    <ul>
        <li><strong>Research highlights</strong> and <strong>journal publications</strong></li>
        <li>Selected <strong>projects and tools</strong></li>
        <li><strong>Technical blogs and notes</strong></li>
        <li>Downloadable <strong>CV and contact info</strong></li>
    </ul>
    
    <p style="color: inherit;">
    I'm passionate about bringing <strong>scientific depth and technical fluency</strong> to real-world problems — across oceanography, climate science, and beyond.
    </p>
    
    </div>
    """, unsafe_allow_html=True)




# --- Research Page ---
elif menu == "🔬 Research":
    st.title("🔬 Research")

    # Split layout: left (description) | right (citation metrics)
    left, right = st.columns([3, 1])  # Wider left, narrower right

    with left:
        st.markdown("""
        <div style='font-size: 16px; line-height: 1.7; color: inherit;'>
        
        <p style="color: inherit;">
        My doctoral research focuses on the <strong>interplay between ocean physics and biogeochemistry</strong> in shaping the Oxygen Minimum Zone (OMZ) in the Arabian Sea. By combining <strong>numerical modeling</strong>, <strong>observational data</strong>, and <strong>machine learning</strong>, I aim to uncover key mechanisms behind OMZ variability and its ecological implications.
        </p>

        <h4>🧪 Core Research Themes</h4>
        <ul>
        <li><strong>Seasonal and interannual OMZ variability</strong> in the Arabian Sea</li>
        <li>Influence of <strong>climate drivers</strong> such as ENSO and IOD on ocean oxygenation</li>
        <li><strong>Circulation and scalar transport diagnostics</strong> using HYCOM-ECOSMO outputs</li>
        <li>Vertical and lateral export of <strong>oxygen, detritus, nitrate</strong> through undercurrents and offshore jets</li>
        <li>Role of <strong>intermediate water masses and upwelling</strong> in biogeochemical redistribution</li>
        </ul>

        <h4>📊 Modeling Tools & Approaches</h4>
        <ul>
        <li>High-resolution simulations with <strong>HYCOM-ECOSMO</strong> for coupled physical-biogeochemical analysis</li>
        <li>Development of a <strong>physics-informed OMZ Intensity Index</strong></li>
        <li>Scalar transport estimators for oxygen, detritus, nitrate, and phytoplankton</li>
        <li><strong>Hovmöller-style diagrams</strong>, seasonal climatologies, and transport cross-sections</li>
        </ul>
        

        <h4>🤖 AI & Machine Learning in Ocean Science</h4>
        <ul>
          <li>
            Application of <strong>XGBoost</strong>, <strong>Random Forests</strong>, and <strong>GAM models</strong> to predict:
            <ul style="padding-left: 1.5em;">
              <li>OMZ structure and seasonal shifts</li>
              <li>Myctophid catch and biomass based on ecological predictors</li>
            </ul>
          </li>
          <li>Feature engineering from ocean circulation, productivity, and oxygen gradients</li>
        </ul>

        
        <hr>
        <p style="color: inherit;">
        My research aims to bridge traditional physical oceanography with modern data science to better understand <strong>marine oxygen variability</strong>, its drivers, and broader implications for ecosystem functioning and fisheries.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("### 📊 Cited by")
        st.markdown("""
        <table style='font-size: 14px; line-height: 1.6;'>
            <tr>
                <th></th><th>All</th><th>Since 2020</th>
            </tr>
            <tr>
                <td><strong>Citations</strong></td><td>84</td><td>82</td>
            </tr>
            <tr>
                <td><strong>h-index</strong></td><td>4</td><td>4</td>
            </tr>
            <tr>
                <td><strong>i10-index</strong></td><td>2</td><td>2</td>
            </tr>
        </table>
        """, unsafe_allow_html=True)

    # ✅ ResearchGate-style counters using metrics
    st.markdown("### 📑 Research Items Overview")

    items = [
    ("Article", 7),
    ("Chapter", 1),
    ("Experiment Findings", 2),
    ("Presentation", 4),
    ("Poster", 16),
    ("", ""),  # Empty row
    ("", ""),  # Another empty row
    ("Total Research Items", 30)
    ]
    
    cols = st.columns(3)
    for i, (label, count) in enumerate(items):
        with cols[i % 3]:
            if label.strip():  # if not empty
                st.metric(label=label, value=str(count))
            else:
                st.markdown(" ")  # spacer

    # --- Publications Section ---
    st.markdown("### 📚 Recent 5 Publications")

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

    st.markdown("### 🗂️ Earlier Publications")
    st.markdown("""
- Sajna V.H. et al., incl. Akash S., 2021. *Impact of climate change on the fishery of Indian mackerel.* [DOI: 10.1016/j.rsma.2021.101773](https://doi.org/10.1016/j.rsma.2021.101773)  
- Shah, P. et al., incl. Akash S., 2019. *A holistic approach to upwelling and downwelling along the SW coast of India.* [DOI: 10.1080/01490419.2018.1553805](https://doi.org/10.1080/01490419.2018.1553805)
""")



# --- Projects Section ---
elif menu == "🛠️ Projects":

    st.title("🛠️ Projects")

    st.markdown("""
<div style='font-size: 16px; line-height: 1.7; color: inherit;'>

<p style="color: inherit;">
    I actively develop scientific tools, analytical pipelines, and domain-specific machine learning models across environmental science, health, and geospatial domains. Below are selected projects:
</p>

</div>
""", unsafe_allow_html=True)


    # 🌊 Oceanography & Climate Tools
    st.subheader("🌊 Oceanography & Climate Tools")
    tile_data = [
        {
            "title": "🌊🌟 Ocean Viewer App",
            "url": "https://oceanviewer.streamlit.app/",
            "description": "App for view and plot ocean data (currently only NetCDF format compatible)",
            "highlight": True
        },
        {
            "title": "argohycom: toolbox",
            "url": "https://github.com/akashspunnayil/ClimoMarineLabProjects/tree/main/projects/argohycom_toolbox",
            "description": "Colocation and filtering of BGC Argo profiles with HYCOM outputs."
        },
        {
            "title": "Ocean Transport Estimator",
            "url": "",
            "description": "Compute zonal & meridional transports. *(link coming soon)*"
        },
        {
            "title": "DSL Depth Estimator",
            "url": "",
            "description": "Estimate OMZ/DSL depths. *(link coming soon)*"
        },
        
    ]
    
    # n_cols = 3  # 3 tiles per row

    for i in range(0, len(tile_data), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(tile_data):
                tile = tile_data[i + j]
                highlight = tile.get("highlight", False)
    
                with cols[j]:
                    if highlight:
                        st.markdown(render_tile_highlight(
                            title=tile["title"],
                            url=tile["url"],
                            description=tile["description"]
                        ), unsafe_allow_html=True)
                    else:
                        st.markdown(render_tile(
                            title=tile["title"],
                            url=tile["url"],
                            description=tile["description"]
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
            url="https://github.com/akashspunnayil/AI_ML_DS_projects/tree/master/2_Diabetes_EDA_ML",
            description="ML-based health risk classification with PDF reports."
        ), unsafe_allow_html=True)
        

    # 🚗 ML Models & Predictive Analytics
    st.subheader("🚗 ML Models & Predictive Analytics")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(render_tile(
            title="Car Price Prediction Dashboard",
            url="https://github.com/akashspunnayil/AI_ML_DS_projects/tree/master/1_Automobiles_EDA_ML",
            description="EDA and regression modeling on automobile pricing data."
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(render_tile(
            title="Sea Level Trend Detector",
            url="#",
            description="Sliding window detection of long-term trends in sea level. *(link coming soon)*"
        ), unsafe_allow_html=True)


    # 🧠 Computer Vision Projects
    st.subheader("🧠 Computer Vision Projects")
    
    tile_data_2 = [
        {
            "title": "Face Mask Detection App",
            "url": "https://facemask-app.streamlit.app/",
            "description": "Streamlit demo app to detect face mask from image, video and live cam",
            "highlight": True
        },
        {
            "title": "Face Detection App",
            "url": "https://a-face-detection-app.streamlit.app/?app=face-detection",
            "description": "Streamlit demo of live webcam face detection with Haar cascades."
        },
        {
            "title": "House Intrusion Detection App",
            "url": "https://a-house-intrusion-detection-app.streamlit.app/",
            "description": "Streamlit demo of live house intrusion detection system with YOLO."
        }
        
    ]
    
    for i in range(0, len(tile_data_2), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(tile_data_2):
                tile = tile_data_2[i + j]
                highlight = tile.get("highlight", False)
    
                with cols[j]:
                    if highlight:
                        st.markdown(render_tile_highlight(
                            title=tile["title"],
                            url=tile["url"],
                            description=tile["description"],
                            img_base64=shared_img_base64  
                        ), unsafe_allow_html=True)
                    else:
                        st.markdown(render_tile(
                            title=tile["title"],
                            url=tile["url"],
                            description=tile["description"],
                            img_base64=shared_img_base64  
                        ), unsafe_allow_html=True)

    # for i in range(0, len(tile_data_2), 3):
    #     cols = st.columns(3)
    #     for j in range(3):
    #         if i + j < len(tile_data_2):
    #             tile = tile_data_2[i + j]
    #             highlight = tile.get("highlight", False)
    
    #             with cols[j]:
    #                 if highlight:
    #                     st.markdown(render_tile_highlight(
    #                         title=tile["title"],
    #                         url=tile["url"],
    #                         description=tile["description"]
    #                     ), unsafe_allow_html=True)
    #                 else:
    #                     st.markdown(render_tile(
    #                         title=tile["title"],
    #                         url=tile["url"],
    #                         description=tile["description"]
    #                     ), unsafe_allow_html=True)



        
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
        ("Image Augmentation - Horse (ImageDataGenerator)", "10_Image_augmentation_imagedatagen_horse.ipynb"),
        ("Image Augmentation - Helicopter (OpenCV)", "11_Image_augmentation_opencv_helicopter.ipynb"),
        ("Image Augmentation - Sailboat (Keras)", "12_Image_augmentation_keras_sailboat.ipynb"),
        ("Image Augmentation - VGG16 Cats vs Dogs", "13_VGG16_image_augment_CATS_DOGS(Competition).ipynb"),
        ("Object Detection - YOLO on Ship Image", "14_Object_detection_YOLO_ship.ipynb"),
        ("Object Detection - YOLO in Classroom", "15_Object_detection_YOLO_classroom.ipynb"),
        ("Object Detection - YOLO on Traffic Footage", "16_Object_detection_YOLO_traffic2.ipynb"),
        ("Real-time Face Detection - YOLO", "17_Real-time-face-detection-YOLO.ipynb"),
        ("Object Detection - YOLO on Traffic Video Input", "18_Object_detection_input_traffic_video.ipynb"),
    ]

    import os  # Make sure this is at the top

    for i in range(0, len(notebooks), 3):
        cols = st.columns(3)
        for col, (title, link) in zip(cols, notebooks[i:i+3]):
            with col:
                folder = os.path.splitext(link)[0]  # Remove .ipynb extension
                url = f"https://github.com/akashspunnayil/AI_ML_DS_projects/tree/master/{folder}"
                st.markdown(render_tile(
                    title=title,
                    url=url,
                    description="Click to view notebook."
                    # img_base64=... (optional future use)
                ), unsafe_allow_html=True)

    # for i in range(0, len(notebooks), 3):
    #     cols = st.columns(3)
    #     for col, (title, link) in zip(cols, notebooks[i:i+3]):
    #         with col:
    #         	folder = os.path.splitext(link)[0]  # Remove .ipynb extension
    #             url=f"https://github.com/akashspunnayil/AI_ML_DS_projects/tree/master/{folder}"
    #             st.markdown(render_tile(
    #                 title=title,
    #                 url=url,
    #                 description="Click to view notebook."
    #                 # In future: img_base64=get_base64_image("static/preview/your_custom.png")
    #             ), unsafe_allow_html=True)


# --- Blog Page ---
elif menu == "✍️ Blog":
    st.title("✍️ Blog")

    # --- Intro Section ---
    st.markdown("""
        <div style='font-size: 16px; line-height: 1.7; color: inherit;'>

        <p style="color: inherit;">
        I regularly share tutorials, research notes, and data science experiments through my blog under 
        <strong><a href="https://aireenproject.wordpress.com/author/akashspunnayil/" target="_blank">
        Aireen Project</a></strong>.

        ### 🔍 What I Write About:
        - 🔬 Ocean science, OMZ dynamics, and data-driven marine research  
        - 🤖 Machine learning workflows for scientific and real-world problems  
        - 🛰️ Remote sensing, cruise-based survey experiences, and field insights  
        - 🛠️ Python scripting, automation, and tool building  
        - 😄 Occasionally... fun experiments with code and observations from the field

        📖 Visit: 
        <a href="https://aireenproject.wordpress.com/author/akashspunnayil/" target="_blank">
        aireenproject.wordpress.com/author/akashspunnayil/</a>
        </p>

        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📚 Blog Posts")

    # Detect theme and set adaptive colors
    theme = st.get_option("theme.base")
    text_color = "#ffffff" if theme == "dark" else "#444444"
    link_color = "#00BFFF" if theme == "dark" else "#0056cc"

    blog_links = [
    	"https://aireenproject.wordpress.com/2025/03/06/machine-learning-workflows-for-ocean-and-climate-science/",
    	"https://aireenproject.wordpress.com/2025/01/11/into-the-twilight-how-omzs-are-squeezing-life-and-fisheries/",
    	"https://aireenproject.wordpress.com/2024/12/12/ocean-models-and-in-situ-data-a-powerful-partnership/",
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
                st.markdown(
		    render_blog_tile(title, link, excerpt, img_url, text_color, link_color),
		    unsafe_allow_html=True
		)



# --- CV Page ---
elif menu == "📄 CV":
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


