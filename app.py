
# Imports 
import streamlit as st
import docx2txt
import os
import spacy
import pandas as pd
import pdfplumber

def pred(text):
    '''Function that performs predictions on the model built using Spacy'''
    output={}
    nlp=spacy.load("model")
    text=text.replace('\n',' ')
    doc = nlp(text)
    for ent in doc.ents:
        print(f'{ent.label_.upper():{30}}-{ent.text}')
        output[ent.label_.upper()]=ent.text
    return output


st.title("Resume Parser") # Sets title 
st.subheader("Upload your resume here!") # Sets sub-title
uploaded_file = st.file_uploader("Upload Files",type=['pdf','docx']) # File uploader 

if uploaded_file is not None: 
    if st.button("Process"): # Check if the button is pressed

        # Check the type of file uploaded 
        if uploaded_file.type=='application/pdf': #handling pdf files
            file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
            with pdfplumber.open(uploaded_file) as pdf:
                ext_txt = str() # Initialize a string
                for i in range(len(pdf.pages)):
                    # Extract text of the pdf from all the pages and store in the initiated string
                    page = pdf.pages[0]
                    ext_txt += page.extract_text() 
                op = pred(ext_txt)
                st.write(op) # Display the output
        if uploaded_file.type=='application/vnd.openxmlformats-officedocument.wordprocessingml.document': #  Handling word documents
            file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
            raw_text = docx2txt.process(uploaded_file) # Extract raw text from word document
            op = pred(raw_text)
            st.write(op) # Display the output

        

