import flask
import os
import os


print ("Selamat datang di website Santri DigiTrack")

print ('\n')
print ('\n')
# Contoh script login sederhana
# Mendefinisikan variabel username dan password
username = "admin"
password = "password123"

# Meminta input dari pengguna
input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")

# Membandingkan input dengan data yang tersimpan

if input_username == username and input_password == password:
    print("Login berhasil!")
else:
    print("Login gagal! Silakan coba lagi.")
