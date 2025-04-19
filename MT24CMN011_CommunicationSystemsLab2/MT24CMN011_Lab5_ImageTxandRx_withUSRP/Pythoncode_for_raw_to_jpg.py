from PIL import Image

with open("D:\MTech_CMN_VNIT_MAIN\VNIT SEM 2\CS_2LAB\MT24CMN011\ImageTxandRx_withUSRP/received_image2.raw", "rb") as f:
    raw_data = f.read()
# Define image dimensions (must match the original!)
  # Use the original dimensions
# Reconstruct image
reconstructed_img = Image.frombytes("RGB", (50, 50), raw_data)
# Save back to JPEG
reconstructed_img.save("reconstructed.jpeg")
print("RAW converted back to JPEG successfully!")