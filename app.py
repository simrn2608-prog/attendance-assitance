import streamlit as st
import pandas as pd
import scraper

# st.title("Attendance Calculator")
st.write("Enter your attendance details below.")
email = st.text_input("email")
st.write("Enter the Password")
password = st.text_input("pass",type="password")

st.button("Reset", type="primary")
if st.button("Get attendance"):
    session = scraper.login(email,password)
    response = scraper.fetch_data(session)
    data = scraper.parse_data(response)
    df = pd.DataFrame(data)
    st.dataframe(df)
else:
    st.write("Hlo")



