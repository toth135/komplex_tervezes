import math

print("A program kiszámítja a négykerekű jármű első kerekeinek kanyarodási szögeit.")
print("Adja meg a tengelytávolságot: ")
w = input()
print("Adja meg a kanyarodási szöget, melyet a jármű középvonalához mérünk: ")
alpha = input()

r = float(w) / (math.tan(math.radians(float(alpha))))

print("A kanyarodási ív sugara", w, "tengelytáv és", alpha, "fokos szög mellett", r)

print("Adja meg a jármű szélességét: ")
a = input()

alpha1 = (math.atan(float(w) / (r - (float(a) / 2))))*100
alpha2 = (math.atan(float(w) / (r + (float(a) / 2))))*100

print("A belső kerék kanyarodási szöge: ", alpha1, ", a külsőé: ", alpha2)

print("Adja meg a jármű sebességét: ")
v = input()

print("Adja meg az eltelt időt: ")
t = input()

# x0 és y0 értéke 0, az origóból indulunk

x = 0 + r - r * math.cos(math.radians(float(v) * float(t)) / abs(r))

y = 0 + abs(r) * math.sin(math.radians(float(v) * float(t)) / abs(r))

print("Pozíció x(t): ", x)
print("Pozíció y(t): ", y)
