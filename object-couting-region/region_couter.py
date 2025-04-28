import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("video-original/video1.mp4")
assert cap.isOpened(), "Error reading video file"

# video1.mp4
region_points = {
    "region-01": [(635, 373), (631, 721), (295, 723), (295, 373)],
    "region-02": [(1454, 80), (1528, 80), (1917, 695), (1915, 827), (1883, 832)],
    "region-03": [(897, 297), (1038, 295), (1149, 362), (1175, 513), (1068, 604), (888, 604), (782, 513), (800, 353)],
    "region-04": [(990, 717), (802, 999), (1265, 983)],
}

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("video-object-couting/video_object_counting_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize region counter object
regioncounter = solutions.RegionCounter(
    show=True,  # display the frame
    region=region_points,  # pass region points
    model="/model/yolo11n.pt",
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = regioncounter(im0)

    # print(results)  # access the output

    video_writer.write(results.plot_im)

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows