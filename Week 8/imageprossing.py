#flipping th eimage

from PIL import Image

#opening the image
img =Image.open('D:\\coding\\python\\Joy of computing using python\\Week 8\\photo1.png')

#transposing
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)

#save it to a file in a human understandable format

transposed_img.save('D:\\coding\\python\\Joy of computing using python\\Week 8\\newphoto1.png')
print("Done")