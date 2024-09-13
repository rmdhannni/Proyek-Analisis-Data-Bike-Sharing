import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Fungsi untuk memuat data
@st.cache_data
def load_data():
    hour_df = pd.read_csv('../data/hour.csv')
    day_df = pd.read_csv('../data/day.csv')
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
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
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

# Clustering Manual Based on Time and Weather
st.subheader('Manual Clustering Based on Time and Weather')

# Binning Hour Data
hour_df['hour_bin'] = pd.cut(hour_df['hr'], bins=[0, 6, 12, 18, 24], labels=['Night', 'Morning', 'Afternoon', 'Evening'])

# Average rentals per time bin
avg_rentals_time_bin = hour_df.groupby('hour_bin')['cnt'].mean().reset_index()

# Visualisasi Binning
st.subheader('Jumlah Penyewaan Sepeda Berdasarkan Waktu')
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=avg_rentals_time_bin, x='hour_bin', y='cnt', palette='coolwarm', ax=ax)
ax.set_title('Rata-rata Jumlah Penyewaan Sepeda Berdasarkan Waktu', fontsize=14)
ax.set_xlabel('Waktu', fontsize=12)
ax.set_ylabel('Jumlah Penyewaan', fontsize=12)
st.pyplot(fig)

# Visualization of Weather Impact
st.subheader('Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda')
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(data=hour_df, x='weathersit', y='cnt', palette='Set2', ax=ax)
ax.set_title('Distribusi Jumlah Penyewaan Sepeda Berdasarkan Cuaca', fontsize=14)
ax.set_xlabel('Kondisi Cuaca', fontsize=12)
ax.set_ylabel('Jumlah Penyewaan', fontsize=12)
st.pyplot(fig)

# Visualization of Rentals by Day of Week
st.subheader('Jumlah Penyewaan Sepeda Berdasarkan Hari dalam Seminggu')
fig, ax = plt.subplots(figsize=(12, 6))
day_df['weekday'] = pd.to_datetime(day_df['dteday']).dt.day_name()
sns.lineplot(data=day_df, x='weekday', y='cnt', hue='season', palette='Paired', ax=ax)
ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Hari dan Musim', fontsize=14)
ax.set_xlabel('Hari dalam Seminggu', fontsize=12)
ax.set_ylabel('Jumlah Penyewaan', fontsize=12)
st.pyplot(fig)

# Kesimpulan
st.header('Conclusion')
st.write("""
- **Pertanyaan 1:** Faktor-faktor seperti waktu hari dan kondisi cuaca memiliki pengaruh signifikan terhadap jumlah penyewaan sepeda. Visualisasi binning berdasarkan waktu memberikan wawasan tentang pola penyewaan sepanjang hari.
- **Pertanyaan 2:** Pola penyewaan sepeda bervariasi tergantung pada kondisi cuaca dan hari dalam minggu, dengan perbedaan signifikan di setiap musim.
""")
