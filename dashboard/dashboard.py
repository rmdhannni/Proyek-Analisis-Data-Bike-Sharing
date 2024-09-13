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

# Pertanyaan 1: Apa faktor-faktor yang mempengaruhi jumlah penyewaan sepeda dalam periode waktu tertentu?
st.subheader('Pertanyaan 1: Faktor-faktor yang mempengaruhi jumlah penyewaan sepeda')

# Menghitung rata-rata jumlah penyewaan berdasarkan jam
avg_rentals_per_hour = hour_df.groupby('hr')['cnt'].mean().reset_index()

# Visualisasi rata-rata penyewaan berdasarkan jam
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(data=avg_rentals_per_hour, x='hr', y='cnt', palette='coolwarm', ax=ax)
ax.set_title('Rata-rata Jumlah Penyewaan Sepeda per Jam', fontsize=14)
ax.set_xlabel('Jam', fontsize=12)
ax.set_ylabel('Jumlah Penyewaan', fontsize=12)
ax.grid(True)
st.pyplot(fig)

# Penjelasan untuk Pertanyaan 1
st.write("""
**Penjelasan:** 
Grafik Bar ini menunjukkan rata-rata jumlah penyewaan sepeda untuk setiap jam dalam sehari. Dengan melihat grafik ini, kita dapat mengidentifikasi jam-jam tertentu yang memiliki jumlah penyewaan yang lebih tinggi atau lebih rendah. Ini membantu dalam memahami pola penyewaan sepeda sepanjang hari, dan bisa digunakan untuk merencanakan promosi atau penjadwalan yang lebih efektif.
""")

# Pertanyaan 2: Bagaimana pola penyewaan sepeda berdasarkan waktu dan kondisi cuaca?
st.subheader('Pertanyaan 2: Pola penyewaan sepeda berdasarkan waktu dan kondisi cuaca')

# Visualisasi jumlah penyewaan berdasarkan waktu dan kondisi cuaca
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=day_df, x='dteday', y='cnt', hue='season', palette='Paired', ax=ax)
ax.set_title('Jumlah Penyewaan Sepeda per Hari Berdasarkan Musim', fontsize=14)
ax.set_xlabel('Tanggal', fontsize=12)
ax.set_ylabel('Jumlah Penyewaan', fontsize=12)
ax.grid(True)
st.pyplot(fig)

# Visualisasi distribusi penyewaan berdasarkan cuaca
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(data=hour_df, x='weathersit', y='cnt', palette='Set2', ax=ax)
ax.set_title('Distribusi Jumlah Penyewaan Sepeda Berdasarkan Cuaca', fontsize=14)
ax.set_xlabel('Kondisi Cuaca', fontsize=12)
ax.set_ylabel('Jumlah Penyewaan', fontsize=12)
ax.grid(True)
st.pyplot(fig)

# Penjelasan untuk Pertanyaan 2
st.write("""
**Penjelasan:** 
- **Jumlah Penyewaan Sepeda per Hari Berdasarkan Musim:** Grafik Garis ini menunjukkan jumlah penyewaan sepeda setiap hari sepanjang tahun, dikelompokkan berdasarkan musim. Ini memberikan wawasan tentang bagaimana jumlah penyewaan berubah seiring dengan perubahan musim dan membantu kita memahami tren musiman dalam penyewaan sepeda.

- **Distribusi Jumlah Penyewaan Sepeda Berdasarkan Cuaca:** Boxplot ini menampilkan distribusi jumlah penyewaan sepeda berdasarkan kondisi cuaca. Dengan melihat boxplot ini, kita dapat memahami bagaimana kondisi cuaca yang berbeda mempengaruhi jumlah penyewaan sepeda. Misalnya, kondisi cuaca buruk mungkin mengurangi jumlah penyewaan secara signifikan.
""")

# Kesimpulan
st.header('Kesimpulan')
st.write("""
- **Pertanyaan 1:** Faktor-faktor seperti jam hari memiliki pengaruh signifikan terhadap jumlah penyewaan sepeda. Dari visualisasi bar, dapat dilihat bahwa beberapa jam tertentu memiliki jumlah penyewaan yang lebih tinggi dibandingkan dengan jam lainnya. Ini memberikan informasi berharga untuk perencanaan operasional dan strategi pemasaran.

- **Pertanyaan 2:** Pola penyewaan sepeda bervariasi tergantung pada musim dan kondisi cuaca. Grafik garis menunjukkan bahwa jumlah penyewaan bervariasi sepanjang tahun dan berbeda menurut musim, sedangkan boxplot menunjukkan bagaimana kondisi cuaca mempengaruhi distribusi jumlah penyewaan sepeda. Informasi ini bisa digunakan untuk meningkatkan pengalaman pengguna dan optimasi operasional.
""")
