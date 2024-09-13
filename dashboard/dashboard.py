import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Fungsi untuk memuat data
@st.cache_data
def load_data():
    hour_df = pd.read_csv('data/hour.csv')
    day_df = pd.read_csv('data/day.csv')
    return hour_df, day_df

# Sidebar
def display_sidebar():
    st.sidebar.title("About Me")
    st.sidebar.write("**Nama:** Yusuf Rahmadhani Asy'Ari")
    st.sidebar.write("**Email:** ggdani137@gmail.com")
    st.sidebar.write("**ID Dicoding:** rmdhannni")

# Load data
hour_df, day_df = load_data()

# Sidebar
display_sidebar()

# Title and Introduction
st.title('Proyek Analisis Data: Bike Sharing Dataset')
st.write("""
- **Nama:** Yusuf Rahmadhani Asy'Ari  
- **Email:** ggdani137@gmail.com  
- **ID Dicoding:** rmdhannni  
""")

st.header('Menentukan Pertanyaan Bisnis')
st.write("""
1. Apa faktor-faktor yang mempengaruhi jumlah penyewaan sepeda dalam periode waktu tertentu?  
2. Bagaimana pola penyewaan sepeda berdasarkan waktu dan kondisi cuaca?
""")

# Import Library Section
st.header('Import Semua Packages/Library yang Digunakan')
st.code("""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
""", language='python')

# Data Wrangling Section
st.header('Data Wrangling')
st.subheader('Gathering Data')
st.write("**Insight:** Dataset berhasil dimuat dan siap untuk analisis.")

# Display the loaded data
st.subheader('Hour Dataset')
st.write(hour_df.head())

st.subheader('Day Dataset')
st.write(day_df.head())

# Exploratory Data Analysis (EDA)
st.header('Exploratory Data Analysis (EDA)')

# RFM Analysis
st.subheader('Explore RFM Analysis')

# Konversi kolom 'dteday' menjadi datetime
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Buat DataFrame RFM
rfm_df = hour_df[['dteday', 'cnt']].copy()
rfm_df['Recency'] = (rfm_df['dteday'].max() - rfm_df['dteday']).dt.days
rfm_df['Frequency'] = rfm_df['cnt']
rfm_df['Monetary'] = rfm_df['cnt']

# Drop kolom yang tidak diperlukan
rfm_df.drop('dteday', axis=1, inplace=True)

# Segmentasi menggunakan KMeans
kmeans = KMeans(n_clusters=3, random_state=0)
rfm_df['Cluster'] = kmeans.fit_predict(rfm_df[['Recency', 'Frequency', 'Monetary']])

# Tampilkan hasil RFM
st.write(rfm_df.head())

# Visualisasi RFM
st.subheader('Visualisasi RFM Analysis')
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=rfm_df, x='Recency', y='Frequency', hue='Cluster', palette='viridis', ax=ax)
ax.set_title('Segmentasi Pelanggan Berdasarkan Analisis RFM')
ax.set_xlabel('Recency')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Visualization & Explanatory Analysis
st.header('Visualization & Explanatory Analysis')

# Pertanyaan 1: Faktor yang mempengaruhi jumlah penyewaan sepeda
st.subheader('Pertanyaan 1: Faktor-faktor yang mempengaruhi jumlah penyewaan sepeda')
fig, ax = plt.subplots(figsize=(12, 6))
hour_df.groupby('hr')['cnt'].mean().plot(kind='bar', ax=ax)
ax.set_title('Rata-rata Jumlah Penyewaan Sepeda per Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Pertanyaan 2: Pola penyewaan sepeda berdasarkan waktu dan kondisi cuaca
st.subheader('Pertanyaan 2: Pola penyewaan sepeda berdasarkan waktu dan kondisi cuaca')
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=day_df, x='dteday', y='cnt', hue='season', ax=ax)
ax.set_title('Jumlah Penyewaan Sepeda per Hari Berdasarkan Musim')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Kesimpulan
st.header('Conclusion')
st.write("""
- **Pertanyaan 1:** Faktor-faktor seperti cuaca dan waktu memiliki pengaruh signifikan terhadap jumlah penyewaan sepeda. Analisis RFM memberikan wawasan tentang segmen pelanggan yang berbeda dan pola penyewaan mereka.
- **Pertanyaan 2:** Pola penyewaan sepeda bervariasi tergantung pada kondisi cuaca dan waktu hari, dengan variasi yang signifikan pada jam-jam tertentu.
""")
