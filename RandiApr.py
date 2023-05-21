import pandas as pd

#import dataset
dataset= pd.read_csv('InternetUser.csv')

#Tampilkan 5 baris pertama dari dataset
print(dataset.head())

#cek jumlah missing values pada kolom
print(dataset['Online_Gaming'].isna().sum())

#mengganti missing values pada kolom dengan nilai baru
dataset['Online_Gaming'].fillna('N', inplace=True)

#cek kembali jumlah missing values pada kolom
print(dataset['Online_Gaming'].isna().sum())

#cek kembali jumlah missing values pada kolom
print(dataset['Read_News'].isna().sum())

#mengganti missing values pada kolom dengan nilai baru
dataset['Read_News'].fillna('N', inplace=True)

# cek kembali jumlah missing values pada kolom
print(dataset['Read_News'].isna().sum())

#cek kembali jumlah missing values pada kolom
print(dataset['Other_Social_Network'].isna().sum())

#mengganti missing values pada kolom dengan nilai baru
dataset['Other_Social_Network'].fillna('N', inplace=True)

# cek kembali jumlah missing values pada kolom
print(dataset['Other_Social_Network'].isna().sum())

# Ubah Nilai yang tidak konsisten pada atribut
dataset['Twitter'].replace(['99'], ['N'], inplace=True)

#Tampilkan hasil perubahan
print(dataset['Twitter'].value_counts())
