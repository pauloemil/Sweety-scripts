import cv2 as cv #computer vision


img = cv.imread('C:\\Users\\buglow\\Desktop\\shapes.png')   #bringing the photo by path


                              # ====> Segmantation | pre-processing <====


imgGrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)                               #convert to gray scale
_, thrash = cv.threshold(imgGrey, 240, 255, cv.THRESH_BINARY)               #cnvt ->b&w (src, sabet, abyad, el method(if > sabet -->put abyad)
contours, _ = cv.findContours(thrash, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
                                                                            # Contours can be explained simply as a
                                                                            # curve joining all the continuous points
                                                                            # (along the boundary), having same color or intensity.

#view for clarification
cv.imshow("Original", img) #give window with the title shapes contain the image
cv.waitKey(0)              #wait any key
cv.destroyAllWindows()     #to destroy all after the key :B

cv.imshow("GRAY Scale", imgGrey) #give window with the title shapes contain the image
cv.waitKey(0)                    #wait any key
cv.destroyAllWindows()           #to destroy all after the key :B


for contour in contours:
                                # ====> Do the Job like a boss  <====


    epsilon = 0.01*cv.arcLength(contour, True)               #calc el epsilon value by kikking el coeff. f el arc-length of countour
    approx = cv.approxPolyDP(contour, epsilon, True)         #extracting points in a 2d array

    cv.drawContours(img, [approx], -1, (0, 150, 255), 6)     #draw on src contours with approx points, all, color, thickness


    x = approx.ravel()[0] -7 #ravel return flated array  wierdoo :P
    y = approx.ravel()[1] -7
#print(approx, len(approx))


                        #  ====> Take decision According to the number of points <=====


    if len(approx) == 3:
        cv.putText(img, "Triangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
    elif len(approx) == 4:
        x1, y1, w, h = cv.boundingRect(approx) #Xtract (first point) and (width and height)
        ratio = float(w)/h
        if 0.8 <= ratio <= 1.3:
            cv.putText(img, "Square", (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0)) #src, text, set(point), fontType, fontSize, RGBcolor
        else:
            cv.putText(img, "Rectangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
    elif len(approx) == 5:
        cv.putText(img, "Pentagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
    elif len(approx) == 6:
        cv.putText(img, "Hexagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
    elif len(approx) == 10:
        cv.putText(img, "Star", (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
    else:
        cv.putText(img, "Circle", (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))

cv.imshow("Final Result", img) #give window with the title shapes contain the image
cv.waitKey(0)                  #wait any key
cv.destroyAllWindows()         #to destroy all after the key :B
#----------------------------|
#                            |
# Done on 7:40 10/3/2020     |
# Paulo's Team:              |
#   Paulo Emil 2             |
#   Gamal Ashraf Gamal 2     |
#   Akram Diaa Abaas 2       |
#   Remon Wagde Marzouk 3    |
#----------------------------|
