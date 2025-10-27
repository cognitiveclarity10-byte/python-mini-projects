import qrcode
from PIL import Image

data = input("Enter a text or URL to Generate a QR code : ").strip()
file = input("How do you want to save the file :").strip()
    



   
img = qrcode.make(data)

img.save(file)

print(f"QR code has saved as {file}")

