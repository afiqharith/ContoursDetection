import cv2
import os

FOLDERPATH = 'images/'
IMAGENAME = 'shape.jpg'
IMAGEPATH = os.path.join(os.getcwd(), FOLDERPATH, IMAGENAME)
ORANGE = (0,165,255)

class ContourDetection:
    
    def __init__(self, IMAGEPATH, START = True):

        self.image = cv2.imread(IMAGEPATH)

        if START == True:
            self.main()

    def cvtContour(self, binaryImage):

        contours, hierarchy = cv2.findContours(binaryImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def main(self):
        rgbImage = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        grayImage = cv2.cvtColor(rgbImage, cv2.COLOR_RGB2GRAY)

        _, binaryImage = cv2.threshold(grayImage, 200, 255, cv2.THRESH_BINARY_INV)

        contors = self.cvtContour(binaryImage)
        cv2.drawContours(self.image, contors, -1, ORANGE, 2)

        cv2.imshow("YOLO Object Detection", self.image)
        cv2.waitKey(0)

if __name__ == "__main__":

    ContourDetection(IMAGEPATH)
