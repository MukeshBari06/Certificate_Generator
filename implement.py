import cv2
import numpy as np

# INPUT FILE PATHS
input_txt_file = 'data.txt'
template_file_path = 'template.jpg'
output_directory_path = ''
INDEX = [7, 2]

# INPUT DATA and SEE PREVIEW
final_font_size = 1.3
final_font_color = (0, 0, 0)
final_font = cv2.FONT_HERSHEY_SIMPLEX
final_font_thickness = 2



img = cv2.imread(template_file_path, cv2.IMREAD_COLOR)

# Convert the image to gray-scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find the edges in the image using canny detector
edges = cv2.Canny(gray, 50, 150)

# Detect points that form a line
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 3, minLineLength=500, maxLineGap=15)

DATA = list(list())
with open(input_txt_file) as input_list:
    content = input_list.read().splitlines()
    for line in content:
        list_elements = line.split("/")
        DATA.append(list_elements)

Locations = {}
Location = open("Locations.txt")
for line in Location:
    index = list(map(int, line.split(" ")))
    Locations[index[0]] = [index[1], index[2]]
Location.close()
for i in range(len(DATA)):
    for j in range(len(INDEX)):
        cv2.putText(img, DATA[i][j], (Locations[INDEX[j]][0], Locations[INDEX[j]][1]), final_font, final_font_size, final_font_color, final_font_thickness)
    certi_path = output_directory_path+str(i+1)+'.jpg'
    cv2.imwrite(certi_path, img)

cv2.destroyAllWindows()