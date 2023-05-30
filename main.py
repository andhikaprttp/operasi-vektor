import numpy as np

def hitung_vektor():
    # Menginputkan vektor
    vektor_a = np.array(eval(input("Masukkan vektor a (dalam bentuk [x, y, z]): ")))
    vektor_b = np.array(eval(input("Masukkan vektor b (dalam bentuk [x, y, z]): ")))
    
    # Menampilkan vektor a dan b
    print("vektor a =", vektor_a)
    print("vektor b =", vektor_b)
    
    # Operasi penjumlahan vektor
    hasil_penjumlahan = np.add(vektor_a, vektor_b)
    print("Penjumlahan vektor a dan b =", hasil_penjumlahan)
    
    # Operasi pengurangan vektor
    hasil_pengurangan = np.subtract(vektor_a, vektor_b)
    print("Pengurangan vektor a dan b =", hasil_pengurangan)
    
    # Operasi perkalian vektor dengan skalar
    skalar = float(input("Masukkan skalar: "))
    hasil_perkalian_skalar_a = np.multiply(skalar, vektor_a)
    hasil_perkalian_skalar_b = np.multiply(skalar, vektor_b)
    print("Perkalian skalar vektor a =", hasil_perkalian_skalar_a)
    print("Perkalian skalar vektor b =", hasil_perkalian_skalar_b)
    
    # Operasi perkalian dot (dot product)
    dot_product = np.dot(vektor_a, vektor_b)
    print("Dot product vektor a dan b =", dot_product)
    
    # Operasi perkalian cross (cross product)
    cross_product = np.cross(vektor_a, vektor_b)
    print("Cross product vektor a dan b =", cross_product)

# Memanggil fungsi hitung_vektor
hitung_vektor()
