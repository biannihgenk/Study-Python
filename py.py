import pandas as pd

# 1. Memuat dataset
df = pd.read_excel('student_innovation_assessment_dataset.xlsx')

# 2. Membersihkan kolom 'innovation_index'
# Menghilangkan teks "approx ", mengganti koma dengan titik, lalu mengubahnya menjadi numerik (float)
df['innovation_index'] = df['innovation_index'].astype(str).str.replace('approx ', '', regex=False)
df['innovation_index'] = df['innovation_index'].str.replace(',', '.', regex=False)
df['innovation_index'] = pd.to_numeric(df['innovation_index'], errors='coerce')

# 3. Membersihkan kolom 'innovation_readiness_level'
# Menghapus spasi berlebih di awal/akhir dan membuat format teks menjadi Title Case
df['innovation_readiness_level'] = df['innovation_readiness_level'].str.strip().str.title()

# Menyeragamkan istilah (mapping) ke dalam 3 kategori standar bahasa Inggris
level_mapping = {
    'Pemula': 'Beginner',
    'Basic': 'Beginner',
    'Berkembang': 'Developing',
    'Intermediate': 'Developing', 
    'Calon Innovator': 'Developing',
    'Mahir': 'Advanced',
    'Super Innovator': 'Advanced', 
    'Future Innovator': 'Advanced', 
    'Innovator': 'Advanced', 
    'Level 5': 'Not Classified'
}
df['innovation_readiness_level'] = df['innovation_readiness_level'].replace(level_mapping)

# 4. Menangani Outlier pada 'innovation_index'
# Opsional: Membatasi (clipping) nilai agar tidak kurang dari 0 dan tidak lebih dari 100
df['innovation_index'] = df['innovation_index'].clip(lower=0, upper=100)

# Cek hasil akhir
print(df.info())
print(df['innovation_readiness_level'].value_counts())