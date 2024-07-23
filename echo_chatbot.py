import streamlit as st
st.title("Echo ChatBot")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt:=st.chat_input("What do you wanna talk about?"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role":"user","content":prompt})

response=f"Echo reply: {prompt}"

with st.chat_message("assisstant"):
    st.markdown(response)
st.session_state.messages.append({"role":"assistant","content":response}) 
