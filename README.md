# Cartoon Rendering
This is a cartoon rendering project using OpenCV and python.

## Project Description
This project transforms an input image into a **cartoon style image** using OpenCV. It applies edge detection, color smoothing, and contrast enhancement to create a stylized cartoon effect.

## How the Code Works
1. **Load the Image:** Reads the input image using OpenCV.
2. **Convert to Grayscale:** Converts the image to grayscale for edge detection.
3. **Reduce Noise:** Applies median blur to smooth the image.
4. **Edge Detection:** Uses adaptive thresholding to detect strong edges.
5. **Smooth Colors:** Applies bilateral filtering multiple times to create a painting-like effect.
6. **Enhance Contrast:** Uses histogram equalization to improve color vibrancy.
7. **Combine Edge Map & Colors:** Merges the edges with the smooth color version to finalize the cartoon effect.
8. **Display & Save Output:** The cartoonified image is displayed and saved.

## 📷 Examples
### ✅ **Good Results** (Works Well):
| Original | Cartoonified |
|----------|-------------|
| ![Original](![image5](https://github.com/user-attachments/assets/d275d5ff-7533-4650-b7b6-46440d15d00b)
) | ![Cartoon](![cartoon5](https://github.com/user-attachments/assets/f542ff8d-098a-40c2-9f03-f3fe9647ccbb)
) |
#### **Best for:**
✔️ Portraits (faces, people)  
✔️ High-contrast and bright images  
✔️ Simple backgrounds  
✔️ Objects with clear edges (cars, animals)  

### ❌ **Bad Results** (Does Not Work Well):
| Original | Cartoonified |
|----------|-------------|
| ![Original](<img width="1278" alt="image1" src="https://github.com/user-attachments/assets/bd79caa7-aaa4-41fe-8949-321f89cc2941" />
)
) | ![Cartoon](![cartoon1](https://github.com/user-attachments/assets/7bc04b1f-a079-4a2b-b830-2f82e57cefd9)
) |
#### **Not Suitable for:**
❌ Low-light or dark images  
❌ Complex backgrounds with too much texture  
❌ Blurry or noisy images  

## Algorithm Limitations
- **Fine textures may be lost:** The smoothing process may remove small details.
- **Does not work well on low-contrast images:** Edge detection struggles when colors blend.
- **Noisy backgrounds cause inaccurate edges:** Complex scenes might produce unwanted results.
- **Face details may be altered:** Strong edge detection may modify small facial features.

##  File Structure
```
📁 Cartoonify_Project
│--  cartoonify.py   # Main Python script
│--  README.md       # Project documentation
│--  good_image.png  # Example of good input image
│--  good_cartoon.png # Example of good cartoon output
│--  bad_image.png   # Example of bad input image
│--  bad_cartoon.png  # Example of bad cartoon output
```

##  License
This project is open-source and available for educational purposes.



