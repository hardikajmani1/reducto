
import cv2
import os

image_folder = '../video1'
video_name = 'video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'MP4V')

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, fourcc, 12.0, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()