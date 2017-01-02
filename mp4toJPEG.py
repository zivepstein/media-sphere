import cv2
path_to_movie = 'sara-fulldome/A.mov'
path_to_output_directory = "slice/sara-A/"
vidcap = cv2.VideoCapture(path_to_movie)
success,image = vidcap.read()
count = 0;
while success:
    success,image = vidcap.read()
    cv2.imwrite(path_to_output_directory + "frame_%d.jpg" % count, image)     # save frame as JPEG file
    if cv2.waitKey(10) == 27:                     # exit if Escape is hit
        break
    count += 1
count


