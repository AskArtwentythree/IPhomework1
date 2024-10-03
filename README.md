# Video Filters Project

This project applies multiple image processing filters to a video stream in real time using Python and OpenCV. The available filters include **Black and White**, **Erosion**, **Horizontal Flip**, and **Inversion**. Each filter is applied sequentially to the video, showcasing how different effects can be stacked together for video manipulation.

## Features

1. **Black and White Filter**:
   - Converts the input image into grayscale.
   - Usage example: ![Example Image](https://ibb.co/w68P2SR)

2. **Erosion Filter**:
   - Applies an erosion effect using a 3x3 kernel.
   - Useful for reducing noise or making structures thinner.
   - Usage example: [Erosion Example](https://imgur.com/a/l3ELN5J)

3. **Horizontal Flip Filter**:
   - Flips the input image horizontally.
   - Usage example: ![Flip Example](https://ibb.co/JB14ZH3)

4. **Inversion Filter**:
   - Inverts the pixel values of an image, changing black to white and vice versa.
   - Usage example: ![Inversion Example](https://pyimagesearch.com/wp-content/uploads/2021/01/opencv_bitwise_not.png)

## File Structure

```
project-root/
│
├── filters/
│   ├── __init__.py                 # Initializes the filters module
│   ├── black_and_white_filter.py   # Black and white filter implementation
│   ├── erosion_filter.py           # Erosion filter implementation
│   ├── flip_horizontal_filter.py   # Horizontal flip filter implementation
│   └── inversion_filter.py         # Inversion filter implementation
│
├── main.py                         # Main file to apply the filters on the video stream
└── README.md                       # Project description and instructions
```

## How to Run the Project

### Requirements
- Python 3.x
- OpenCV
- NumPy

To install the dependencies, run:

```bash
pip install opencv-python numpy
```

### Running the Application

1. Place your video file in the project directory.
2. Update the video path in the `main.py` file:
   ```python
   video_capture = cv2.VideoCapture("path")
   ```
   Replace `"path"` with the path to your video file.
   
3. Run the application:

```bash
python main.py
```

Press `q` to stop the video playback.

## How It Works

The `main.py` script loads a video and processes it frame by frame. Each frame goes through a pipeline of filters that transform the image sequentially. The following filters are applied:

1. Black and White conversion
2. Erosion
3. Inversion of colors
4. Horizontal flipping

Each filter is implemented in its own module under the `filters/` directory, and all filters are combined in the `main.py` script.

## Example Output

![Filtered Output](example-output.png)

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request. You can add new filters, improve existing ones, or optimize the performance of the video processing pipeline.

---

This format gives a clear structure and helpful information for anyone looking to understand and run your project. Feel free to adjust any specific details!
