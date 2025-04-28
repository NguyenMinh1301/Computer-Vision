import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("video-original/video1.mp4") # Path
assert cap.isOpened(), "Error reading video file"

# video1.mp4
region_points = [(733, 435), (706, 617), (1369, 598), (1320, 422)]

# video2.mp4
# region_points = [(1343, 346), (1398, 869), (1647, 866), (1567, 336)]

# video3.mp4
# region_points = [(3239, 866), (3269, 2103), (883, 2080), (843, 851)]

# video4.mp4
# region_points = [(323, 471), (320, 279), (810, 282), (815, 473)]

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("video-object-couting/video_object_counting_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize object counter object
counter = solutions.ObjectCounter(
    show=True,  # display the output
    region=region_points,  # pass region points

    # Models
    # model="/model/yolo11x.pt", #HIGH
    model="/model/yolo11n.pt", #BASIC
    # model="/model/yolov8x6.pt", #ULTRA
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = counter(im0)

    # print(results)  # access the output

    video_writer.write(results.plot_im)  # write the processed frame.

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows