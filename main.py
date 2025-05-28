kamus_meme = {
    "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
    "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
    "SKIBIDI": "Seuatu yang keren",
    "SIGMA": "Sifat keren",
    "MEWING": "Menunjukkan sisi psikopat",
    "ROFL" : "Tanggapan terhadap lelucon",
    "SHEESH" : "Sedikit ketidaksetujuan"
}

print("Selamat datang di kamus istilah gaul!")
print("Saya akan membantu Anda memahami beberapa kata gaul yang Anda tidak tahu.")
print("Anda akan diminta untuk memasukkan 5 kata. ")
print("-" * 50)

for i in range(5):
    print("Kata ke-",i+1)
    word = input("Masukkan kata yang ingin Anda cari").upper()
    
    if word in meme_dict.keys():
        print("Berikut artinya:", kamus_meme[word])
    else:
        print("Maaf, kata",word,  "belum tersedia dalam kamus ini.")
    print("-" * 50)

print("Terima kasih telah menggunakan kamus istilah gaul!")
