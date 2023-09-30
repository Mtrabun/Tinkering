import cv2
import numpy as np

# Function to add a watermark to an image
def add_watermark(input_image_path, output_image_path, watermark_text):
    # Load the input image
    image = cv2.imread(input_image_path)

    # Define the watermark font, size, and color
    font = cv2.FONT_HERSHEY_TRIPLEX  # Modern font family (you can change this to your preferred font)
    font_scale = 0.5  # Decrease the font size
    font_color = (255, 255, 255)  # White color
    font_thickness = 1

    # Calculate the position to place the watermark
    text_size = cv2.getTextSize(watermark_text, font, font_scale, font_thickness)[0]
    watermark_x = 20  # Adjust the position as needed
    watermark_y = image.shape[0] - 20 - text_size[1]  # Adjust the position as needed

    # Create a transparent overlay for the watermark
    overlay = image.copy()
    cv2.putText(
        overlay,
        watermark_text,
        (watermark_x, watermark_y),
        font,
        font_scale,
        font_color,
        font_thickness,
        cv2.LINE_AA,
    )

    # Blend the overlay with the original image to make it transparent
    alpha = 0.5  # Adjust the transparency level (0.0 = fully transparent, 1.0 = fully opaque)
    cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

    # Save the image with the watermark
    cv2.imwrite(output_image_path, image)

if __name__ == "__main__":
    input_image_path = ""  # Replace with the path to your input image
    output_image_path = ""  # Replace with the desired output path
    watermark_text = "Water Mark Text"

    add_watermark(input_image_path, output_image_path, watermark_text)
