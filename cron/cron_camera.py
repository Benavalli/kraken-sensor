from IO.camera import picture_camera


if __name__ == "__main__":
	camera = picture_camera.PictureCamera()
	picture_file_name = camera.take_picture()
	camera.save_picture(picture_file_name)
