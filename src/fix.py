from pathlib import Path
from rembg import remove, new_session
from PIL import Image


class fix_images():

    def fix_list():
        session = new_session()
        for file in Path('input_images').glob('*.jpg'):
            input_path = str(file)
            output_path = str('output_images' + "\\" + (file.stem + "_out.jpg"))
            with open(input_path, 'rb') as i:
                with open(output_path, 'wb') as o:
                    input = i.read()
                    output = remove(input, session=session)
                    o.write(output)
            image = Image.open(output_path).convert("RGBA")
            new_image = Image.new("RGBA", image.size, "WHITE")
            new_image.paste(image, mask=image)
            new_image.convert("RGB").save(output_path)







