from PIL import Image

with open("C:/Users/Asus/Desktop/received_image2.raw", "rb") as f:
    raw_data = f.read()

# Define image dimensions (must match the original!)
  # Use the original dimensions

# Reconstruct image
reconstructed_img = Image.frombytes("RGB", (50, 50), raw_data)

# Save back to JPEG
reconstructed_img.save("reconstructed.jpeg")

print("RAW converted back to JPEG successfully!")
