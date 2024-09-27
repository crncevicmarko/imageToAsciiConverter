from PIL import Image, ImageDraw, ImageFont

asciiCharacters =  "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,. "
asciiCharactersList = list(asciiCharacters)
asciiCharactersLenght = len(asciiCharactersList)

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

im = Image.open("Luffy.jpg")
print("Original: ",im.height, im.width)
im.show()
newImage = resizeImage(im)
grayImage = convertImageToGrayScale(newImage)

ascii_art_image = Image.new("L", (grayImage.width * 10, grayImage.height * 10), color=255)
draw = ImageDraw.Draw(ascii_art_image)

font = ImageFont.load_default()
print("Resized: ",grayImage.height, grayImage.width)
grayImage.show()
for y in range(grayImage.height):
    for x in range(grayImage.width):
        rgb_value = grayImage.getpixel((x, y)) # za svaki pixel za x,y kordinate izvalcimo RGB vrednost
        asciiCharacter = mapAsciiToBrightnes(rgb_value, asciiCharacters) # getting the right ascii character for the brightnes of the pixel
        draw.text((x * 10 , y * 10), asciiCharacter, fill=rgb_value, font=font)

ascii_art_image.show()