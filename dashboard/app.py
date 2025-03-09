import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime
from PIL import Image
import numpy as np
import time
import os
import plotly.express as px
import joblib
import plotly.graph_objects as go


# Loading Image using PIL
web_icon = Image.open('dashboard/image/dashboard-icon.png') # Adding Image to web app
st.set_page_config(page_title="Dashboard Prediction", layout="wide", initial_sidebar_state="auto", page_icon = web_icon)

# Dialog Input Nama
@st.dialog("Selamat Datang! 🎉")
def get_name():
    st.write("Silakan masukkan nama Anda untuk melanjutkan:")
    name = st.text_input("Nama Anda", key="user_name_input")
    
    if st.button("Masuk"):
        if name:
            st.session_state.user_name = name  # Simpan nama ke session_state
            st.rerun()
        else:
            st.warning("Silakan isi nama terlebih dahulu!")

# Periksa apakah pengguna sudah memasukkan nama sebelumnya
if "user_name" not in st.session_state:
    get_name()
else:
    # Tampilkan toast sambutan
    st.toast(f"Selamat datang, {st.session_state.user_name}! 🎉")
    time.sleep(0.5)
    st.toast("Semoga harimu menyenangkan! ☀️")
    time.sleep(0.5)
    st.toast("Ayo jelajahi dashboard ini!", icon="🚀")
    
# ======================================== Sidebar Configuration ========================================

with st.sidebar:
    # Gunakan f-string agar nilai user_name dari session_state bisa ditampilkan dengan benar
    if "user_name" in st.session_state: # Jika sudah ada nama, tampilkan nama
        st.markdown(f"""<h1 style='text-align: center; color: black;'>🙏 <strong>WELCOME</strong> 🙏<br><i>{st.session_state.user_name}</i>👋</h1>""", unsafe_allow_html=True)
    else: # Jika belum ada nama, tampilkan "Guest"
        st.markdown("""<h1 style='text-align: center; color: black;'>🙏 <strong>WELCOME</strong> 🙏<br><i>Guest</i>👋</h1>""", unsafe_allow_html=True)  # Jika belum ada nama, tampilkan "Guest"

    st.sidebar.image("https://i.pinimg.com/originals/fc/71/63/fc71635c7f1b09ed30413f59bb749582.gif", use_container_width=True)

    # Sidebar with two columns
    col1, col2 = st.columns(2)

    # Column 1: Social Media Badges
    with col1:
        # Instagram Badge (shields.io)
        st.markdown("[![Instagram Badge](https://img.shields.io/badge/Instagram-8a3ab9?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/rendika__07/?hl=en)")
        
        # GitHub Badge (shields.io)
        st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/Rendika7)")

    with col2:

        # WhatsApp Badge (shields.io)
        st.markdown("[![WhatsApp Badge](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/6281334814045)")
        
        # LinkedIn Badge (shields.io)
        st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/rendika-nurhartanto-s-882431218/)")

    # About Section ========================================
    with st.expander("Tentang Dashboard!"):
        st.markdown("""
        <div style="text-align: center;">
            🚀 <strong>Informasi Dashboard</strong> 🚀
            <hr style="border: 1px solid #ddd; width: 50%; margin: 10px auto;">
            <p><strong>Dashboard ini dirancang untuk memprediksi status siswa di Jaya Jaya Maju Institut</strong>, dengan tiga kategori utama: <strong>Enrolled</strong> (Terdaftar), <strong>Dropout</strong> (Putus Sekolah), dan <strong>Graduate</strong> (Lulus). 🎓</p>
            ♨ <strong>Tujuan utama Dashboard</strong> ♨
            <hr style="border: 1px solid #ddd; width: 50%; margin: 10px auto;">
            <p>⚡Dashboard dibuat untuk <strong>mendeteksi siswa yang berisiko putus sekolah</strong> dengan akurat, sehingga dapat diberikan <strong>bimbingan khusus</strong>✨ dan intervensi lebih awal. Dengan menggunakan model prediksi, dashboard ini memberikan wawasan yang berguna bagi pengambil keputusan dalam menangani masalah retensi siswa di institut. 🌟</p>
        </div>
        """, unsafe_allow_html=True)
        
# ======================================== Sidebar Configuration ========================================



# ======================================== Start Dashboard Here !!! ======================================== #

# # CSS untuk memposisikan tabs di tengah
# st.markdown("""
#     <style>
#         div[data-baseweb="tab-list"] {
#             display: flex;
#             justify-content: center;
#         }
#     </style>
# """, unsafe_allow_html=True)

# CSS untuk memposisikan tabs di tengah dan memperbesar ukuran tab
st.markdown("""
    <style>
        div[data-baseweb="tab-list"] {
            display: flex;
            justify-content: center;
            font-weight: bold;  /* Membuat teks tab lebih tebal */
            font-size: 30px;  /* Mengubah ukuran font tab */
        }
        /* Memperbesar ukuran tab */
        div[data-baseweb="tab-list"] > div {
            font-size: 30px;  /* Mengubah ukuran font tab */
            font-weight: bold;  /* Membuat teks tab lebih tebal */
            padding: 2px 1px;  /* Menambahkan padding agar lebih besar */
        }
        /* Menambahkan efek hover agar tab lebih interaktif */
        div[data-baseweb="tab-list"] > div:hover {
            background-color: #000000;  /* Mengubah warna background saat dihover */
            border-radius: 8px;
            transition: background-color 0.3s ease;
        }

        /* Tombol dengan kelas spesifik */
        [class="st-emotion-cache-89jlt8 egexzqm0"] {
            display: inline-block;
            text-align: center;
            text-decoration: none;
            # font-size: 18px;  /* Memperbesar ukuran font */
            padding: 6px 20px;  /* Menambahkan padding agar tombol lebih besar */
            width: 100%;  /* Membuat tombol mengisi lebar container */
            box-sizing: border-box;  /* Agar padding tidak mempengaruhi ukuran tombol */
            transition: background-color 0.3s ease; /* Efek transisi untuk hover */
        }
        
        /* Efek hover pada tombol */
        [class="st-emotion-cache-89jlt8 egexzqm0"]:hover {
            background-color: #ff3131;  /* Mengubah warna saat hover */
            color: #FFFFFF;  /* Pastikan warna teks tetap putih saat hover */
        }
    </style>
""", unsafe_allow_html=True)


# Membuat Tabs untuk membagi tampilan menjadi beberapa section
tab1, tab2, tab3 = st.tabs(["🏡 Home", "🔎 Predict Data", "📃 Download Data"])

with tab1:
    
    # Menampilkan banner gambar sebagai hero image  ========================================
    st.image(r'dashboard/image/Prediction Dashboard for Student Status.png', use_container_width=True)

    # Membuat DataFrame untuk menampilkan tabel
    data_diri = pd.DataFrame({
        "Nama": ["[Rendika Nurhartanto Suharto](https://www.linkedin.com/in/rendika-nurhartanto-s-882431218/)"],
        "Email": ["rendikarendi96@gmail.com"],
        "ID Dicoding": ["[RENDIKA NURHARTANTO SUHARTO](https://www.dicoding.com/users/rendika7/academies)"]
    })
    # Menampilkan tabel  ========================================
    st.table(data_diri)
    
with tab2:
    
    # Menampilkan banner gambar sebagai hero image  ========================================
    st.image(r'dashboard/image/Predict Banner.jpg', use_container_width=True)
    
    # Menambahkan dropdown button untuk memilih model ML
    st.markdown("""
    <style>
        .dropdown-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
            font-size: 20px;
        }
        .info-box {
            background-color: #f1f1f1;
            border-left: 5px solid #ff9800;
            padding: 16px;
            margin-top: 20px;
            font-size: 16px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .info-box h4 {
            color: #ff9800;
        }
        .info-box p {
            color: #333;
            font-size: 16px;
        }
        .metrics-container {
            display: flex;
            justify-content: flex-start;
            align-items: center;
            margin-top: 10px;
        }
        .metric {
            margin-right: 30px;
            font-size: 16px;
            color: #333;
        }
        .metric-label {
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Membuat dropdown model ML di tengah halaman
    model_choice = st.selectbox("Pilih Model Machine Learning", 
                                options=["Random_Forest", "LightGBM", "Gradient_Boosting"],
                                index=0)
    
    # Tampilkan informasi terkait model yang dipilih
    if model_choice == "Random_Forest":
        model_file_path = 'model/Random_Forest.pkl'
        model_info = """
        <div class="info-box">
            <h4>Random Forest Model</h4>
            <p><strong>Best Parameters:</strong> {'n_estimators': 100, 'min_samples_split': 5, 'min_samples_leaf': 4, 'max_features': 'log2', 'max_depth': 20}</p>
            <div class="metrics-container">
                <div class="metric"><span class="metric-label">Accuracy:</span> 0.7606</div>
                <div class="metric"><span class="metric-label">Precision:</span> 0.7423</div>
                <div class="metric"><span class="metric-label">Recall:</span> 0.7606</div>
                <div class="metric"><span class="metric-label">F1 Score:</span> 0.7437</div>
            </div>
        </div>
        """
    elif model_choice == "LightGBM":
        model_file_path = 'model/LightGBM.pkl'
        model_info = """
        <div class="info-box">
            <h4>LightGBM Model</h4>
            <p><strong>Best Parameters:</strong> {'subsample': 1.0, 'num_leaves': 31, 'n_estimators': 50, 'max_depth': 10, 'learning_rate': 0.05}</p>
            <div class="metrics-container">
                <div class="metric"><span class="metric-label">Accuracy:</span> 0.7621</div>
                <div class="metric"><span class="metric-label">Precision:</span> 0.7434</div>
                <div class="metric"><span class="metric-label">Recall:</span> 0.7621</div>
                <div class="metric"><span class="metric-label">F1 Score:</span> 0.7463</div>
            </div>
        </div>
        """
    elif model_choice == "Gradient_Boosting":
        model_file_path = 'model/Gradient_Boosting.pkl'
        model_info = """
        <div class="info-box">
            <h4>Gradient Boosting Model</h4>
            <p><strong>Best Parameters:</strong> {'subsample': 0.9, 'n_estimators': 50, 'max_depth': 5, 'learning_rate': 0.1}</p>
            <div class="metrics-container">
                <div class="metric"><span class="metric-label">Accuracy:</span> 0.7621</div>
                <div class="metric"><span class="metric-label">Precision:</span> 0.7471</div>
                <div class="metric"><span class="metric-label">Recall:</span> 0.7621</div>
                <div class="metric"><span class="metric-label">F1 Score:</span> 0.7502</div>
            </div>
        </div>
        """
    
    # Menampilkan informasi model yang dipilih
    st.markdown(model_info, unsafe_allow_html=True)
    
    # Muat model yang sudah disimpan menggunakan joblib
    loaded_model = joblib.load(model_file_path)
    
    tab_upload, = st.tabs(["⛓️‍💥 Upload & Predict"])
    
    with tab_upload:
        # Display info or warning message if no file is uploaded
        st.info("ℹ️ Jika Anda tidak memiliki data, silakan pergi ke menu '📃 Download Data'. Jika sudah, silakan langsung lakukan prediksi.")
        
        # Upload CSV or XLSX file
        uploaded_file = st.file_uploader("Masukkan Dataset", 
                                        type=["csv", "xlsx"], 
                                        key="fileuploader1")
        
        if uploaded_file is not None:
            modelPath = 'model'
            
            # ----------------- Load Scaler -----------------
            # Menentukan path untuk MinMaxScaler
            scaler_file_path = os.path.join(modelPath, 'minmax_scaler.pkl')

            # Memuat MinMaxScaler yang sudah disimpan
            scaler = joblib.load(scaler_file_path)
            
            df_inference = pd.read_csv(uploaded_file)
            
            inference_data_without_label = df_inference.drop(columns=['Status'], errors='ignore')

            inference_data_without_label = inference_data_without_label[['Application_mode', 'Debtor', 'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder', 'Age_at_enrollment', 'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade','Curricular_units_2nd_sem_enrolled', 'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade']]

            # Skalakan data inferensi menggunakan scaler yang sudah dimuat
            inference_data_scaled = scaler.transform(inference_data_without_label)

            # Melakukan prediksi menggunakan model yang telah dimuat
            model_predictions = loaded_model.predict(inference_data_scaled)
    
            st.write("Dataset Preview:")
            st.dataframe(inference_data_without_label.sample(5))

            # Menambahkan kolom prediksi ke dalam inference_data untuk masing-masing model
            inference_data_without_label[f'Predicted_Status'] = model_predictions
            
            st.write("Predict Results:")
            st.dataframe(inference_data_without_label)
            
            csv_results = inference_data_without_label.to_csv(index=False)
            
            st.download_button(
            label="Download Predict Results",
            data=csv_results,
            file_name="Result of Student Status Prediction.csv",
            mime="text/csv",
            icon=":material/download:")
            
with tab3:
    # Menampilkan banner gambar sebagai hero image  ========================================
    st.image(r'dashboard/image/Download Banner.jpg', use_container_width=True)
        
    
    kol1, kol2 = st.columns([2, 7])
    
    # Add custom CSS
    st.markdown("""
    <style>
        .info-box {
            background-color: #f1f1f1;
            border-left: 5px solid #ff9800;
            padding: 16px;
            margin-top: 20px;
            font-size: 16px;
            border-radius: 5px;
        }
        .info-box h4 {
            color: #ff9800;
        }
        [class="st-emotion-cache-ocsh0s e1d5ycv52"] {
            display: inline-block;
            padding: 5px 20px;
            background-color: #4A55A2;
            color: #FFFFFF;
            width: 100%; /* Membuat tombol memenuhi lebar kolom/container */
            height: 100px;
            text-align: center;
            text-decoration: none;
            font-size: 28px;
            border-radius: 8px;
            box-sizing: border-box; /* Agar padding tidak mempengaruhi ukuran tombol */
        }
        [class="st-emotion-cache-ocsh0s e1d5ycv52"]:hover {
            background-color: #3a47a1;
        }
    </style>
    """, unsafe_allow_html=True)
        
    with kol1:
        st.markdown("""<br>""", unsafe_allow_html=True)  # Jika belum ada nama, tampilkan "Guest"
        # Add download button for a sample dataset
        sample_data = pd.read_csv(r"dataset/data_inference.csv")
        csv = sample_data.to_csv(index=False)

        st.download_button(
            label="Download Sample Dataset",
            data=csv,
            file_name="sample_student_data.csv",
            mime="text/csv",
            icon=":material/download:"
        )
    
    with kol2:
        
        # Display info about prediction with a stylish box
        st.markdown("""
        <div class="info-box">
            <h4>ℹ️ Info:</h4>
            Jika sudah memiliki data yang sesuai, silakan pindah ke menu '🔎 Predict Data'.
        </div>
        """, unsafe_allow_html=True)