---

# Add_Watermark.py

## Description

This script allows users to add a textual watermark to an image. The watermark can be customized in terms of font, size, color, position, and transparency.

## Dependencies

- Python (Tested with Python 3.x)
- OpenCV (cv2)

To install OpenCV, you can use pip:

```bash
pip install opencv-python
```

## Usage

1. Ensure you have all the required dependencies installed.
2. Replace the `input_image_path`, `output_image_path`, and `watermark_text` placeholders in the `if __name__ == "__main__":` section with appropriate values.
3. Run the script:

```bash
python Add_Watermark.py
```

## Functionality

- **add_watermark(input_image_path, output_image_path, watermark_text)**:
  This function takes in the path to the input image, the path where the output image should be saved, and the text of the watermark. It then adds the watermark to the image and saves the result.

    - **Parameters**:
        - `input_image_path` (str): Path to the input image.
        - `output_image_path` (str): Path to save the watermarked image.
        - `watermark_text` (str): Text that should be added as a watermark.

    - **Returns**: None. The function saves the watermarked image to the specified output path.

### Customizing the Watermark

Inside the `add_watermark` function, you can adjust the following variables to customize the watermark:

- **font**: Font family for the watermark. Default is `cv2.FONT_HERSHEY_TRIPLEX`.
- **font_scale**: Size of the watermark font. Default is `0.5`.
- **font_color**: Color of the watermark. Default is white (`(255, 255, 255)`).
- **font_thickness**: Thickness of the watermark text. Default is `1`.
- **watermark_x** and **watermark_y**: Position of the watermark on the image.
- **alpha**: Adjust the transparency level (0.0 = fully transparent, 1.0 = fully opaque).

## Note

Ensure you have the necessary permissions for both reading the input image and writing to the output path. 

---
