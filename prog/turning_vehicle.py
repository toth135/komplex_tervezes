import math

print("A program kiszámítja a négykerekű jármű első kerekeinek kanyarodási szögeit.")
print("Adja meg a tengelytávolságot: ")
wheel_base = float(input())
print("Adja meg a kanyarodási szöget, melyet a jármű középvonalához mérünk: ")
alpha = float(input())

radius = wheel_base / math.tan(math.radians(alpha))

print("A kanyarodási ív sugara", wheel_base, "tengelytáv és", alpha, "fokos szög mellett", radius)

print("Adja meg a jármű szélességét: ")
width = float(input())

def calc_wheel_angles(radius, wheel_base, width):
    """
    Calculate the angles of the steered wheels.
    :param radius: the radius of the curve path
    :param wheel_base: the distance of the wheel axis
    :param width: length of the axis
    :return: left and right wheel angles in degrees
    """
    alpha1 = math.atan(wheel_base / (radius - (width / 2)))
    alpha2 = math.atan(wheel_base / (radius + (width / 2)))
    return [math.degrees(alpha1), math.degrees(alpha2)]

list = calc_wheel_angles(radius, wheel_base, width)
print("Az belső kerék kanyarodási szöge: ", list[0], "a külsőé: ", list[1])


print("Adja meg a jármű sebességét: ")
v = float(input())

print("Adja meg az eltelt időt: ")
t = float(input())

# x0 és y0 értéke 0, az origóból indulunk

x = 0 + radius - radius * math.cos(math.radians(v * t) / abs(radius))

y = 0 + abs(radius) * math.sin(math.radians(v * t) / abs(radius))

print("Pozíció x(t): ", x)
print("Pozíció y(t): ", y)
