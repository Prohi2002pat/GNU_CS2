from PIL import Image

# Load image and convert to raw binary
img = Image.open("C:/Users/Asus/Desktop/MT24CMN006_Communication/ImageTxandRx_withUSRP/images.jpg").convert("RGB")
raw_data = img.tobytes()

width, height = img.size
print(width)
print(height)
# Save raw data
with open("img1.raw", "wb") as f:
    f.write(raw_data)

