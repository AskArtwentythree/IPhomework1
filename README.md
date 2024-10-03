# Video Filters Project

This project applies multiple image processing filters to a video stream in real time. The available filters include **Black and White**, **Erosion**, **Horizontal Flip**, and **Inversion**. Each filter is applied sequentially to the video, showing by how different effects can be stacked together.

## Features

1. **Black and White Filter**:
   - Converts the input image into grayscale.

2. **Erosion Filter**:
   - Applies an erosion effect using a 3x3 kernel.

3. **Horizontal Flip Filter**:
   - Flips the input image horizontally.

4. **Inversion Filter**:
   - Inverts the pixel values of an image, changing black to white and vice versa.

## How It Works

The `main.py` script loads a video and processes it frame by frame. Each frame goes through a pipeline of filters that transform the image sequentially. The following filters are applied:

1. Black and White conversion
2. Erosion
3. Inversion of colors
4. Horizontal flipping

## Preview

https://www.youtube.com/watch?v=ZbM8tWJ5ELc

