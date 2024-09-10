x1 = float(input("Masukkan titik X1: "))
y1 = float(input("Masukkan titik Y1: "))
x2 = float(input("Masukkan titik X2: "))
y2 = float(input("masukkan titik Y2: "))

gradien = (y2-y1)/(x2-x1) #mencari garis miring

x_mid = (x1+x2)/2 #titik tengah x
y_mid = (y1+y2)/2 #titik tengah y

gradien_tegak_lurus = -1 / gradien #mencari gradien tegak lurus dengan rumus m2= -1/m1

Titik_potong_terhadap_sumbu_Y= y_mid - gradien_tegak_lurus * x_mid  #rumus y-intercept: y_mid - m2 . x_mid

print(f"Titik 1: {x1:,.0f},{y1:,.0f}")
print(f"Titik 2: {x2:,.0f},{y2:,.0f}")
print(f"persamaan sumbu tengah tegak lurus dengan sumbu Y adalah :{gradien_tegak_lurus:,.1f} , {Titik_potong_terhadap_sumbu_Y:,.1f}")