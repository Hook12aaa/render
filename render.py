import cv2 
from playsound import playsound
video = cv2.VideoCapture("videoRender.mp4")
playsound('musicRender.mp3',False)
while(video.isOpened()):
    ret, frame = video.read()
    cv2.imshow('frame',colour)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()