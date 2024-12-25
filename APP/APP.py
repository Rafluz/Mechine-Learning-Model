import streamlit as st
import numpy as np
import pickle

# Set konfigurasi halaman
st.set_page_config(page_title="Fruit")

# Judul aplikasi
st.title('Name Fruit')

# Input pengguna
D = float(st.number_input("Diameter "))
W = float(st.number_input("Weight "))
R = float(st.number_input("Red "))
G = float(st.number_input("Green "))
B = float(st.number_input("Blue "))


# Tombol submit
submit_lr = st.button("Submit Logistic Regression")
submit_svm = st.button("Submit Naive Bayes")

# Memuat model sekali di awal
with open("LOGISTIC/lr_fruit.pkl", mode='rb') as file:
    modelfruitknn = pickle.load(file)

#with open("SVM/svm_fruit.pkl", mode='rb') as file:
    #modelfruitnb = pickle.load(file)

# Jika tombol ditekan, jalankan prediksi
datapred = None
if submit_lr:
    datainput = np.array([D, W, R, G, B]).reshape(1, -1)
    datapred = modelfruitknn.predict(datainput)
    st.write(f"Species (Logistic Regression): {datapred[0]}")
    
#elif submit_nb:
    #datainput = np.array([D, W, R, G, B]).reshape(1, -1)
    #datapred = modelfruitnb.predict(datainput)
    #st.write(f"Species (Naive Bayes): {datapred[0]}")
