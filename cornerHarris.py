# -*- coding: utf-8 -*-
"""
Created on Wed May 19 13:19:16 2021

@author: user
"""
import cv2

def cH(img):
    #
    blockSize = 2
    kSize = 3
    k = 0.04
    #thread_value = 85
    
    original_img = cv2.imread(img)
    gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    after_Harris_img = cv2.cornerHarris(gray_img, blockSize, kSize, k, cv2.BORDER_DEFAULT)
    norm_image = cv2.normalize(after_Harris_img, 0, 255, cv2.NORM_MINMAX)
    scaled_image = cv2.convertScaleAbs(norm_image)
    '''
    for (i in range(norm_image.rows)):
        for (int j = 0; j < norm_image.cols; j++):
            if ((int)norm_image.at<float>(i, j) > thread_value):
                cv::circle(orignal_image, cv::Point(j, i), 10, cv::Scalar(10, 10, 255), 1, 8, 0);  //tag the corner

    cv::imshow("after_harris_corner", orignal_image);
    cv::imwrite("after_harris_corner.png",orignal_image);
    cv::waitKey(0);
    '''
    cv2.imshow('Normalized Image', scaled_image)
    cv2.waitKey(5000)
  
if __name__ == "__main__":
    img_add = 'test.png'
    cH(img_add)

