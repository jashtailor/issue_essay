import streamlit as st
import pickle 
import random 

with open("issue_topics", "rb") as fp:
  lst = pickle.load(fp)
  
st.header('Issue essay prompt')
