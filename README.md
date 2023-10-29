# QR Code Encoder and Decoder

This Python script allows you to both encode a string into a QR code and decode a QR code from an image file.

## Installation

Make sure you have the required libraries installed by running:

```bash
pip install qrcode[pil]
pip install pyzbar
```

## Usage 
You can run the script with the following command:

- To decode a QR code from an image file:

```bash
python qrencoder.py -d /path/to/qr
```

- To encode a string into a QR code and save it as an image:

```bash
python qrencoder.py -e "string to encode"
```
