import os
import cv2
import streamlit as st

st.set_page_config(page_title="Learning Interface", page_icon=":book:", layout="wide")

st.header('Learning Interface')
st.info('In this section, a huge collection of hand signs can be explored from the ASLLVD Dataset.')

st.sidebar.header("Learning Interface")
st.sidebar.info("Learning Page lets you explore and visualise, a huge collection of hand signs from the ASLLVD Dataset.")

PATH = os.path.join('ASLLVD')
signs = (os.listdir(PATH))

col1, col2 = st.columns(2)
with col1:
    st.error('The American Sign Language Lexicon Video Dataset (ASLLVD) consists of videos of >3,300 ASL signs in citation form, each produced by 1-6 native ASL signers, for a total of almost 9,800 tokens. This dataset includes multiple synchronized videos showing the signing from different angles. To facilitate computer vision-based sign language recognition, the dataset also includes numeric ID labels for sign variants, video sequences in uncompressed-raw format, and camera calibration sequences.')
    option = st.selectbox('Select a ASLLVD sign:', signs)
    signer = st.slider('Select a signer:', 0, 3)
with col2:
    fname = os.path.join('ASLLVD/' + option + '/' + str(signer))
    video_file = open(fname + '.mp4', 'rb')
    video_bytes = video_file.read()
    with st.container():
        st.video(video_bytes)