from helper_functions import *

# -----------------------FILL IN THE FOLDER WHERE YOUR IMAGE EXISTS--------------------------
datafolder = "C:/Users/Reshmi/OneDrive/Desktop/assgn/images/"
imgpath = datafolder + "1.jpg"
# ----------------------------------------STARTER CODE----------------------------------------
# Convert the color image to grayscale and returns the grayscale pixels
pixel_values = read_colorimg(imgpath)
# The returned pixel values INCLUDE 2 boundary rows and 2 boundary colns. Therefore,
numb_rows = len(pixel_values) - 2
numb_colns = len(pixel_values[0]) - 2
#
# ----------------------------------------WRITE YOUR CODE HERE----------------------------------------
# Create a data structure to store updated pixel information
# temp = [0] * numb_colns
# new_pixel_values = [temp] * numb_rows
new_pixel_values = [[0 for i in range(numb_colns)] for j in range(numb_rows)]
print("HELLO")
# Define the 3 x 3 mask as a tuple of tuples
mask = ((-1, -1, -1), (-1, 8, -1), (-1, -1, -1))

# Implement a function to slice a part from the image as a 2D list


def get_slice_2d_list(pixel_list, ind_x, ind_y):
    return [pixel_list[i][ind_y - 1:ind_y + 2] for i in range(ind_x - 1, ind_x + 2)]

# Implement a function to flatten a 2D list or a 2D tuple


def flatten(sliced_list):
    return [i for dum in sliced_list for i in dum]

flattened_mask = flatten(mask)
print(flattened_mask)
for i in range(1, numb_rows + 1):
    for j in range(1, numb_colns + 1):
        neighbour_pixels = get_slice_2d_list(pixel_values, i, j)
        flattened_neighbour_pixels = flatten(neighbour_pixels)
        mult_result = list(
            map(lambda x, y: x * y, flattened_neighbour_pixels, flattened_mask))
        print(neighbour_pixels)
        new_pixel_values[i-1][j-1] = sum(mult_result)

# ----------------------------------------END YOUR CODE HERE----------------------------------------
# Verify your result
verify_result(pixel_values, new_pixel_values, mask)
# View the original image and the edges of the image
view_images(imgpath, new_pixel_values)
