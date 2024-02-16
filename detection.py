import cv2
import numpy as np
import pandas as pd
import argparse

# Set up argument parser to take image path from command line
argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('-i', '--image', required=True, help="Specify Image Path")
arguments = vars(argument_parser.parse_args())
image_path = arguments['image']

# Read the image using OpenCV
image = cv2.imread(image_path)

# Declare global variables for later use
mouse_clicked = False
r = g = b = xpos = ypos = 0

# Read CSV file containing color data and assign column names
column_names = ["color", "color_name", "hex", "R", "G", "B"]
color_data = pd.read_csv('colors.csv', names=column_names, header=None)

# Function to determine the closest matching color from the CSV data
def get_color_name(R, G, B):
    min_distance = 10000
    for i in range(len(color_data)):
        distance = abs(R - int(color_data.loc[i, "R"])) + abs(G - int(color_data.loc[i, "G"])) + abs(B - int(color_data.loc[i, "B"]))
        if distance <= min_distance:
            min_distance = distance
            color_name = color_data.loc[i, "color_name"]
    return color_name

# Function to retrieve x, y coordinates of mouse click
def handle_mouse_event(event, x, y, flags, param):
    global b, g, r, xpos, ypos, mouse_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_clicked = True
        xpos = x
        ypos = y
        b, g, r = image[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow('image')
cv2.setMouseCallback('image', handle_mouse_event)

while True:
    cv2.imshow("image", image)
    if mouse_clicked:
        # Draw filled rectangle to display selected color
        cv2.rectangle(image, (20, 20), (750, 60), (b, g, r), -1)

        # Generate text string to display color name and RGB values
        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        
        # Add text to image using different font
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, text, (50, 50), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # For very light colors, display text in black
        if r + g + b >= 600:
            cv2.putText(image, text, (50, 50), font, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
            
        mouse_clicked = False

    # Break the loop when the 'esc' key is pressed
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()