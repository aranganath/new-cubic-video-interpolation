import os
import cv2

path = "/home/achyuth/new-cubic-video-interpolation/datasets/example/car-turn/"
out_path = "/home/achyuth/new-cubic-video-interpolation/vid_out/car-turn/"
out_video_path = "car-turn_vid.mp4"
output_full_vid_path = out_path+out_video_path

images = os.listdir(path)
images.sort()
# print(images)

img = []

for i in images:
	i = path+i
	img.append(i)

cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')

frame = cv2.imread(img[0])
size = list(frame.shape)
# print(size)
del size[2]
size.reverse()

video = cv2.VideoWriter(output_full_vid_path, cv2_fourcc, 24, size)

for i in range(len(img)):
	video.write(cv2.imread(img[i]))


video.release()