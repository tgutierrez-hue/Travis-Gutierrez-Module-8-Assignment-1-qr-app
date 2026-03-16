import streamlit as st
import qrcode

st.title("QR Code Generator")

text = st.text_input("Enter text or a URL")

if text:
    qr = qrcode.make(text)
    st.image(qr)