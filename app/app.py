"""
Script for launching anime recommendation system app.

Example usage: python -m streamlit run app/app.py
"""

import streamlit as st

from dotenv import load_dotenv
from pipeline.pipeline import AnimeRecommendationPipeline


st.set_page_config(page_title="Anime Recommender", layout="wide")
st.title("Anime Recommender System")

load_dotenv()


@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()


# Init pipeline:
pipeline = init_pipeline()

query = st.text_input(
    "Enter your anime preferences", placeholder="a light-hearted drama with a school setting"
)

if query:
    with st.spinner("Retrieving recommendations..."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)