import numpy as np

particle_center = [0,0,0]

dots = []

bit_array = np.zeros((101,101,101), dtype=bool)

for i in xrange(101):
    dots.append(i/10. - 5)

print dots

i_number = 0
for i in dots:
    j_number = 0
    for j in dots:
        k_number = 0
        for k in dots:
            if not (bit_array[i,j,k]):
                squared_distance = (particle_center[0] - i)**2 + (particle_center[1] - j)**2 + (particle_center[2] - k)**2
                if i==-5 and j==-5 and k==-4.9: print squared_distance
                if squared_distance < 16:
                    bit_array[i_number,j_number,k_number] = True
            k_number += 1
        j_number += 1
    i_number += 1

print bit_array[50, 50, 50]
print bit_array