from PIL import Image
# img=Image.open("1..jpg")
# #img.show()
# st=img.size
# print(st)
# dimen=(0,0,200,200)
# im=img.crop(dimen)
# im.show()



img=Image.open("2..jpg")
im=img.transpose(Image.FLIP_LEFT_RIGHT)
img.show()
im.show()