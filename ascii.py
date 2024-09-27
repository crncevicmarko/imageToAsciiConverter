from PIL import Image, ImageDraw, ImageFont

asciiCharacters =  "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,. "[::-1]
asciiCharactersList = list(asciiCharacters)
asciiCharactersLenght = len(asciiCharactersList)

scaleFactor = 0.1
oneCharWidth = 10
oneCharHeight = 18

def resizeImage(image):
    width, height = im.size
    img_aspect_ratio = height / width
    new_image_width = 100
    new_image_height = int(img_aspect_ratio * new_image_width) 
    return image.resize((new_image_width, new_image_height))

def convertImageToGrayScale(image):
    return image.convert("L")

def mapAsciiToBrightnes(brightnesOfThePixel, asciiCharacters):
    # checking how many levels of brightnes (256) can one ascii character cover 
    howManyBrightnesesOneAsciiCharacterCanCover = 256 / asciiCharactersLenght
    # getting the ascii character position in list by dividing the brightnes of current pixel
    asciiIndexThatIsGoingToTheImage = int(brightnesOfThePixel / howManyBrightnesesOneAsciiCharacterCanCover)
    # returning right character from list
    return asciiCharacters[asciiIndexThatIsGoingToTheImage]

# load the image
im = Image.open("Luffy.jpg")
newImage = resizeImage(im)
grayImage = convertImageToGrayScale(newImage)

ascii_art_image = Image.new("RGB", (grayImage.width * 10, grayImage.height * 10), color=(0,0,0))
draw = ImageDraw.Draw(ascii_art_image)
font = ImageFont.load_default()

for y in range(grayImage.height):
    for x in range(grayImage.width):
        rgb_value = grayImage.getpixel((x, y)) # getting RGB value for x,y cordinates of every pixel
        asciiCharacter = mapAsciiToBrightnes(rgb_value, asciiCharacters) # getting the right ascii character for the brightnes of the pixel
        draw.text((x * 10 , y * 10), asciiCharacter, fill=rgb_value, font=font)

ascii_art_image.show()