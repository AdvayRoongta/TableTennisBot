import cv2 as cv
import numpy as np
import machine
import time

dir_pin = machine.Pin(2, machine.Pin.OUT)
step_pin = machine.Pin(3, machine.Pin.OUT)

def step_motor(direction, steps=10, delay=0.001):
    dir_pin.value(direction)
    for _ in range(steps):
        step_pin.value(1)
        time.sleep(delay)
        step_pin.value(0)
        time.sleep(delay)

camera = cv.VideoCapture(0)
camera.set(cv.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    success, frame = camera.read()
    if not success:
        break
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
  #white
    lower = np.array([10, 180, 180])
    upper = np.array([22, 255, 255])
  
    mask = cv.inRange(hsv, lower, upper)
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max(contours, key=cv.contourArea)
      
        if cv.contourArea(largest_contour) > 30:
            ((x, y), radius) = cv.minEnclosingCircle(largest_contour)
            M = cv.moments(largest_contour)
            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"])
                if cx < 270:
                    step_motor(0)
                elif cx > 370:
                    step_motor(1)
                center = (cx, int(M["m01"] / M["m00"]))
                cv.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
                cv.circle(frame, center, 5, (0, 0, 255), -1)
    cv.imshow("Ball Tracking", frame)
    cv.imshow("mask", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv.destroyAllWindows()
