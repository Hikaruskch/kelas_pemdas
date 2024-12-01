print("Rahadrin Muhammad Hikaru Faqath Sechan")
print("15-2023-128")
print("Informaatika Itenas")
data_panen = {
    'lokasi1':{
        'nama_lokasi':'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2':{
        'nama_lokasi':'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
        'lokasi3':{
        'nama_lokasi':'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
        'lokasi4':{
        'nama_lokasi':'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
        'lokasi5':{
        'nama_lokasi':'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }              
}

# Soal no 1
print ("Data Panen Bos!")
print (data_panen)

# Soal no 2
print("Jumlah Hasil Panen di Lokasi 2:",data_panen['lokasi2']['hasil_panen']['jagung'])

# Soal no 3
print ("Nama Lokasi dari Lokasi 3:",data_panen['lokasi3']['nama_lokasi'])

# Soal no 4
padi = {}
kedelai = {}

for lokasi, hasil in data_panen.items():
    padi[lokasi] = hasil ['hasil_panen']['padi']
    kedelai[lokasi] = hasil ['hasil_panen']['kedelai']
    
print ("Hasil Panen Padi:", padi)
print ("Hasil Panen Kedelai:",kedelai)

# Soal no 5 and 6
for lokasi, hasil in data_panen.items():
    padi = hasil ['hasil_panen']['padi']
    jagung = hasil ['hasil_panen']['jagung']
    
    if padi > 1300 or jagung > 800:
        print ("Lokasi Memerlukan Perhatian Khusus, untuk lokasi")
    else:
        print ("Lokasi dalam kondisi Baik")
    

