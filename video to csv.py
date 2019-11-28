# list of imports
import cv2
import csv
import os

#define path
path = "videos/train/"

# get all the video file names
video_file_names = []
for x in os.listdir(path):
		video_file_names.append(x)
print(video_file_names)

# iterate and save them to csv
for file in video_file_names:
    # use cv2 to take the videos
	cam = cv2.VideoCapture("{}{}".format(path,file))
	currenti = 0
	# get images from the videos
	while(True):
		ret, frame = cam.read()
		if ret:
    		# The csv would be saved in "video csv data" folder
			with open("video csv data/{}_pixel.csv".format(file), 'a') as f:
					writer = csv.writer(f)
					writer.writerow(frame)
		else:
			break
	cam.release()