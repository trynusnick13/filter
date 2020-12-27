from filter_app.image.base_image import Image
import PIL
import datetime

def apply_commands(Command, filename):
    pil_image = PIL.Image.open(f'./static/{filename}')
    base_image = Image("temp-name", pil_image)
    command = Command(base_image)
    new_file = command.execute()
    timestamp_now = datetime.datetime.now()
    path = "./static/"
    new_file.name = f"{timestamp_now.timestamp()}-{filename}"
    new_file.save_file(name=path+new_file.name)
    return new_file.name
