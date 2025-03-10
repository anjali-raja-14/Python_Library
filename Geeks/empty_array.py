import numpy as np

# Create an empty array of shape (3, 4)
empty_array = np.empty((3, 4))
print("Empty Array:\n", empty_array)

# Create a full array of shape (3, 3) filled with the value 5
full_array = np.full((3, 3), 5)
print("Full Array:\n", full_array)


"""
Empty Array:
 [[4.45057637e-308 1.78021527e-306 8.45549797e-307 1.37962049e-306]
 [1.11260619e-306 1.78010255e-306 9.79054228e-307 4.45057637e-308]
 [8.45596650e-307 9.34602321e-307 4.94065646e-322 3.35919717e-138]]
Full Array:
 [[5 5 5]
 [5 5 5]
 [5 5 5]]

"""