from PIL import Image
im=Image.open('Week 9\\test1.png')
rgb_im=im.convert('RGB')
r,g,b=rgb_im.getpixel((150,1))
print(r,b,g)