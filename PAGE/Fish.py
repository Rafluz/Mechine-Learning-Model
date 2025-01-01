import streamlit as st
import numpy as np
import pickle

# Set konfigurasi halaman
st.set_page_config(page_title="Fruit")

# Judul aplikasi
st.title('Name Fruit')

# Input pengguna
L = float(st.number_input("Length (Panjang)"))
W = float(st.number_input("Weight (Berat)"))
WLR = float(st.number_input("W|L Ratio (Rasio Besar dan Panjang)"))

# Tombol submit
submit_lr = st.button("Submit Logistic Regression")
submit_svm = st.button("Submit Suport Vector Mechine")

# Memuat model sekali di awal
with open("LOGISTIC/lr_fish.pkl", mode='rb') as file:
    modelfruitlr = pickle.load(file)
with open("SVM/fishsvm.pkl", mode='rb') as file:
    modelfruitlr = pickle.load(file)

# Jika tombol ditekan, jalankan prediksi
if submit_lr:
    # Menyiapkan data input
    datapred = np.array([L, W, WLR]).reshape(1, -1)
    # Prediksi menggunakan model Logistic Regression
    result = modelfruitlr.predict(datapred)
    
    # Menampilkan hasil prediksi
    if result[0] == 0:
        st.write("Prediksi: Setipinna taty ")
    elif result[0] == 1:
        st.write("Prediksi: Anabas testudineus")
    elif result[0] == 2:
        st.write("Prediksi: Pethia conchonius")
    elif result[0] == 3:
        st.write("Prediksi: Otolithoides biauritus")
    elif result[0] == 4:
        st.write("Prediksi: Polynemus paradiseus")
    elif result[0] == 5:
        st.write("Prediksi: Sillaginopsis panijus ")
    elif result[0] == 6:
        st.write("Prediksi: Otolithoides pama ")
    elif result[0] == 7:
        st.write("Prediksi: Puntius lateristriga")
    elif result[0] == 8:
        st.write("Prediksi: Coilia dussumieri ")
    else:
        st.write("Prediksi tidak dikenal.")
elif submit_svm:
    # Menyiapkan data input
    datapred = np.array([L, W, WLR]).reshape(1, -1)
    # Prediksi menggunakan model Logistic Regression
    result = modelfruitlr.predict(datapred)
    
     # Menampilkan hasil prediksi
    if result[0] == 0:
        st.write("Prediksi: Setipinna taty ")
    elif result[0] == 1:
        st.write("Prediksi: Anabas testudineus")
    elif result[0] == 2:
        st.write("Prediksi: Pethia conchonius")
    elif result[0] == 3:
        st.write("Prediksi: Otolithoides biauritus")
    elif result[0] == 4:
        st.write("Prediksi: Polynemus paradiseus")
    elif result[0] == 5:
        st.write("Prediksi: Sillaginopsis panijus ")
    elif result[0] == 6:
        st.write("Prediksi: Otolithoides pama ")
    elif result[0] == 7:
        st.write("Prediksi: Puntius lateristriga")
    elif result[0] == 8:
        st.write("Prediksi: Coilia dussumieri ")
    else:
        st.write("Prediksi tidak dikenal.")