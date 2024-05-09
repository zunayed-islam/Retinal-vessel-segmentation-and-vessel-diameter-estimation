"""
===========================
@Author  : Pranjal Rai
@Version: 1.0    12/07/2020
Retinal vessel segmentation 
and diameter estimation
===========================
"""



import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import diameter_calc


img = cv2.imread("C:\\Users\\zunay\\OneDrive\\Desktop\\499_project\\Retinal-vessel-segmentation-and-vessel-diameter-estimation\\Images\\image.png")


diameter_calc.diameter(img)