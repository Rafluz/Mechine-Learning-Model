import streamlit as st
import numpy as np
import pickle
import streamlit.components.v1 as components
import sys
import os

# Menambahkan direktori luar ke path agar bisa mengimpor fish.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'APP')))
import Fish  # Mengimpor Fish dari folder yang sama

# Fungsi prediksi
def predict_fruit(model, data):
    result = model.predict(data)
    if result[0] == 0:
        return "Grapefruit"
    elif result[0] == 1:
        return "Orange"
    else:
        return None

def show_notification(image_url, message):
    html_code = f"""
    <style>
        .notification {{
            display: none;
            min-width: 300px;
            background-color: #555;
            color: white;
            text-align: center;
            border-radius: 5px;
            padding: 16px;
            position: fixed;
            z-index: 99999;
            left: 50%;
            top: 10px; /* Pastikan posisi di bagian atas layar */
            transform: translate(-50%, 0);
            font-size: 17px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }}

        .notification.show {{
            display: block;
            animation: fadein 0.5s, fadeout 0.5s 2.5s;
        }}

        @keyframes fadein {{
            from {{top: -50px; opacity: 0;}}
            to {{top: 10px; opacity: 1;}}
        }}

        @keyframes fadeout {{
            from {{top: 10px; opacity: 1;}}
            to {{top: -50px; opacity: 0;}}
        }}

        /* Pastikan kontainer Streamlit tidak membatasi overflow */
        [data-testid="stAppViewContainer"] {{
            overflow: visible !important;
        }}
    </style>

    <div class="notification" id="notification">
        <img src="{image_url}" alt="Notification Image" 
             style="width: 50px; height: auto; margin-right: 10px; vertical-align: middle;">
        <span>{message}</span>
    </div>

    <script>
        var notification = document.getElementById("notification");
        notification.classList.remove("show");
        setTimeout(function() {{
            notification.classList.add("show");
        }}, 100);
        setTimeout(function() {{
            notification.classList.remove("show");
        }}, 3000);
    </script>
    """
    components.html(html_code, height=200)



# Sidebar navigasi
st.sidebar.title("Navigation")
app_choice = st.sidebar.selectbox("Choose Dataset:", ["Fruit Prediction", "Fish Prediction"])

# Jika pengguna memilih aplikasi Fruit Prediction
if app_choice == "Fruit Prediction":
    st.title('Fruit Prediction App')

    # Input pengguna
    D = float(st.number_input("Diameter ", step=0.1))
    W = float(st.number_input("Weight ", step=0.1))
    R = float(st.number_input("Red ", step=0.1))
    G = float(st.number_input("Green ", step=0.1))
    B = float(st.number_input("Blue ", step=0.1))

    # Tombol submit
    submit_fruitlr = st.button("Submit Logistic Regression")
    submit_fruitsvm = st.button("Submit Support Vector Machine")

    # Memuat model sekali di awal
    try:
        with open("LOGISTIC/lr_fruit.pkl", mode='rb') as file:
            modelfruitlr = pickle.load(file)
        with open("SVM/fruitsvm.pkl", mode='rb') as file:
            modelfruitsvm = pickle.load(file)
    except FileNotFoundError:
        st.error("Model file not found. Please ensure the model files are in the correct directory.")

    # Jika tombol Logistic Regression ditekan
    if submit_fruitlr:
        submit_fruitsvm = False  # Reset SVM button
        datapred = np.array([D, W, R, G, B]).reshape(1, -1)
        prediction = predict_fruit(modelfruitlr, datapred)
        
        if prediction == "Grapefruit":
            show_notification("https://cdn.pixabay.com/photo/2013/07/12/19/16/grapefruit-154469_960_720.png", "Grapefruit")
        elif prediction == "Orange":
            show_notification("https://cdn.pixabay.com/photo/2016/03/03/17/15/fruit-1234657_1280.png", "Orange")

    # Jika tombol SVM ditekan
    if submit_fruitsvm:
        submit_fruitlr = False  # Reset Logistic Regression button
        datapred = np.array([D, W, R, G, B]).reshape(1, -1)
        prediction = predict_fruit(modelfruitsvm, datapred)
        
        if prediction == "Grapefruit":
            show_notification("https://cdn.pixabay.com/photo/2013/07/12/19/16/grapefruit-154469_960_720.png", "Grapefruit")
        elif prediction == "Orange":
            show_notification("https://cdn.pixabay.com/photo/2016/03/03/17/15/fruit-1234657_1280.png", "Orange")

# Jika pengguna memilih aplikasi Fish Prediction
elif app_choice == "Fish Prediction":
    st.title('Fish Prediction App')
    Fish.render_fish_app()  # Panggil fungsi utama di Fish.py jika tersedia
