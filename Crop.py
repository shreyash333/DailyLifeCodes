
######## code to corp multiple images together ########

from PIL import Image
for i in range(791,795):
    print(i)
    img = Image.open("Screenshot ("+str(i)+").png")
    img2 = img.crop((784, 130, 1465, 969))
    img2.save("Crop Screenshot ("+str(i)+").png")