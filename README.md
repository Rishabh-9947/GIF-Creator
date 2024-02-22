# GIF-Creator
This project involves creating a Python script that can generate GIFs from a series of images or video clips. This is a great way to learn about image processing and working with files in Python.
# GIF Creator

The "GIF Creator" is a Python utility that allows you to create animated GIFs from a collection of image files. This tool is perfect for beginners who want to explore the world of image processing and file manipulation in Python. With a simple command-line interface, you can transform a series of static images into a fun and shareable animation.

## Features

- Create GIFs from a sequence of image files (PNG, JPG, JPEG).
- Customize the frame duration to control the animation speed.
- Automatically resize images to a uniform size for consistent GIF quality.
- Simple CLI for easy operation and customization.

## Prerequisites

Before running the script, ensure you have Python and the Pillow library installed:

```bash
pip install Pillow

Usage
To create a GIF, follow these steps:
Place all your source images in a single directory.
Run the script and provide the path to the directory and the desired output filename.
bash
python gif_creator.py

You will be prompted to enter the directory containing your images and the name of the output GIF file.
Customization
You can adjust the duration of each frame in the GIF by modifying the duration parameter in the create_gif function call within the script.
Contributing:
Contributions to enhance this tool, such as adding support for more image formats or introducing new features like custom transitions, are welcome. Please fork the repository, make your changes, and submit a pull request.
