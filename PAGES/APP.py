import streamlit as st
import numpy as np
import pickle
import Fish  

# Set konfigurasi halaman
# st.set_page_config(page_title="Fruit and Fish App")

# Sidebar navigasi
st.sidebar.title("Navigation")
app_choice = st.sidebar.selectbox("Choose Dataset:", ["Fruit Prediction", "Fish Prediction"])

# Jika pengguna memilih aplikasi Fruit Prediction
if app_choice == "Fruit Prediction":
    st.title('Fruit Prediction App')

    # Input pengguna
    D = float(st.number_input("Diameter "))
    W = float(st.number_input("Weight "))
    R = float(st.number_input("Red "))
    G = float(st.number_input("Green "))
    B = float(st.number_input("Blue "))

    # Tombol submit
    submit_lr = st.button("Submit Logistic Regression")
    submit_svm = st.button("Submit Support Vector Machine")

    # Memuat model sekali di awal
    with open("LOGISTIC/lr_fruit.pkl", mode='rb') as file:
        modelfruitlr = pickle.load(file)
    with open("SVM/fruitsvm.pkl", mode='rb') as file:
        modelfruitsvm = pickle.load(file)

    # Jika tombol ditekan, jalankan prediksi
    if submit_lr:
        datapred = np.array([D, W, R, G, B]).reshape(1, -1)
        result = modelfruitlr.predict(datapred)
        if result[0] == 0:
            st.write("Prediksi: Grapefruit")
        elif result[0] == 1:
            st.write("Prediksi: Orange")
        else:
            st.write("Prediksi tidak dikenal.")
    elif submit_svm:
        datapred = np.array([D, W, R, G, B]).reshape(1, -1)
        result = modelfruitsvm.predict(datapred)
        if result[0] == 0:
            st.write("Prediksi: Grapefruit")
        elif result[0] == 1:
            st.write("Prediksi: Orange")
        else:
            st.write("Prediksi tidak dikenal.")

# Jika pengguna memilih aplikasi Fish Prediction
elif app_choice == "Fish Prediction":
    st.title('Fish Prediction App')
    Fish.render_fish_app()  # Panggil fungsi utama di Fish.py
