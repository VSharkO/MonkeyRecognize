#just add path as argument

import os, sys
from PIL import Image

directory = sys.argv[1]

for file_name in os.listdir(directory):
  print("Processing %s" % file_name)
  image = Image.open(os.path.join(directory, file_name))

  x,y = image.size
  new_dimensions = (30, 30)
  output = image.resize(new_dimensions, Image.ANTIALIAS)

  output_file_name = os.path.join(directory,file_name)
  output.save(output_file_name, "JPEG", quality = 95)

print("All done")