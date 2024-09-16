import qrcode
from PIL import Image

# Create a QRCode object
qr = qrcode.QRCode(
    version=1,  # Version of the QR code (1 is the smallest, higher numbers allow more data)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level (L: 7% of data can be restored)
    box_size=10,  # Size of the QR code box
    border=4,  # Border thickness
)

# Add data to the QR code
qr.add_data("https://github.com/vishal-56/Students-Marks-and-rank-analysis-by-react")
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='green', back_color='blue')

# Save the image
img.save("qrcode_image.png")
