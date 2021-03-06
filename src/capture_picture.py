import argparse
import cv2
from time import sleep
from shutil import rmtree
import os

training_path = "training"

def check_positive(value):
	"""  This function checks whether the input is positive or not.   """
	ivalue = int(value)
	if ivalue <= 0:
		raise argparse.ArgumentTypeError("Please Enter Positive Number")
	return ivalue

def folder_check_or_create(user):
	""" This function checks whether the user folder is exists or not exists.  """
	training_user_folder = training_path + "/" + user
	if not os.path.exists(training_user_folder):
		os.makedirs(training_user_folder)
	else:
		if os.path.exists(training_user_folder):
			print("This folder already exist. To change it, type yes and press enter.")
			query = input("If you write 'yes' yhe folder will deleted.")
			if query == "yes":
				rmtree(training_user_folder)
				os.makedirs(training_user_folder)
			else:
				raise Exception("Program is down")

def capture_the_picture(number_of_photos, user):
	""" This function captures the user pictures.  """
	folder_check_or_create(user) # check folder exist and create

	camera = cv2.VideoCapture(0)
	for x in range(number_of_photos):
		save_image_path = training_path + "/" + user + "/" + user + str(x+1) + '.jpg'	
		return_value,image = camera.read()
		cv2.imwrite(save_image_path, image)
		cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
		print(str(x) + ". taked photo ")
	camera.release()
	cv2.destroyAllWindows()



parser = argparse.ArgumentParser(description='Take picture for training data')
parser.add_argument("-p", "--photo", type=check_positive, default=10,
					help="The number of photo for training")
parser.add_argument("-u", "--user", type=str, default="None",
					help="The number of photo for training")
args = parser.parse_args()

capture_the_picture(args.photo, args.user)
