MW_convert = 10**6  # 1 MW = 10^6 W
konversi_energi= 0.90 #90%
g= 9.80 #percepatan gravitasi
densitiy_air = 1000 #massa satu meeter kubik

height= int(input("Masukkan tinggi bendungan (m): "))
flow_rate= int(input("Masukkan aliran air: "))

m= densitiy_air * flow_rate #mencari massa perdetik (m)

w= m*g*height  #rumus energi potensial

power_electric = konversi_energi * w #mencari tenaga listrik setelah efisiensi

megawat = power_electric / MW_convert  #konversi wat ke megawat 

print(f"daya yang dihasilkan dari bendungan adalah: {megawat:,.1f} MW")