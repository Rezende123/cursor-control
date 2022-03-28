import os
from traceback import print_tb
from imutils import face_utils
import cv2
import dlib
import numpy as np

dat_file_name = "shape_predictor_68_face_landmarks.dat"

def createDatFile():
    if not os.path.exists(dat_file_name):
        print('Downloading files for aligning face image...')
        os.system('wget http://dlib.net/files/' + dat_file_name + '.bz2')
        os.system('bzip2 -dk ' + dat_file_name + '.bz2')
        print('Done.')

def shape_to_np(shape, dtype="int"):
    coords = np.zeros((68, 2), dtype=dtype)
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords

def show_face(dat_file_name, rects, img, gray):
    createDatFile()

    predictor = dlib.shape_predictor(dat_file_name)

    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = shape_to_np(shape)
        for (x, y) in shape:
            cv2.circle(img, (x, y), 2, (0, 0, 255), -1)

    cv2.imshow("Image", img)


def detect_face():
    # image_path = os.path.join(os.getcwd(), 'assets', 'image.png') # Para testes com imagens estáticas
    # img = cv2.imread(image_path) # Para testes com imagens estáticas
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale
        detector = dlib.get_frontal_face_detector()
        rects = detector(gray, 1) # rects contains all the faces detected
        
        if len(rects) > 0:
            predictor = dlib.shape_predictor(dat_file_name)
            shape = predictor(gray, rects[0])
            shape = shape_to_np(shape)
            # loop over the face parts individually
            for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
                # Nose positions returned
                if (name == 'nose'):
                    return shape[i:j]

            # return shape
        # else:
        #     show_face(dat_file_name, rects, img, gray)
    
        #     if cv2.waitKey(1) & 0xFF == ord('q'): # escape when q is pressed
        #         break




    # cv2.imshow("Image", img)
    # cv2.waitKey()



