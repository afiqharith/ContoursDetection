# Contours Detection using OpenCV

Detect contours on any pictures using OpenCV.

_To run the program on command line:_

```sh
$ python3 app.py
```

**Steps:**

1. Read original image from directory.
2. Convert image colour from BGR <sub>(OpenCV use BGR format instead of RGB)</sub> to GRAY.
3. Get image threshold <sub>(binary image)</sub>.
4. Get contour from the image.
5. Draw the contour lines on original image.
6. Display image.

</br>

### Output sample:

| Original Image                         | Gray Image                       | Binary Image                       | Contours Detected Image            |
| -------------------------------------- | -------------------------------- | ---------------------------------- | ---------------------------------- |
| ![origin-thumbnail](/images/shape.jpg) | ![g-thumbnail](/images/gray.jpg) | ![b-thumbnail](/images/binary.jpg) | ![o-thumbnail](/images/output.jpg) |
