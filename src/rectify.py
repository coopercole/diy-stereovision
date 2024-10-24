import cv2
import numpy as np

# Load calibration data
data = np.load('stereo_calib.npz')
mtxL, distL = data['mtxL'], data['distL']
mtxR, distR = data['mtxR'], data['distR']
R, T = data['R'], data['T']

# Capture images from cameras
cap_left = cv2.VideoCapture(1)
cap_right = cv2.VideoCapture(2)
ret_left, frame_left = cap_left.read()
ret_right, frame_right = cap_right.read()

# Stereo rectification
R1, R2, P1, P2, Q, _, _ = cv2.stereoRectify(mtxL, distL, mtxR, distR, frame_left.shape[:2], R, T)

# Compute the rectification transform for each camera
map1L, map2L = cv2.initUndistortRectifyMap(mtxL, distL, R1, P1, frame_left.shape[:2], cv2.CV_32FC1)
map1R, map2R = cv2.initUndistortRectifyMap(mtxR, distR, R2, P2, frame_right.shape[:2], cv2.CV_32FC1)

# Apply the rectification transform
rectified_left = cv2.remap(frame_left, map1L, map2L, cv2.INTER_LINEAR)
rectified_right = cv2.remap(frame_right, map1R, map2R, cv2.INTER_LINEAR)

# Display rectified images
cv2.imshow('Rectified Left', rectified_left)
cv2.imshow('Rectified Right', rectified_right)
cv2.waitKey(0)

cap_left.release()
cap_right.release()
cv2.destroyAllWindows()
