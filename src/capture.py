import cv2

# Initialize video capture devices
cap_left = cv2.VideoCapture(1)  # Assuming the left camera is at index 0
cap_right = cv2.VideoCapture(2)  # Assuming the right camera is at index 1

# Capture a single frame from each camera
ret_left, frame_left = cap_left.read()
ret_right, frame_right = cap_right.read()

if ret_left and ret_right:
    # Display the captured images
    cv2.imshow('Left Camera Image', frame_left)
    cv2.imshow('Right Camera Image', frame_right)
    
    # Save the captured images to files
    cv2.imwrite('left_image.png', frame_left)
    cv2.imwrite('right_image.png', frame_right)
    
    # Wait until a key is pressed
    cv2.waitKey(0)

cap_left.release()
cap_right.release()
cv2.destroyAllWindows()