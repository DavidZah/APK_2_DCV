"""main.py: kód na APK implementace flout numbers dle IEEE754 ."""
__author__      = "David Žahour"
__copyright__   = "THE BEER-WARE LICENSE , PS:mám rád 12 Plzeň "

import numpy as np
arr = []
x = np.uint8

for x in range(0,255):
    sing = (x & 0b10000000)>>7
    exp = (x & 0b01110000)>>4
    man = x & 0b00001111

    num = pow(-1,sing) * pow(2,exp-3)*man
    arr.append(num)

arr = list(set(arr))
arr.sort()

print("Unikátních čísel je:", len(arr))
print("Největší číslo je:", arr[len(arr)-1])
print(arr)
