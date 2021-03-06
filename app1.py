# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 16:53:17 2021

@author: Prabh
"""


import pandas as pd
import numpy as np
import pickle
import streamlit as st

from PIL import Image


pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)


def welcome():
    return("Welcome Learner")


def predict_note_authenticator(variance,skewness,curtosis,entropy):
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return(prediction)

def main():
    st.title("Bank Authenticator")
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    variance=st.text_input("Variance","TypeHere")
    skewness=st.text_input("skewness","TypeHere")
    curtosis=st.text_input("curtosis","TypeHere")
    entropy=st.text_input("entropy","TypeHere")
    result=""
    if st.button("Predict"):
        result=predict_note_authenticator(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("And do YO YO")
if __name__=='__main__':
    main()