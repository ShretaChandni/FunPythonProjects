import qrcode

data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename (with .png extension): ').strip()

# Create a QR Code object
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code
    box_size=10,
    border=4
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Generate the QR code image with colors
image = qr.make_image(fill_color='purple', back_color='pink')

# Save the image
image.save(filename)

print(f'QR code saved as {filename}')
