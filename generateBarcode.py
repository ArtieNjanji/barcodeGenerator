# from barcode1 import codeType, ImageWriter
from barcode import EAN13 as codeType
from barcode.writer import ImageWriter
import random
import os
import sys

def generateBarcode(code, user):
    if not os.path.exists('barcode'):
        os.makedirs('barcode')
    
    bCode = codeType(code, writer=ImageWriter())
    bCode.save('../barcode/'+ user)

def main():
    code = str(random.randint(1000000000000, 9999999999999))

    # Check if the username is provided as a command-line argument
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = input('Enter Username: ')

    generateBarcode(code, username)

if __name__ == "__main__":
    main()