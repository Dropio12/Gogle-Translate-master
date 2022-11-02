import cv2
from PIL import Image


def textscanner():
    # activate the camera
    vid = cv2.VideoCapture(0)
    while True:  # tries to find in the camera text and takes a picture when q is clicked
        _, Image = vid.read()
        cv2.imshow("Text Detection", Image)
        if cv2.waitKey(1) == ord('q'):
            cv2.imwrite('ImageWithText.jpg', Image)
            break
    vid.release()  # stops camera
    cv2.destroyAllWindows()  # delete all the windows
