import cv2

def findPin(img):
    template = cv2.resize(cv2.imread('images/pin.png', 0), (0, 0), fx=0.6, fy=0.6)
    h, w = template.shape

    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    location = min_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    
    middle = location[0] + w/2, location[1] + h/2

    return middle

def findSphero(img):
    template = cv2.resize(cv2.imread('images/sphero.png', 0), (0, 0), fx=0.6, fy=0.6)
    h, w = template.shape

    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    location = min_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)

    middle = location[0] + w/2, location[1] + h/2

    return middle

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

ret, frame = cap.read()

cv2.imwrite('images/field.png', frame)
pinLocation = findPin(cv2.resize(cv2.imread('images/field.png', 0), (0, 0), fx=0.6, fy=0.6))
spheroLocation = findSphero(cv2.resize(cv2.imread('images/field.png', 0), (0, 0), fx=0.6, fy=0.6))

print(pinLocation)
print(spheroLocation)

cap.release()