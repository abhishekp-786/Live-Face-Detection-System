import cv2

face_cap = cv2.CascadeClassifier("C:/Users/ABHISHEK/AppData/Local/Programs/Python/Python313/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)

if not video_cap.isOpened():
    print("Error: Could not open video device.")
    exit()

while True:
    ret, video_data = video_cap.read()
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(255,255,255),2)
    cv2.imshow("Live_Video",video_data)
    if cv2.waitKey(10) == ord("a"):
        break
video_cap.release()




######## This code is only to open the Camera ###########

# video_cap = cv2.VideoCapture(0)
# while True:
#     ret, video_data = video_cap.read()
#     cv2.imshow("Live_Video",video_data)
#     if cv2.waitKey(10) == ord("a"):
#         break
# video_cap.release()
