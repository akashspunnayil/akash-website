# streamlit_app.py
import streamlit as st
from PIL import Image
import base64

# --- Helper Functions ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def render_blog_tile(title, url, excerpt, image_url=None):
    image_height = 150

    img_tag = f"""
    <img src='{image_url}' style='
        width:100%;
        height:{image_height}px;
        object-fit:cover;
        border-radius:6px;
        margin-bottom:10px;
    '/>""" if image_url else ""

    return f"""
    <div class="blog-tile">
        {img_tag}
        <h4>
            <a href='{url}' target='_blank' style='text-decoration: none;'>{title}</a>
        </h4>
        <p>{excerpt}</p>
    </div>
    """

# --- Theme-Adaptive CSS ---
st.markdown("""
<style>
.blog-tile {
    background-color: #fafafa;
    color: #1a1a1a;
    border: 1px solid #e6e6e6;
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
@media (prefers-color-scheme: dark) {
    .blog-tile {
        background-color: #1e1e1e;
        color: #eeeeee;
        border: 1px solid #444;
    }
    .blog-tile h4, .blog-tile p {
        color: #eeeeee;
    }
    .blog-tile a {
        color: #66b3ff;
    }
}
</style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
menu = st.sidebar.radio("Navigation", ["Home", "Research", "Projects", "Blog", "CV"])

# --- Home Page ---
if menu == "Home":
    st.title("Hi, I'm AKASH. S (AKASH SOMASEKHARAN)")
    st.subheader("Oceanography Researcher | Data Scientist | Scientific Consultant")

    st.markdown("""
    <p style='font-size:16px; line-height:1.6; color: inherit;'>
        I am a multidisciplinary researcher with over 7 years of experience in <b>physical oceanography</b>, 
        <b>biogeochemical modeling</b>, and <b>data science consulting</b>. My work bridges academic research and 
        applied analytics, focusing on climate–ocean dynamics, dissolved oxygen variability, and actionable 
        insights from complex datasets.
    </p>
    """, unsafe_allow_html=True)

# --- Research Page ---
elif menu == "Research":
    st.title("🔬 Research")
    st.markdown("""
    <div style='font-size: 16px; line-height: 1.7; color: inherit;'>
    <p>
        My doctoral research focuses on the <strong>interplay between ocean physics and biogeochemistry</strong> in shaping the Oxygen Minimum Zone (OMZ) in the Arabian Sea.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📚 Recent 5 Publications")
    publication_tiles = [
        {
            "title": "HYCOM-ECOSMO for the Indian Ocean: a simulation of oxygen minimum zone variability",
            "url": "https://doi.org/10.1007/s10872-025-00744-0",
            "excerpt": "Akash S. et al., Journal of Oceanography (2025)"
        },
        {
            "title": "Distribution dynamics of kiddi prawn",
            "url": "https://doi.org/10.1016/j.rsma.2023.103364",
            "excerpt": "Dineshbabu A.P. et al., incl. Akash S. (2024)"
        },
        {
            "title": "Interannual variability of chlorophyll-a",
            "url": "https://doi.org/10.1016/j.rsma.2021.101986",
            "excerpt": "Shafeeque M. et al., incl. Akash S. (2021)"
        },
        {
            "title": "Spatio-temporal variations of chlorophyll from satellite and CMIP5",
            "url": "https://doi.org/10.1007/s12040-021-01663-6",
            "excerpt": "Joseph D. et al., incl. Akash S. (2021)"
        },
        {
            "title": "Links between coastal processes and Indian Oil Sardine",
            "url": "https://doi.org/10.1016/j.rsma.2021.101850",
            "excerpt": "Akash S. et al. (2021)"
        }
    ]

    for pub in publication_tiles:
        st.markdown(render_blog_tile(pub['title'], pub['url'], pub['excerpt']), unsafe_allow_html=True)

    st.markdown("### 🗂️ Earlier Publications")
    st.markdown("""
- Sajna V.H. et al., incl. Akash S. (2021). [DOI](https://doi.org/10.1016/j.rsma.2021.101773)
- Shah, P. et al., incl. Akash S. (2019). [DOI](https://doi.org/10.1080/01490419.2018.1553805)
    """)

# --- Projects Page ---
elif menu == "Projects":
    st.title("🧪 Projects")
    st.markdown("""
    <p style="font-size: 16px; line-height: 1.6; color: inherit;">
        Explore my open-source scientific tools and custom analytics packages designed to streamline research in climate science, oceanography, and data-driven decision-making.
    </p>
    """, unsafe_allow_html=True)

    st.subheader("🌊 Oceanography & Climate Tools")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(render_blog_tile(
            title="argohycom-toolbox",
            url="https://github.com/akashspunnayil/ClimoMarineLabProjects/tree/main/projects/argohycom_toolbox",
            excerpt="Colocation and filtering of BGC-Argo profiles with HYCOM outputs."
        ), unsafe_allow_html=True)

# --- Blog Page ---
elif menu == "Blog":
    st.title("📝 Technical Blog")
    st.markdown("""
    <p style="font-size: 16px; line-height: 1.6; color: inherit;">
        Read my latest insights, guides, and case studies on applying machine learning in ocean science, building custom Python tools, and solving domain-specific problems.
    </p>
    """, unsafe_allow_html=True)

    # Example post
    st.markdown(render_blog_tile(
        title="Building a Sliding Window Sea Level Trend Detector",
        url="https://yourblog.com/sea-level-trends",
        excerpt="Learn how I built a spatial sliding window tool for trend detection in gridded sea level data using xarray and NumPy."
    ), unsafe_allow_html=True)

# --- CV Page ---
elif menu == "CV":
    st.title("📄 Curriculum Vitae")
    st.markdown("""
    <p style="font-size: 16px; line-height: 1.6; color: inherit;">
        Download my full CV below, or scroll through for an overview of my academic background, project history, technical skills, and consulting experience.
    </p>
    <a href="https://github.com/akashspunnayil/akash-website/raw/main/static/AkashS_CV.pdf" target="_blank">
        📄 Download CV (PDF)
    </a>
    """, unsafe_allow_html=True)

