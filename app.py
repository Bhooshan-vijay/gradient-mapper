from PIL import Image
import numpy
from numpy.lib.function_base import average 

#variables
gradient_percentages = [0, 25, 50, 75, 100]
rgb_value_for_first_gradient  = [0, 0, 0]
rgb_value_for_second_gradient = [0, 0, 0]
rgb_value_for_third_gradient = [0, 0, 0]
rgb_value_for_fourth_gradient = [0, 0, 0]
one_fourth_of_pixel_average_range = (((3 * 255) / 3) / 4)
image_width = 0
image_height = 0
processed_pixel_row = [] 
processed_pixel_matrix = []

def get_pixel_matrix_from_image(image_name) :
    image = Image.open(image_name)
    pixel_data = image.load()
    image_width = image.width
    image_height = image.height
    pixel_matrix = []
    pixel_row = []
    for rows in range(image_height):
        for pixels in range(image_width):
            pixel_row.append(pixel_data[pixels, rows])
        pixel_matrix.append(pixel_row)
        pixel_row = [] 
    return pixel_matrix
    
raw_pixel_matrix = get_pixel_matrix_from_image("image.jpg")


#user input for setting color
for index in range((len(gradient_percentages) - 1)):
    red = input("What r color value do you want for range " + str(gradient_percentages[index]) + " to " + str(gradient_percentages[index + 1]) + " :" )
    green =  input("What g color value do you want for range " + str(gradient_percentages[index]) + " to " + str(gradient_percentages[index + 1]) + " :" )
    blue =  input("What b color value do you want for range " + str(gradient_percentages[index]) + " to " + str(gradient_percentages[index + 1]) + " :" )
    if index == 0:
        rgb_value_for_first_gradient[0] = red
        rgb_value_for_first_gradient[1] = green
        rgb_value_for_first_gradient[2] = blue
    elif index == 1:
        rgb_value_for_second_gradient[0] = red
        rgb_value_for_second_gradient[1] = green
        rgb_value_for_second_gradient[2] = blue
    elif index == 2:
        rgb_value_for_third_gradient[0] = red
        rgb_value_for_third_gradient[1] = green
        rgb_value_for_third_gradient[2] = blue
    elif index == 3:
        rgb_value_for_fourth_gradient[0] = red
        rgb_value_for_fourth_gradient[1] = green
        rgb_value_for_fourth_gradient[2] = blue


#set pixel color according to user preference
for row in raw_pixel_matrix : 
    for pixel in row :
        average_pixel_brightness = (pixel[0] + pixel[1] + pixel[2] ) / 3
        if average_pixel_brightness < one_fourth_of_pixel_average_range :
            processed_pixel_row.append(tuple(rgb_value_for_first_gradient))
        elif average_pixel_brightness < (2 * one_fourth_of_pixel_average_range):
            processed_pixel_row.append(tuple(rgb_value_for_second_gradient))
        elif average_pixel_brightness < (3 * one_fourth_of_pixel_average_range):
            processed_pixel_row.append(tuple(rgb_value_for_third_gradient))
        elif average_pixel_brightness < (4 * one_fourth_of_pixel_average_range):
            processed_pixel_row.append(tuple(rgb_value_for_fourth_gradient))
    processed_pixel_matrix.append(processed_pixel_row)
    processed_pixel_row = [] 





# 0 0 66
# 132 0 0
# 234, 182, 1
# 211 127 1

pixel_array = numpy.array(processed_pixel_matrix,  dtype=numpy.uint8)
processed_image = Image.fromarray(pixel_array)

