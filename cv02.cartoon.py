import cv2
import numpy as np

def cartoonify_image(image_path, output_path):
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Unable to load image. Check file path!")
        return
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply median blur to reduce noise
    gray = cv2.medianBlur(gray, 5)
    
    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 19, 9)
    
    # Apply multiple bilateral filters for stronger smoothing
    color = img.copy()
    for _ in range(3):  # Apply filter multiple times
        color = cv2.bilateralFilter(color, 9, 250, 250)
    
    # Enhance contrast using histogram equalization
    lab = cv2.cvtColor(color, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    l = cv2.equalizeHist(l)
    lab = cv2.merge((l, a, b))
    color = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    
    # Combine the color image with the edges mask
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    # Save the output
    cv2.imwrite(output_path, cartoon)
    print(f"Cartoon image saved to {output_path}")

    # Display the cartoon image
    cv2.imshow("Original Image", img)
    cv2.imshow("Cartoon", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
cartoonify_image("image1.png", "cartoon1.png")
