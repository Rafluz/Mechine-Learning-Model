import streamlit as st
import numpy as np
import pickle
import streamlit.components.v1 as components

def render_fish_app():

    # Fungsi untuk prediksi ikan
    def predict_fish(model, data):
        result = model.predict(data)
        if result[0] == 0:
            return "Setipinna taty"
        elif result[0] == 1:
            return "Anabas testudineus"
        elif result[0] == 2:
            return "Pethia conchonius"
        elif result[0] == 3:
            return "Otolithoides biauritus"
        elif result[0] == 4:
            return "Polynemus paradiseus"
        elif result[0] == 5:
            return "Sillaginopsis panijus"
        elif result[0] == 6:
            return "Otolithoides pama"
        elif result[0] == 7:
            return "Puntius lateristriga"
        elif result[0] == 8:
            return "Coilia dussumieri"
        else:
            return "Prediksi tidak dikenal."

    # Fungsi untuk menampilkan notifikasi
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
                top: 10px;
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

    # Input dari pengguna
    st.title("Fish Species Prediction")
    L = st.number_input("Length (Panjang) in cm", min_value=0.0, step=0.1)
    W = st.number_input("Weight (Berat) in grams", min_value=0.0, step=0.1)
    WLR = st.number_input("W|L Ratio (Rasio Berat ke Panjang)", min_value=0.0, step=0.01)

    # Tombol submit
    submit_fishlr = st.button("Submit Logistic Regression")
    submit_fishsvm = st.button("Submit Support Vector Machine")

    # Memuat model
    try:
        with open("LOGISTIC/lr_fish.pkl", "rb") as file:
            modelfishlr = pickle.load(file)
        with open("SVM/fishsvm.pkl", "rb") as file:
            modelfishsvm = pickle.load(file)
    except FileNotFoundError:
        st.error("Model file not found. Please ensure the model files are in the correct directory.")
        return

    # Reset tombol dan status ketika salah satu tombol diklik
    if submit_fishlr:
        submit_fishsvm = False  # Reset SVM button
        datapred = np.array([L, W, WLR]).reshape(1, -1)
        prediction = predict_fish(modelfishlr, datapred)
        fish_images = {
            "Setipinna taty": "https://p1.ssl.qhimg.com/t01e4b7cbe48641d770.jpg",
            "Anabas testudineus": "https://th.bing.com/th/id/OIP.zpO_HIrcyQkMq7UqRsDD2AHaEo",
            "Pethia conchonius": "https://www.researchgate.net/profile/Heok-Tan/publication/341868681/figure/fig20/AS:898282083594240@1591178546035/Pethia-conchonius-428-mm-SL.jpg",
            "Otolithoides biauritus": "https://marinebiodiversity.org.bd/wp-content/uploads/2024/01/Otolithoides-biauritus_ABR-LAB-300x179.jpg",
            "Polynemus paradiseus": "https://marinebiodiversity.org.bd/wp-content/uploads/2024/01/Polynemus-paradiseus_ABR-LAB.jpg",
            "Sillaginopsis panijus": "https://marinebiodiversity.org.bd/wp-content/uploads/2024/01/Sillaginopsis-panijus_ABR-LAB.jpg",
            "Otolithoides pama": "https://marinebiodiversity.org.bd/wp-content/uploads/2024/01/Otolithoides-pama_F1602sb-49-1_MF621553-300x180.jpg",
            "Puntius lateristriga": "https://www.universaquatique.fr/23436-large_default/barbus-puntius-lateristriga-7cm.jpg",
            "Coilia dussumieri": "https://upload.wikimedia.org/wikipedia/commons/6/63/Coilia_dussumieri.jpg",
        }

        # Tampilkan notifikasi
        image_url = fish_images.get(prediction, "")
        show_notification(image_url, prediction)

    if submit_fishsvm:
        submit_fishlr = False  # Reset Logistic Regression button
        datapred = np.array([L, W, WLR]).reshape(1, -1)
        prediction = predict_fish(modelfishsvm, datapred)
        fish_images = {
            "Setipinna taty": "https://p1.ssl.qhimg.com/t01e4b7cbe48641d770.jpg",
            "Anabas testudineus": "https://th.bing.com/th/id/OIP.zpO_HIrcyQkMq7UqRsDD2AHaEo",
            "Pethia conchonius": "https://www.researchgate.net/profile/Heok-Tan/publication/341868681/figure/fig20/AS:898282083594240@1591178546035/Pethia-conchonius-428-mm-SL.jpg",
            "Otolithoides biauritus": "https://marinebiodiversity.org.bd/wp-content/uploads/2024/01/Otolithoides-biauritus_ABR-LAB-300x179.jpg",
            "Polynemus paradiseus": "https://marinebiodiversity.org.bd/wp-content/uploads/2024/01/Polynemus-paradiseus_ABR-LAB.jpg",
            "Sillaginopsis panijus": "https://marinebiodiversity.org.bd/wp-content/uploads/2024/01/Sillaginopsis-panijus_ABR-LAB.jpg",
            "Otolithoides pama": "https://marinebiodiversity.org.bd/wp-content/uploads/2024/01/Otolithoides-pama_F1602sb-49-1_MF621553-300x180.jpg",
            "Puntius lateristriga": "https://www.universaquatique.fr/23436-large_default/barbus-puntius-lateristriga-7cm.jpg",
            "Coilia dussumieri": "https://upload.wikimedia.org/wikipedia/commons/6/63/Coilia_dussumieri.jpg",
        }

        # Tampilkan notifikasi
        image_url = fish_images.get(prediction, "")
        show_notification(image_url, prediction)
