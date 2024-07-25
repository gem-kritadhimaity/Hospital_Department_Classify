import streamlit as st
# import json

from utils.classify import classify_department

# Streamlit UI
st.title("Hospital Department Classification")
st.write("Provide necessary symptoms to know the required Department to visit.")
st.write("Given symptoms eg: fever, headache, vomiting...")

# Text input for symptoms
symptoms = st.text_input("Enter your symptoms")

# Submit button to process the input text
if st.button("Submit"):
    if symptoms:
        result = classify_department(symptoms)
        st.write(result)
    else:
        st.write("Please enter symptoms to get a classification.")

# Clear button to clear the output
if st.button("Clear"):
    st.experimental_rerun()



