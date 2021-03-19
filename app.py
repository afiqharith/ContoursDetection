import cv2
import os

FOLDERPATH = 'images/'
IMAGENAME = 'shape.jpg'
IMAGEPATH = os.path.join(os.getcwd(), FOLDERPATH, IMAGENAME)
RED = (0,0,255)

class ContourDetection:
    
    def __init__(self, IMAGEPATH, START = True):

        self.image = cv2.imread(IMAGEPATH)

        if START == True:
            self.main()

    def cvtContour(self, binaryImage):

        contours, hierarchy = cv2.findContours(binaryImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def main(self):
        # Convert color in from BGR to GRAY
        # If use PIL, please convert BGR to RGB before converting to GRAY
        grayImage = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        _, binaryImage = cv2.threshold(grayImage, 200, 255, cv2.THRESH_BINARY_INV)

        contours = self.cvtContour(binaryImage)
        cv2.drawContours(self.image, contours, -1, RED, 4)

        cv2.imshow("Contour Detection", self.image)
        cv2.waitKey(0)

if __name__ == "__main__":

    ContourDetection(IMAGEPATH)
