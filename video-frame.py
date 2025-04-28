import cv2

VIDEO = "video3.mp4"   # path
FRAME_IDX = 1       # frame number to get
# Or select by time seconds:
# TIME_SEC = 5.3      # -> cv2.CAP_PROP_FPS to derive the frame index

cap = cv2.VideoCapture(VIDEO)
fps = cap.get(cv2.CAP_PROP_FPS)
if 'TIME_SEC' in locals():
    FRAME_IDX = int(TIME_SEC * fps)

cap.set(cv2.CAP_PROP_POS_FRAMES, FRAME_IDX)
success, frame = cap.read()
assert success, "Cannot get frame!"

cv2.imwrite("snapshot.png", frame)   # Saved snapshot
print("Saved snapshot.png (frame", FRAME_IDX, ")")
cap.release()
