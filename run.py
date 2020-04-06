import cv2


def _detec():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')   
    img = cv2.imread('BNK48.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    faces = face_cascade.detectMultiScale(gray, 1.2, 6)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print((x, y), (x + w, y + h))
        
    count_faces=str(len(faces))
    print ("number of face(s)= " + count_faces)
    #cv2.imshow('img', img)
    #cv2.waitKey()


if __name__ == "__main__":
    _detec()
    

