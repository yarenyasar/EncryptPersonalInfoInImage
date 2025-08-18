# Image Encryption & Decryption GUI Application

## Overview
This Python project provides a user-friendly GUI application for encrypting and decrypting personal information embedded in grayscale images. Users can input their name and Turkish ID (TC), upload a PNG image, and securely encode the data within the image pixels.

The project combines:
- **Tkinter** for the GUI interface  
- **Pillow (PIL)** for image processing  
- Custom **encryption algorithms** using XOR operations with a randomly generated password  

## Features
- Encrypt personal information (name and TC number) into grayscale images  
- Decrypt previously encrypted images to retrieve the original data  
- Random password generation for secure encryption  
- Simple and intuitive graphical interface  

## How It Works

### Encryption
1. Input personal data and select a grayscale PNG image  
2. Convert image to a NumPy array  
3. Transform characters into binary and encode them in pixel values  
4. Use a randomly generated password for XOR-based encryption  

### Decryption
1. Upload an encrypted image and provide the password  
2. Extract binary data from the image pixels  
3. Reverse the XOR operation to retrieve the original information  

## Usage
1. Install dependencies:
```bash
pip install pillow numpy

