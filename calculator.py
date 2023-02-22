# Membuat fungsi penjumlahan
def add(x, y):
   return x + y

# Membuat fungsi pengurangan
def subtract(x, y):
   return x - y

# Membuat fungsi perkalian
def multiply(x, y):
   return x * y

# Membuat fungsi pembagian
def divide(x, y):
   return x / y

# Menampilkan menu operasi
print("Pilih Operasi.")
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")

# Meminta input dari pengguna
choice = input("Masukkan pilihan(1/2/3/4): ")

num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))

# Menjalankan operasi sesuai dengan pilihan pengguna
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Input salah")
