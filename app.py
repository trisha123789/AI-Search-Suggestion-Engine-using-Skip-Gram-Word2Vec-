import streamlit as st
from gensim.models import Word2Vec
@st.cache_resource
def load_model():
    return Word2Vec.load("optimizer.model")
model  = load_model()
st.set_page_config(page_title="AI SEARCH ENGINE",layout="centered")
st.title("AI SEARCH ENGINE")
st.write("Wikipedia + Skip-Gram Intelligence")
query = st.text_input("Enter your search Query:")
if query:
    if query in model.wv:
        results = model.wv.most_similar(query,topn=10)
        st.subheader(" Related searches")
        for word in results:
            st.write(f"{word[0]}")
    else:
        st.write("Word not found in Knowledge Base.")