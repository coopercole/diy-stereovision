import cv2
import numpy as np
import glob

# Termination criteria for corner detection
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Prepare object points (0,0,0), (1,0,0), (2,0,0), ..., (6,5,0) for a 7x6 chessboard
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all images
objpoints = []  # 3d point in real world space
imgpointsL = [] # 2d points in image plane for left camera
imgpointsR = [] # 2d points in image plane for right camera

# Load images
imagesL = glob.glob('left_*.png')
imagesR = glob.glob('right_*.png')

for imgL, imgR in zip(imagesL, imagesR):
    imgL = cv2.imread(imgL)
    imgR = cv2.imread(imgR)
    
    grayL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
    grayR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)
    
    retL, cornersL = cv2.findChessboardCorners(grayL, (7,6), None)
    retR, cornersR = cv2.findChessboardCorners(grayR, (7,6), None)
    
    if retL and retR:
        objpoints.append(objp)
        
        cornersL = cv2.cornerSubPix(grayL, cornersL, (11,11), (-1,-1), criteria)
        imgpointsL.append(cornersL)
        
        cornersR = cv2.cornerSubPix(grayR, cornersR, (11,11), (-1,-1), criteria)
        imgpointsR.append(cornersR)

# Calibrate each camera
retL, mtxL, distL, rvecsL, tvecsL = cv2.calibrateCamera(objpoints, imgpointsL, grayL.shape[::-1], None, None)
retR, mtxR, distR, rvecsR, tvecsR = cv2.calibrateCamera(objpoints, imgpointsR, grayR.shape[::-1], None, None)

# Stereo calibration
ret, mtxL, distL, mtxR, distR, R, T, E, F = cv2.stereoCalibrate(
    objpoints, imgpointsL, imgpointsR, mtxL, distL, mtxR, distR, grayL.shape[::-1], criteria=criteria, flags=cv2.CALIB_FIX_INTRINSIC)

# Save calibration data
np.savez('stereo_calib.npz', mtxL=mtxL, distL=distL, mtxR=mtxR, distR=distR, R=R, T=T, E=E, F=F)

print("Calibration complete")

