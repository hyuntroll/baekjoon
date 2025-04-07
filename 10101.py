angles = []
for i in range(3):
    angles.append(int(input()))

angle_set = set(angles)

if sum(angles) != 180:
    print("Error")
elif len(angle_set) == 1:
    print("Equilateral")
elif len(angle_set) == 2:
    print("Isosceles")
else:
    print("Scalene")    