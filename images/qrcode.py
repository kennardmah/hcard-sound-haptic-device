import qrcode

# The URL you want to convert into a QR code
url = 'https://forms.gle/UvuD6AZRdd19dpuE8'

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an Image object from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("qr_code.png")