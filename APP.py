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

# Memuat model sekali di awal
with open("LOGISTIC/lr_fruit.pkl", mode='rb') as file:
    modelfruitknn = pickle.load(file)

# Jika tombol ditekan, jalankan prediksi
if submit_lr:
    # Menyiapkan data input
    datapred = np.array([D, W, R, G, B]).reshape(1, -1)
    # Prediksi menggunakan model Logistic Regression
    result = modelfruitknn.predict(datapred)
    
    # Menampilkan hasil prediksi
    if result[0] == 0:
        st.write("Prediksi: Grapefruit")
    elif result[0] == 1:
        st.write("Prediksi: Orange")
    else:
        st.write("Prediksi tidak dikenal.")
