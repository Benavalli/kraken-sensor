from IO.camera import camera

if __name__ == "__main__":
	picture_file_name = camera.take_picture()
	camera.save_picture(picture_file_name)
