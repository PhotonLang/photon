from photon import _pillow, helpers

timer = helpers.TimerHelper()

timer.start()

image = helpers.safe_read("image.jpg")


new_image = _pillow.resize(image, (3, 4))

timer.end()
print(timer.time())

helpers.safe_save(new_image, "resizedimage.jpg")


