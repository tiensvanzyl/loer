import cv2
user = "admin"
password = "d1abl0"
cap = cv2.VideoCapture("rtsp://admin: d1abl0@192.168.1.134:554/Streaming/Channels/101?")

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()