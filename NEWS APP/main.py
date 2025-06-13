import requests
import streamlit as st

st.set_page_config(page_title='News',layout='centered')
st.title("News Bazzar")

api = 'API_Key' #get your own API from NEWS API AND PUT IT HERE
query = st.text_input("Enter a topic to Search: ")

if query:
    url = f'https://newsapi.org/v2/everything?q={query}&from=2025-05-13&sortBy=publishedAt&apiKey={api}'

    req = requests.get(url)

    j_data = req.json()
    name_list = []

    article = j_data['articles']

    for data in article:
        if data['source']['name'] not in name_list:
            name_list.append(data['source']['name'])
    
    task1 = st.selectbox("Choose Newsletter",name_list)        

    for data in article:
        if data['source']['name'] == task1:
            title = data.get('title', "None")
            author = data.get('author', "None")
            description = data.get('description', "None")
            link = data.get('url', "None")
            content = data.get('content', "None")
            st.markdown(f"### {title}")
            st.markdown(f"**Author:** {author}")
            st.markdown(f"**Source:** {task1}")
            st.markdown(f"[🔗 Read Full Article]({link})", unsafe_allow_html=True)

            st.markdown("**Summary:**")
            st.markdown(description)

            st.markdown("**Content:**")
            st.markdown(content)

            st.markdown("---")
            