import streamlit as st
import gemini_model as gm

#initialize our streamlit app
st.set_page_config(page_title="Gemini Chat App")

st.header("Gemini Chat Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submitQns=st.button("Question")
uploadFile=st.file_uploader("Upload Image",type=["jpg","png"])

if submitQns and input:
    response=gm.chat_with_bot(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("Response")
    for r in response:
        st.write(r.text)
        st.session_state['chat_history'].append(("Bot", r.text))

if uploadFile and submitQns and input:
    file_bytes = uploadFile.read().decode("utf-8",'ignore')
    response=gm.describe_image(file_bytes,input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("Response")
    for r in response:
        st.write(r.text)
        st.session_state['chat_history'].append(("Bot", r.text))


st.subheader("Chat History")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
    


