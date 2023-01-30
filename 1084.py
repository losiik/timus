import math

params = input()
params = params.split()
garden_side = int(params[0])
r = int(params[1])


def S():
    half_diag = garden_side * math.sqrt(2) / 2
    if r >= half_diag:
        return garden_side**2
    if r <= garden_side / 2:
        return math.pi * r**2

    sin_alpha = half_diag * math.sin(math.radians(45)) / r
    x = 180 - 45 - math.degrees(math.asin(sin_alpha))
    print(x)

    s_sector = r * x * 2 * math.pi / 360
    s_sectors = s_sector * 4
    print(s_sectors)

    l = r * math.sin(math.radians(90-x))
    print(l)

    return s_triangles + s_sectors

    s_triangle = l * garden_side / 4

    s_triangles = s_triangle * 8
    print(s_triangles)


print(S())

