from classes.barang_kantor import Atk
from classes.div_it import IT
from classes.div_rnd import RnD

print("Python OOP")

pulpen1 = Atk('Pulpen', 10, 2000)
kertas1 = Atk('kertas', 50, 30000)

print(pulpen1.info())
print(pulpen1.total_invent())
print('='*30)
print(kertas1.info())
print('+'*30)
print('\n')

it1 = IT('Dolor', 20)
rnd1 = RnD('Sit', 23)
print(it1.nama)
print(it1.hitung_gaji(5, 10))

gaji1 = it1.hitung_gaji(5, 10)
gaji2 = rnd1.hitung_gaji(6, 12)

semuagaji = [gaji1, gaji2]
x = 0
for i in (it1, rnd1):
    print(i.info())
    print(semuagaji[x])
    print('=' * 30)
    x += 1
