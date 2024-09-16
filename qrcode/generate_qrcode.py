import qrcode as qr

# Create a QR code for the given URL
img = qr.make("https://github.com/vishal-56/Students-Marks-and-rank-analysis-by-react")

# Save the QR code image
img.save("qr_code.png")
