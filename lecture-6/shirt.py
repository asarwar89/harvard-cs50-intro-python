import sys
from PIL import Image, ImageOps

images = []

if (len(sys.argv) != 3):
  sys.exit("Invalid input")

input = sys.argv[1]
output = sys.argv[2]

formats = ["jpg", "jpeg", "png"]

try:
  name_input,format_input = input.split(".")
  name_output, format_output = output.split(".")
  format_input = format_input.lower()
  format_output = format_output.lower()

  if (format_input not in formats or format_output not in formats):
    sys.exit("Invalid format")
except:
  sys.exit("Invalid format")

input = Image.open(input)
image = ImageOps.fit(input, size=(600, 600))

shirt = Image.open("shirt.png")
image.paste(im=shirt, mask=shirt)

image.save(
  output,
  save_all=True,
)