from PIL import Image
I = Image.open("littleschoolbus.bmp")
binary = ""
for y in range(I.size[0]):
    for comp in I.getpixel((y, 198))[::-1]:
        binary += str(comp & 1)
binary = binary.rstrip("1")
for i in range(16):
    try:
        print(bytes.fromhex(hex(int(binary + "1" * i, 2))[2:]).decode("ascii", "replace"))
    except: pass

