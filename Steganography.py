from PIL import Image
import binascii as t
import optparse

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r,g,b)

def hex2rgb(hexcode):
    return tuple(map(ord, hexcode[1:],decode('hex')))

def str2bin(message):
    binary = bin(int(t.hexlify(message), 16))
    return binary[2:]

def encode(hexcode, digit):
    if hexcode[-1] in ('0', '1', '2', '3', '4', '5'):
        hexcode = hexcode[:-1] + digit
        return hexcode
    else:
        return None

def decode(hexcode):
    if hexcode[-1] in ('0', '1'):
        return hexcode[-1]
    else:
        return None