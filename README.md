# color-detection-program

This program is designed to display the name of a color along with its RGB values when you click on an image. It utilizes OpenCV and pandas libraries in Python.

![image](https://github.com/atugharajohn/color-detection-program/assets/92631399/9a6da2a2-ec6a-473f-8154-385067c87623)

![image](https://github.com/atugharajohn/color-detection-program/assets/92631399/8c02e2dd-9522-419f-8fd2-9be5d5b1dbd7)


To run the program, follow these steps:

1. Ensure you have Python installed on your system.

2. Install the necessary libraries using pip:

```pip install opencv-python numpy pandas```

3. Download the 'colors.csv' file containing color data.

4. Run the program from the command line, providing the path to the image you want to analyze:

```python color_detector.py -i <image_path>```

5. Click anywhere on the displayed image to see the name of the color and its RGB values. Press the 'esc' key to exit the program.

Please note:
- The 'colors.csv' file should contain color data in the format: color, color_name, hex, R, G, B.
- Ensure the image you provide exists and is accessible from the provided path.
- Close the image window by pressing the 'esc' key when you are done.
