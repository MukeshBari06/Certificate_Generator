import cv2
import numpy as np

# INPUT FILE PATHS
template_file_path = 'template.jpg'
output_directory_path = 'preview.jpg'

img = cv2.imread(template_file_path, cv2.IMREAD_COLOR)

# Convert the image to gray-scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find the edges in the image using canny detector
edges = cv2.Canny(gray, 50, 150)

# Detect points that form a line
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 3, minLineLength=500, maxLineGap=15)


# INPUT DATA and SEE PREVIEW (onClickPreview method)
final_font_size = 1.0
final_font_color = (255, 0, 0)
final_font = cv2.FONT_HERSHEY_SIMPLEX
final_font_thickness = 2


ind = 0;
Location = open("Locations.txt", "w")
y = [0]
for line in lines:
    x1, y1, x2, y2 = line[0]
    if y1 == y2:
        draw = True
        for y3 in y:
            if abs(y3 - y1) < 30:
                draw = False
                break

        if draw:
            text_x = (x1 + x2) / 2
            text_y = (y1 + y2) / 2
            text_x = int(text_x)
            text_y = int(text_y)
            cv2.putText(img, str(ind), (text_x, text_y-20), final_font, final_font_size, final_font_color, final_font_thickness)
            Location.write(str(ind)+" "+str(int(x1)+30)+" "+str(text_y-20)+"\n")
        ind += 1
        y.append(y1)
Location.close()
cv2.imwrite(output_directory_path, img)