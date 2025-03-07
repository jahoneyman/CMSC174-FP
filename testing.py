from copyreg import constructor
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2


# construct the argument parse and parse the arguments

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#                 help="path to the input image")
# args = vars(ap.parse_args())
# define the answer key which maps the question number
# to the correct answer
ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1}

# load the image, convert it to grayscale, blur it
# slightly, then find edges
img = cv2.imread('test.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0)
cnts = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

output = img.copy
cv2.drawContours(output, cnts, -1, (0, 0, 255), 3)

cv2.imshow("Exam", output)
cv2.waitKey(0)


# thresh = cv2.threshold(edged, 0, 255,
#                        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]


# # find contours in the thresholded image, then initialize
# # the list of contours that correspond to questions
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
#                         cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# questionCnts = []
# # loop over the contours
# for c in cnts:
#     # compute the bounding box of the contour, then use the
#     # bounding box to derive the aspect ratio
#     (x, y, w, h) = cv2.boundingRect(c)
#     ar = w / float(h)
#     # in order to label the contour as a question, region
#     # should be sufficiently wide, sufficiently tall, and
#     # have an aspect ratio approximately equal to 1
#     if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
#         questionCnts.append(c)

# # sort the question contours top-to-bottom, then initialize
# # the total number of correct answers
# questionCnts = contours.sort_contours(questionCnts,
#                                       method="top-to-bottom")[0]
# correct = 0
# # each question has 5 possible answers, to loop over the
# # question in batches of 5
# for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
#     # sort the contours for the current question from
#     # left to right, then initialize the index of the
#     # bubbled answer
#     cnts = contours.sort_contours(questionCnts[i:i + 5])[0]
#     bubbled = None

#     # loop over the sorted contours
#     for (j, c) in enumerate(cnts):
#         # construct a mask that reveals only the current
#         # "bubble" for the question
#         mask = np.zeros(thresh.shape, dtype="uint8")
#         cv2.drawContours(mask, [c], -1, 255, -1)
#         # apply the mask to the thresholded image, then
#         # count the number of non-zero pixels in the
#         # bubble area
#         mask = cv2.bitwise_and(thresh, thresh, mask=mask)
#         total = cv2.countNonZero(mask)
#         # if the current total has a larger number of total
#         # non-zero pixels, then we are examining the currently
#         # bubbled-in answer
#         if bubbled is None or total > bubbled[0]:
#             bubbled = (total, j)

#             # initialize the contour color and the index of the
#         # *correct* answer
#         color = (0, 0, 255)
#         k = ANSWER_KEY[q]
#         # check to see if the bubbled answer is correct
#         if k == bubbled[1]:
#             color = (0, 255, 0)
#             correct += 1
#         # draw the outline of the correct answer on the test
#         cv2.drawContours(paper, [cnts[k]], -1, color, 3)

# score = (correct / 5.0) * 100
# print("[INFO] score: {:.2f}%".format(score))
# cv2.putText(paper, "{:.2f}%".format(score), (10, 30),
#             cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
# cv2.imshow("Original", image)
# cv2.imshow("Exam", paper)
# cv2.waitKey(0)
