import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import streamlit as st

# Mengatur path file data
DATA_PATH = '../data/'

# Cek jika file ada
if os.path.exists(f'{DATA_PATH}hour.csv'):
    hour_df = pd.read_csv(f'{DATA_PATH}hour.csv')
else:
    st.error("File 'hour.csv' tidak ditemukan.")

# Lanjutkan dengan kode lainnya


# Menyediakan informasi identitas
def display_sidebar():
    st.sidebar.title("About Me")
    st.sidebar.write("Yusuf Rahmdhani Asy'Ari")
    st.sidebar.write("ggdani137@gmail.com") 
    st.sidebar.write("@rmdhannni") 

# Memanggil fungsi untuk menampilkan sidebar
display_sidebar()


# Memuat data
hour_df = pd.read_csv('../data/hour.csv')
day_df = pd.read_csv('../data/day.csv')

# Konversi kolom 'dteday' menjadi tipe datetime
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

st.title('Analisis Data Bike Sharing')

# Statistik Deskriptif
st.header('Statistik Deskriptif')
st.write('**Hour Data**')
st.write(hour_df.describe())
st.write('**Day Data**')
st.write(day_df.describe())

# Visualisasi
st.header('Visualisasi Data')

# Penyewaan Sepeda per Jam
st.subheader('Penyewaan Sepeda per Jam')
fig, ax = plt.subplots(figsize=(12, 6))
hour_df.groupby('hr')['cnt'].mean().plot(kind='bar', ax=ax)
ax.set_title('Rata-rata Jumlah Penyewaan Sepeda per Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Penyewaan Sepeda per Hari dan Musim
st.subheader('Penyewaan Sepeda per Hari berdasarkan Musim')
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=day_df, x='dteday', y='cnt', hue='season', ax=ax)
ax.set_title('Jumlah Penyewaan Sepeda per Hari berdasarkan Musim')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Penyewaan Sepeda Berdasarkan Cuaca
st.subheader('Penyewaan Sepeda Berdasarkan Cuaca')
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(data=hour_df, x='weathersit', y='cnt', ax=ax)
ax.set_title('Jumlah Penyewaan Sepeda berdasarkan Kondisi Cuaca')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Analisis Korelasi
st.header('Analisis Korelasi')
correlation = hour_df[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
ax.set_title('Korelasi antara Fitur dan Jumlah Penyewaan Sepeda')
st.pyplot(fig)

# Deteksi Anomali
st.header('Deteksi Anomali')
threshold = hour_df['cnt'].quantile(0.95)
anomalies = hour_df[hour_df['cnt'] > threshold]
st.write(anomalies[['dteday', 'hr', 'cnt']])




