import streamlit as st
import pandas as pd
import google.generativeai as genai
from sklearn.metrics.pairwise impor cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
st.set_page_config(page_title="Svecw College Chatbot",layout="centered")
if "messages" not in st.session_state:
  st.session_state.messages=[]
csv_url="svcew_details.csv"
try:
  df=pd.read_csv(csv_url)
except Exception as e:
  st.error(f"Failed to load the CSV file.Error: {e}")
  st.stop()
df=df.fillna("")
df['Question']=df['question'].str.lower()
df['Answer']=df['Answer'].str.lower()
vectorizer=TfidfVectorizer()
question_vectorizer.fit_transform(df['Question'])
API_KEY="AIzaSyBOeQUL549Fy6_lcvlDkG_TTsHyHKwTdlE"
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel('gemini-1.5-flash')
def find_closest_question(user_query,vectorizer,question_vectors,df):
  query_vector=vectorizer.transform([user_query.lower()])
  similarities=cosine_similarity(query_vector,question_vectors).flatten()
  best_match_index=similarities.argmax()
  best_match_score=similarities[best_match_index]
  if best_match_score >0.3:
    return df.iloc[best_match_index]['Answer']
  else:
    return None
st.title("Svecw College Chatbot")
st.write("Welcome to the college Chatbot! ask me anything about the colleg.")
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])
if prompt := st.chat_input("Say something..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    closest_answer=find_closest_question(prompt,vectorizer,question_vectors,df)
    if closest_answer:
      st.session_state.message.append({"role":"assistant","content":closest_answer})
      with st.chat_message("assistant"):
        st.markdown(closest_answer)
    else:
      try:
        response=model.generate_content(prompt)
       st.session_state.messages.append({"role":"assistant","content":response.text})
          with st.chat_meassage("assistant"):
              st.markdown(response.text)
        except Exception as e:
          st.error(f"Sorry,I couldn't generate a response. Error: {e}")
