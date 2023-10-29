import argparse
import sys
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

def mensaje_error(option):
    sys.stderr.write(f"Error: The correct use is qrencoder.py -d \"path/to/qr\" to decode, and qrencoder.py -e \"string to qr\" to encode\n")
    sys.exit(1)

parser = argparse.ArgumentParser()
parser.error = mensaje_error

exclusive_group = parser.add_mutually_exclusive_group(required=True)

exclusive_group.add_argument("-d", "--decode", help="Use for decoding a qr", type=str, metavar="/path/to/qr")
exclusive_group.add_argument("-e", "--encode", help="Use for encoding a string", type=str, metavar="string_to_encode")

args = parser.parse_args()

if args.decode:
    text = args.decode
    image = Image.open(text)
    result = decode(image)
    if result:
        print("QR content:", result[0].data.decode('utf-8'))
    else:
        print("No QR code found in the photo.")
elif args.encode:
    text = args.encode
    img=qrcode.make(text)
    name = input("Type the name for saving the qr: ")
    img.save(name+".png")

