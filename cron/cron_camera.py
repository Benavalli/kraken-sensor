from IO.camera import pi_camera


if __name__ == "__main__":
	picture_file_name = pi_camera.Camera.take_picture()
	pi_camera.Camera.save_picture(picture_file_name)
