# Import
import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"

# First pass in the image and the cascade names as command-line arguments
# Use the ABBA image as well as the default cascade for detecting faces by OpenCV

# Create the HAAR cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Create the cascade and initialize it with our face cascade
# This loads the face cascade into memory so it's ready for use
# Note: Cascade is just an XML file that contains the data to detect faces

# Read the image
# Read the image and convert it to grayscale. Many operations in OpenCV are done in grayscale
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

'''
The function above detects the actual faces and is the key part of the code.
Explanation:
    1. The detectMultiScale function is a general function that detects objects.
    Since we are calling it on the face cascade, that's what it detects.

    2. The first option is the grayscale image.

    3. The second is the scaleFactor. Since some faces may be closer to the camera,
    they would appear bigger than the faces in the back. The scale factor compesates for this.

    4. The detection algorithm uses a moving window to detect objects.minNeighbors 
    defines how many objects are detected near the current one before it declares the face found.
    minSize, meanwhile, gives the size of each window.
'''


# The function reutrns a list of rectangles to indicate it found a face.
# Now, loop over where it thinks it found something

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
# This function returns 4 values: the x and y location of the rectangle,
# and the rectangle's width and height: w, h
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# We use these values to draw a rectangle using the built-in rectangle() function
cv2.imshow("Faces found", image)
cv2.waitKey(0)


