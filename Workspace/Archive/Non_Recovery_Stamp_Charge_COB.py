import pandas as pd
import numpy as np



# Define the D matrix
D = np.array([
    [26, 20, 10,10,10,9, 0,0, 5,5,5, 0,0, 0],
    [26, 20, 10,10,10,9, 0,0, 5,5,5, 0,0, 0],
    [26, 20, 10,10,10,9, 0,0, 5,5,5, 0,0, 0],
    [26, 20, 10,10,10,9, 0,0, 5,5,5, 0,0, 0],
    [22, 17, 8,8,7,7, 0,0, 6,5,5, 7,8, 0],
    [22, 17, 8,8,7,7, 0,0, 6,5,5, 7,8, 0],
    [22, 17, 8,8,7,7, 0,0, 6,5,5, 7,8, 0],    
    [22, 17, 8,8,7,7, 0,0, 6,5,5, 7,8, 0],
    [22, 17, 8,8,7,7, 0,0, 6,5,5, 7,8, 0],
    [24, 20, 8,8,8,8, 0,0, 6,5,5, 4,4, 0],
    [24, 20, 8,8,8,8, 0,0, 6,5,5, 4,4, 0],
    [24, 20, 8,8,8,8, 0,0, 6,5,5, 4,4, 0],
    [24, 20, 8,8,8,8, 0,0, 6,5,5, 4,4, 0],
    [24, 20, 8,8,8,8, 0,0, 6,5,5, 4,4, 0],
    [22, 26, 8,8,8,8, 0,0, 7,7,7, 0,0, 0],
    [16, 18, 9,9,8,8, 7,7, 6,6,6, 0,0, 0],
    [16, 18, 9,9,8,8, 7,7, 6,6,6, 0,0, 0],
    [16, 18, 9,9,8,8, 7,7, 6,6,6, 0,0, 0],
    [22, 20, 10,10,9,9, 0,0, 7,7,6, 0, 0,0],
    [17, 17, 10,10,9,9, 7,7, 5,5,4, 0, 0,0],
    [17, 17, 10,10,9,9, 7,7, 5,5,4, 0, 0,0],
    [17, 17, 10,10,9,9, 7,7, 5,5,4, 0, 0,0],
    [17, 17, 10,10,9,9, 7,7, 5,5,4, 0, 0,0],
    [17, 17, 10,10,9,9, 7,7, 5,5,4, 0, 0,0],
   [17, 17, 10,10,9,9, 7,7, 5,5,4, 0, 0,0],
    [17, 17, 10,10,9,9, 7,7, 5,5,4, 0, 0,0],
    [17, 17, 10,10,9,9, 7,7, 5,5,4, 0, 0,0],
    [17, 17, 10,10,9,9, 7,7, 5,5,4, 0, 0,0],
    [18, 19, 9,9,9,9, 7,6,6, 4,4, 0, 0,0],
    [18, 19, 9,9,9,9, 7,6,6, 4,4, 0, 0,0],
    [18, 19, 9,9,9,9, 7,6,6, 4,4, 0, 0,0],
    [18, 19, 9,9,9,9, 7,6,6, 4,4, 0, 0,0],
    [18, 19, 9,9,9,9, 7,6,6, 4,4, 0, 0,0],
    [18, 19, 9,9,9,9, 7,6,6, 4,4, 0, 0,0],
    [18, 19, 9,9,9,9, 7,6,6, 4,4, 0, 0,0],
    [18, 19, 9,9,9,9, 7,6,6, 4,4, 0, 0,0],
    [18, 19, 9,9,9,9, 7,6,6, 4,4, 0, 0,0],
    [18, 25, 11,11,10,10, 0,0,5,5,5, 0, 0,0],
    [18, 25, 11,11,10,10, 0,0,5,5,5, 0, 0,0],
   [18, 25, 11,11,10,10, 0,0,5,5,5, 0, 0,0],
    [18, 25, 11,11,10,10, 0,0,5,5,5, 0, 0,0],
    [18, 25, 11,11,10,10, 0,0,5,5,5, 0, 0,0],
    [18, 25, 11,11,10,10, 0,0,5,5,5, 0, 0,0],
    [18, 25, 11,11,10,10, 0,0,5,5,5, 0, 0,0],
    [18, 25, 11,11,10,10, 0,0,5,5,5, 0, 0,0],
    [18, 25, 11,11,10,10, 0,0,5,5,5, 0, 0,0],
    [22, 22, 9,9,9,8, 0,0, 5,5,6, 0,0, 5],
    [22, 22, 9,9,9,8, 0,0, 5,5,6, 0,0, 5],
    [22, 22, 9,9,9,8, 0,0, 5,5,6, 0,0, 5],
    [22, 22, 9,9,9,8, 0,0, 5,5,6, 0,0, 5],
    [22, 22, 9,9,9,8, 0,0, 5,5,6, 0,0, 5],
    [22, 22, 9,9,9,8, 0,0, 5,5,6, 0,0, 5]
])

# Define the P matrix
P = np.array([
    [18.25, 21, 10, 21, 25, 950, 1.2, 85, 445, 480, 505, 60, 0.6, 0.065, 7],
    [18.5, 25.5, 10, 26, 28, 3750, 1, 65, 435, 470, 505, 70, 0.65, 0.07, 3],
    [11.86, 23.04, 10, 18, 25, 1200, 1.25, 68, 400, 425, 495, 85, 0.45, 0.056, 7.5],
    [9, 24.5, 10, 20, 28, 1100, 1.17, 70, 410, 460, 500, 90, 0.53, 0.025, 8],
    [8.97, 24.8, 9.3, 21, 30, 315, 1.15, 82, 395, 450, 495, 75, 0.48, 0.088, 7.5],
    [8.5, 24.5, 10, 20, 31, 1500, 1.15, 75, 405, 455, 495, 90, 0.5, 0.04, 8],
    [9.8, 28, 10, 19, 25, 2000, 1.1,80,400 , 450, 485, 85, 0.48, 0.06, 7],
     [9.5, 27.5, 9, 25, 29, 3000, 0.95, 65, 395, 450, 485, 90, 0.66, 0.08, 7],
    [8.1, 24.4, 9, 20, 30, 300, 1.15, 78, 420, 455, 485, 65, 0.44, 0.061, 7],
    [8.7, 33.8, 8, 27, 32, 3000, 0.93, 96, 380, 470, 495, 80, 0.66, 0.03, 8],
    [8.5, 19.5, 9.5, 28, 35, 10, 1.38, 82, 440, 450, 490, 55, 0.45, 0.045, 5.5],
    [8.9, 20.5, 9, -22, 14, 1050, 1.51, 93, 427, 469, 503, 34, 0.68, 0.45, 9],
    [7.4, 23.7, 10.6, 18, 28, 440, 1.21, 85, 420, 437, 485, 65, 0.38, 0.087, 7.5],
    [10.5 ,19.5 ,8 ,0 ,0 ,0 ,1.23 ,51 ,0 ,0 ,0,0 ,0.45 ,0.07 ,1]
])

Coke_properties = np.array([
    [16.00, 0.93, 4.17, 0.78, 1.56, 18.64, 33.00, 24.25, 6.93, 92.47, 6.20, 4.33, 67.10, 25.10,53.91],
    [15.52, 0.85, 4.60, 0.78, 1.71, 19.08, 34.57, 22.63, 6.50, 92.47, 6.13, 4.40, 67.40, 23.90,54.34],
    [16.18, 0.90, 4.63, 0.78, 1.74, 19.37, 33.23, 22.70, 6.37, 92.33, 6.27, 4.40, 67.80, 24.00,54.68],
    [16.02, 0.97, 3.77, 0.78, 1.59, 18.95, 33.21, 22.98, 6.67, 92.40, 6.27, 4.33, 67.50, 24.10,54.45],
    [15.77, 0.90, 4.37, 0.78, 1.76, 18.41, 33.91, 23.94, 6.63, 92.96, 6.22, 3.82, 67.20, 23.40,54.50],
    [15.48, 0.97, 4.20, 0.78, 1.62, 18.86, 34.32, 23.31, 6.60, 92.74, 5.73, 4.53, 68.80, 22.00,54.30],
    [15.40, 0.90, 4.20, 0.78, 1.37, 18.99, 33.76, 24.48, 6.43, 92.60, 6.13, 4.27, 68.50, 23.30,54.04],
    [15.13, 0.92, 4.17, 0.78, 1.31, 19.58, 33.30, 25.10, 6.03, 92.80, 6.13, 4.07, 68.70, 22.10,54.04],
    [15.13, 0.95, 4.20, 0.78, 1.44, 19.49, 33.14, 24.37, 6.53, 92.87, 6.13, 4.00, 68.90, 23.10,53.94],
    [15.25, 0.88, 4.00, 0.71, 1.59, 19.33, 32.89, 23.62, 6.37, 92.67, 6.95, 4.38, 68.40, 22.60,53.85],
    [15.70, 0.97, 4.10, 0.78, 1.61, 16.47, 36.76, 25.95, 6.47, 92.60, 6.20, 4.20, 67.80, 24.00,54.29],
    [15.20, 0.90, 4.07, 0.78, 0.99, 17.94, 34.52, 24.72, 6.40, 92.67, 6.13, 4.20, 65.60, 23.40,54.12],
    [15.10, 0.90, 4.40, 0.78, 1.59, 18.96, 33.30, 23.35, 6.60, 93.00, 6.20, 3.80, 0.78, 0.78,53.98],
    [14.75, 0.83, 3.90, 0.78, 1.12, 17.56, 35.63, 24.15, 6.35, 92.50, 6.10, 4.40, 68.30, 23.00,53.68],
    [15.33, 0.93, 4.20, 0.78, 1.88, 18.48, 33.05, 24.82, 6.40, 92.53, 6.93, 4.53, 69.03, 22.39,53.61],
    [16.03, 0.95, 3.84, 1.00, 1.72, 18.90, 33.78, 23.07, 6.70, 92.50, 6.00, 4.50, 67.89, 25.14,54.41],
    [15.73, 0.98, 4.03, 0.78, 1.57, 20.23, 32.53, 23.42, 6.43, 92.80, 6.20, 4.00, 69.88, 22.44,54.58],
    [15.07, 0.90, 4.85, 0.78, 1.41, 19.46, 32.60, 23.80, 6.70, 92.40, 6.00, 4.60, 67.10, 23.60,53.89],
    [15.00, 1.00, 4.43, 1.20, 2.08, 18.29, 33.53, 24.30, 6.03, 92.60, 6.07, 4.33, 68.05, 24.06,54.10],
    [15.35, 0.88, 3.80, 0.85, 1.70, 17.97, 33.86, 24.66, 6.50, 92.07, 6.33, 4.60, 68.10, 24.43,54.10],
    [14.95, 0.98, 3.80, 0.91, 1.70, 19.02, 34.25, 23.17, 5.87, 92.80, 6.87, 4.33, 68.73, 24.22,53.87],
    [15.45, 1.00, 3.77, 1.39, 1.68, 19.65, 31.61, 24.28, 6.77, 92.60, 6.13, 4.27, 69.70, 23.30,54.27],
    [15.10, 1.04, 3.57, 0.88, 1.66, 18.54, 34.18, 23.76, 5.97, 92.67, 6.00, 4.33, 68.70, 23.60,53.91],
    [15.22, 1.00, 3.77, 0.78, 1.57, 18.64, 33.21, 24.00, 6.00, 92.60, 6.00, 4.40, 69.20, 23.80,53.95],
    [15.15, 1.08, 3.57, 0.78, 1.83, 19.42, 32.12, 23.92, 6.53, 92.60, 6.13, 4.27, 68.90, 23.40,54.31],
    [15.25, 0.97, 3.80, 0.78, 1.73, 19.19, 32.63, 23.52, 6.67, 92.47, 6.13, 4.40, 66.10, 26.50,53.50],
    [14.92, 1.08, 3.60, 0.78, 1.62, 18.91, 32.97, 24.27, 6.80, 92.40, 6.13, 4.47, 67.30, 24.30,54.15],
    [14.88, 0.98, 3.87, 0.78, 1.49, 18.71, 32.70, 23.71, 6.43, 92.47, 6.13, 4.40, 67.00, 23.00,54.01],
    [15.48, 0.97, 4.20, 0.78, 1.62, 18.86, 34.32, 23.31, 6.60, 92.74, 5.73, 4.53, 68.80, 22.00,53.86],
    [15.40, 0.90, 4.20, 0.78, 1.37, 18.99, 33.76, 24.48, 6.43, 92.60, 6.13, 4.27, 68.50, 23.30,54.07],
    [15.13, 0.92, 4.17, 0.78, 1.31, 19.58, 33.30, 25.10, 6.03, 92.80, 6.13, 4.07, 68.70, 22.10,54.39],
    [15.13, 0.95, 4.20, 0.78, 1.44, 19.49, 33.14, 24.37, 6.53, 92.87, 6.13, 4.00, 68.90, 23.10,54.44],
    [15.25, 0.88, 4.00, 0.71, 1.59, 19.33, 32.89, 23.62, 6.37, 92.67, 5.95, 4.38, 68.40, 22.60,53.88],
    [15.70, 0.97, 4.10, 0.78, 1.61, 16.47, 36.76, 25.95, 6.47, 92.60, 6.20, 4.20, 67.80, 24.00,54.52],
    [15.20, 0.90, 4.07, 0.78, 0.99, 17.94, 34.52, 24.72, 6.40, 92.67, 6.13, 4.20, 65.60, 23.40,54.23],
    [15.10, 0.90, 4.40, 0.78, 1.59, 18.96, 33.30, 23.35, 6.60, 93.00, 6.20, 3.80, 68.50, 23.30,54.02],
    [14.75, 0.83, 3.90, 0.78, 1.12, 17.56, 35.63, 24.15, 6.35, 92.50, 6.10, 4.40, 68.30, 23.00,54.40],
    [15.33, 0.93, 4.20, 0.78, 1.88, 18.48, 33.05, 24.82, 6.40, 92.53, 5.93, 4.53, 69.03, 22.39,53.80],
    [16.03, 0.95, 3.84, 1.00, 1.72, 18.90, 33.78, 23.07, 6.70, 92.50, 6.00, 4.50, 67.89, 25.14,54.30],
    [15.73, 0.98, 4.03, 0.78, 1.57, 20.23, 32.53, 23.42, 6.43, 92.80, 6.20, 4.00, 69.88, 22.44,54.26],
    [15.07, 0.90, 4.85, 0.78, 1.41, 19.46, 32.60, 23.80, 6.70, 92.40, 6.00, 4.60, 67.10, 23.60,53.74],
    [15.00, 1.00, 4.43, 1.20, 2.08, 18.29, 33.53, 24.30, 6.03, 92.60, 6.07, 4.33, 68.05, 24.06,53.86],
    [15.35, 0.88, 3.80, 0.85, 1.70, 17.97, 33.86, 24.66, 6.50, 92.07, 6.33, 4.60, 68.10, 24.43,54.06],
    [14.95, 0.98, 3.80, 0.91, 1.70, 19.02, 34.25, 23.17, 5.87, 92.80, 5.87, 4.33, 68.73, 24.22,54.46],
    [15.45, 1.00, 3.77, 1.39, 1.68, 19.65, 31.61, 24.28, 6.77, 92.60, 6.13, 4.27, 69.70, 23.30,54.12],
    [15.10, 1.04, 3.57, 0.88, 1.66, 18.54, 34.18, 23.76, 5.97, 92.67, 6.00, 4.33, 68.70, 23.60,54.09],
    [15.22, 1.00, 3.77, 0.78, 1.57, 18.64, 33.21, 24.00, 6.00, 92.60, 6.00, 4.40, 69.20, 23.80,54.20],
    [15.15, 1.08, 3.57, 0.78, 1.83, 19.42, 32.12, 23.92, 6.53, 92.60, 6.13, 4.27, 68.90, 23.40,53.88],
    [15.25, 0.97, 3.80, 0.78, 1.73, 19.19, 32.63, 23.52, 6.67, 92.47, 6.13, 4.40, 66.10, 26.50,54.87],
    [14.92, 1.08, 3.60, 0.78, 1.62, 18.91, 32.97, 24.27, 6.80, 92.40, 6.13, 4.47, 67.30, 24.30,54.07],
    [14.88, 0.98, 3.87, 0.78, 1.49, 18.71, 32.70, 23.71, 6.43, 92.47, 6.13, 4.40, 67.00, 23.00,54.34],
    [14.65, 0.95, 3.77, 0.78, 1.62, 19.29, 32.63, 24.13, 6.27, 92.67, 6.13, 4.20, 65.93, 23.42,54.01]

])




import numpy as np



Process_parameters = np.array([
      [50.83, 9.97, 1.13, 1002.84, 1364.93, 248.82, 99.93, 34.33, 73.97, 1127.73, 64.23, 1074.25, 5.03],
    [49.11, 10.06, 1.09, 1017.92, 1310, 244.55, 97.56, 34.44, 73.34, 1114.55, 65.46, 1074.07, 4.97],
    [50.96, 9.79, 1.11, 1014.22, 1376.5, 247.27, 98, 34.95, 72.2, 1112.6, 65.27, 1078.79, 5.01],
    [50.67, 9.89, 1.13, 1027.02, 1333.71, 256.13, 97.05, 33.6, 74.02, 1102.5, 65.04, 1070.44, 5.05],
    [49.87, 10.23, 1.12, 993.21, 1311.57, 247.83, 97.38, 34.16, 72.96, 1125.46, 66.67, 1044.71, 4.95],
    [51.45, 10.16, 1.1, 1027.14, 1331.89, 245.29, 97.04, 34.35, 74.77, 1108.91, 65.78, 1069.67, 4.88],
    [51.13, 9.83, 1.07, 980.98, 1352, 248.16, 98.94, 33.73, 71.77, 1089.05, 64.47, 1051.03, 5.01],
    [51.04, 10.2, 1.07, 1014.35, 1367, 244.09, 103, 34.99, 74.25, 1073.09, 67.37, 1053.99, 5.08],
    [50.81, 9.75, 1.09, 981.85, 1384.04, 244.12, 102.24, 33.92, 74.12, 1084.77, 66.55, 1028.49, 4.94],
    [51.29, 10.01, 1.09, 990.64, 1388.71, 248.61, 97.65, 35.26, 73.42, 1126.68, 65.96, 1074.4, 4.85],
    [49.47, 9.84, 1.07, 975.38, 1380.8, 244.88, 99.76, 34.61, 71.15, 1124, 67.76, 1067.42, 4.97],
    [49.88, 9.74, 1.08, 977.49, 1325.57, 247.6, 102.51, 35.23, 74.82, 1112.84, 65.66, 1032.44, 4.9],
    [49.1, 10.13, 1.08, 1009.96, 1352.18, 253.93, 102.36, 33.69, 72.16, 1091.56, 66.37, 1024.54, 4.86],
    [49.16, 10.11, 1.11, 994.16, 1382.34, 245.54, 101.84, 33.5, 71.13, 1096.8, 64.14, 1075.01, 4.92],
    [49.52, 9.92, 1.1, 988.59, 1380.23, 256.1, 97.62, 35.16, 74.14, 1078.86, 65.45, 1037.63, 5.15],
    [49.74, 9.93, 1.11, 1021.65, 1325.07, 244.38, 99.66, 35.19, 73.46, 1092.23, 67.12, 1026.08, 5.01],
    [49.54, 10.21, 1.1, 990.58, 1336.37, 256.59, 97.92, 35.41, 73.72, 1101.21, 65.28, 1063.67, 4.92],
    [50.8, 10.08, 1.09, 1003.51, 1352.06, 249.96, 98.72, 34.01, 70.91, 1119.78, 66.88, 1079.4, 5.1],
    [50.4, 9.92, 1.12, 991.97, 1327.81, 248.46, 98.88, 34.23, 73.63, 1083.92, 64.65, 1023, 4.95],
    [48.81, 9.91, 1.11, 990.09, 1372.56, 254.03, 97.52, 35.35, 71.34, 1099.96, 65.33, 1021.45, 5.15],
    [50.58, 9.83, 1.11, 1007.08, 1337.25, 242.54, 101.87, 35.28, 74.3, 1089.24, 64.67, 1025.42, 4.86],
    [49.52, 10.27, 1.08, 1028.32, 1313.39, 249.5, 99.36, 33.8, 74.21, 1110.62, 67.31, 1038.91, 4.99],
    [48.65, 10.21, 1.12, 984.65, 1318.26, 248.58, 98.51, 34.28, 75.09, 1084.73, 66.05, 1035.83, 5.11],
    [49.76, 10.09, 1.09, 984.83, 1364.32, 256.23, 99.24, 34.1, 73.43, 1094.72, 65.01, 1079.83, 5.13],
    [50.62, 10.2, 1.09, 983.8, 1369.18, 243.14, 98.87, 34.72, 72.08, 1120.72, 65.55, 1023.36, 4.92],
    [49.78, 9.77, 1.13, 1005.2, 1339.72, 243.43, 99.42, 34.7, 74.3, 1073.18, 67.59, 1054.38, 4.93],
    [49.12, 10.21, 1.1, 985.79, 1354.52, 252.44, 101.8, 35.28, 72.74, 1131.54, 65.03, 1034.74, 5.05],
    [48.76, 10.22, 1.09, 1002.01, 1346.15, 244.86, 97.12, 33.52, 71.99, 1092.47, 66.65, 1047.09, 4.99],
    [51.27, 9.85, 1.08, 1029.98, 1339.65, 251.55, 101.98, 35.19, 74.23, 1126.15, 64.1, 1040.03, 5.14],
    [50.12, 9.79, 1.13, 1010.89, 1327.61, 254.5, 98.72, 33.9, 74.99, 1084.55, 65.22, 1080.42, 4.91],
    [50.41, 9.77, 1.1, 988.78, 1313.11, 250.18, 98.03, 34.24, 71.96, 1119.16, 64.53, 1020.69, 4.96],
    [50.45, 10.01, 1.12, 1009.66, 1344.33, 256.01, 99.34, 33.94, 74.66, 1098.77, 67.81, 1076.1, 4.97],
    [51.1, 9.75, 1.13, 991.05, 1384.43, 245.15, 97.38, 34.13, 72.15, 1108.8, 66.81, 1019.08, 5.03],
    [49.05, 9.88, 1.1, 1002.79, 1324.67, 250.72, 102.82, 33.82, 74.48, 1128.24, 64.65, 1067.03, 5.01],
    [49.53, 10.17, 1.13, 976.47, 1358.48, 243.49, 99.22, 35.4, 71.3, 1129.25, 66.01, 1064.94, 5.1],
    [48.74, 10.25, 1.12, 1003.86, 1315.35, 242.81, 97.26, 35.05, 73.92, 1100.15, 65.42, 1025.58, 4.85],
    [49.43, 10.26, 1.1, 1026.23, 1327.9, 246.9, 101.45, 33.92, 73.29, 1072.98, 64.53, 1069.52, 5.03],
    [48.51, 9.81, 1.1, 988.86, 1354.13, 254.53, 101.56, 34.71, 71.09, 1082.89, 65.55, 1071.35, 5.09],
    [49.22, 10.29, 1.1, 978.54, 1386.43, 244.62, 99.65, 34.75, 72.3, 1076.04, 66.65, 1063.82, 5],
    [51, 9.78, 1.08, 1020.48, 1326.99, 254.35, 100.43, 33.85, 74.62, 1120.84, 66.33, 1076.34, 4.92],
    [50.84, 9.99, 1.12, 971.96, 1316.58, 253.99, 98.98, 34.99, 71.35, 1116.27, 65.22, 1058.67, 4.91],
    [49.24, 10.02, 1.11, 990.77, 1343.5, 257.01, 99.96, 33.92, 71.99, 1090.69, 65.26, 1071.43, 5.07],
    [50.76, 9.79, 1.09, 1005.43, 1311.38, 248.55, 98.78, 34.14, 71.57, 1093.81, 65.71, 1080.44, 5.08],
    [50, 10.1, 1.13, 988.45, 1323.12, 248.22, 97.46, 35.13, 73.71, 1070.88, 65.79, 1064.63, 4.87],
    [51.14, 9.89, 1.09, 982.85, 1350.42, 254.16, 102, 34.51, 73.11, 1105.56, 64.92, 1034.79, 5.14],
    [49.71, 9.99, 1.07, 1001.55, 1345.38, 256.04, 101.12, 35.39, 71.82, 1123.25, 65.03, 1049.52, 4.95],
    [50.02, 9.94, 1.08, 999.48, 1358.65, 254.61, 99.82, 34.26, 71.73, 1088.98, 64.23, 1066.78, 4.92],
    [49.85, 10.09, 1.08, 997.38, 1379.88, 254.84, 98.14, 33.63, 72.32, 1094.21, 64.82, 1039.46, 5.1],
    [50.91, 10.21, 1.12, 1024.18, 1358.81, 253.74, 102.4, 35.13, 72.08, 1105.1, 65.59, 1079.03, 5.07],
    [48.65, 9.73, 1.12, 1026.98, 1387, 257.05, 100.53, 35.2, 73.55, 1069.17, 67, 1031.05, 4.89],
    [50.51, 9.79, 1.08, 976.28, 1384.31, 249.11, 101.44, 34.6, 74.48, 1069.66, 66.19, 1061.69, 5.14],
    [49.9, 10.13, 1.1, 985.88, 1369.32, 252.27, 101.42, 34.82, 71.54, 1080.69, 66.47, 1059.76, 5.13]
      ])


B = np.dot(D, P)
B = B / 100
Blended_coal_parameters = np.array([
    [11.86, 23.04, 10.03, 18, 28, 903, 85.5, 46.38, 408, 423, 482, 78.9, 0.38, 0.06, 6],
    [11.86, 23.04, 10.03, 19, 37, 903, 85.5, 46.38, 408, 423, 482, 78.9, 0.38, 0.06, 6],
    [11.86, 23.04, 10.03, 18, 19, 903, 85.5, 46.38, 408, 423, 482, 78.9, 0.38, 0.06, 6],
    [11.86, 23.04, 10.03, 19, 32, 903, 85.5, 46.38, 408, 423, 482, 78.9, 0.38, 0.06, 6],
    [11.61, 23.36, 10.75, 19, 51, 1256, 85.78, 46.51, 398, 427, 482, 79.8, 0.38, 0.06, 6],
    [11.61, 23.36, 10.75, 20, 32, 1256, 85.78, 46.51, 398, 427, 482, 79.8, 0.38, 0.06, 6],
    [11.61, 23.36, 10.75, 20, 59, 1256, 85.78, 46.51, 398, 427, 482, 79.8, 0.38, 0.06, 6],
    [11.61, 23.36, 10.75, 20, 51, 1256, 85.78, 46.51, 398, 427, 482, 79.8, 0.38, 0.06, 6],
    [11.61, 23.36, 10.75, 19, 48, 1256, 85.78, 46.51, 398, 427, 482, 79.8, 0.38, 0.06, 6],
    [11.82, 22.89, 10.6, 18, 8, 1011, 85.81, 46.33, 410, 424, 468, 80.6, 0.35, 0.08, 6],
    [11.82, 22.89, 10.6, 19, 3, 1011, 85.81, 46.33, 410, 424, 468, 80.6, 0.35, 0.08, 6],
    [11.82, 22.89, 10.6, 20, 12, 1011, 85.81, 46.33, 410, 424, 468, 80.6, 0.35, 0.08, 6],
    [11.82, 22.89, 10.6, 20, 47, 1011, 85.81, 46.33, 410, 424, 468, 80.6, 0.35, 0.08, 6],
    [11.82, 22.89, 10.6, 20, 47, 1011, 85.81, 46.33, 410, 424, 468, 80.6, 0.35, 0.08, 6],
    [11.82, 22.89, 10.6, 19, 56, 1011, 85.81, 46.33, 410, 424, 468, 80.6, 0.35, 0.08, 6],
    [11.91,	22.9, 11.23, 18, 41, 937, 85.44, 46.2, 420,	432 ,472 , 87.4, 0.33 ,0.07,6],
    [11.91, 22.9, 11.23, 17, 21, 937, 85.44, 46.2, 420, 432, 472, 87.4, 0.33, 0.07, 6],
    [11.91, 22.9, 11.23, 19, 26, 937, 85.44, 46.2, 420, 432, 472, 87.4, 0.33, 0.07, 6],
    [11.91, 22.9, 11.23, 18, 20, 937, 85.44, 46.2, 420, 432, 472, 87.4, 0.33, 0.07, 6],
    [10.3, 23.51, 10.3, 18, 57, 1366, 84.77, 45.93, 420, 432, 472, 87.4, 0.33, 0.07, 6],
    [10.3, 23.51, 10.3, 20, 23, 1366, 84.77, 45.93, 350, 427, 472, 81.4, 0.36, 0.08, 6],
    [10.3, 23.51, 10.3, 21, 33, 1366, 84.77, 45.93, 350, 427, 472, 81.4, 0.36, 0.08, 6],
    [10.3, 23.51, 10.3, 19, 54, 1366, 84.77, 45.93, 350, 427, 472, 81.4, 0.36, 0.08, 6],
    [10.3, 23.51, 10.3, 21, 52, 1366, 84.77, 45.93, 350, 427, 472, 81.4, 0.36, 0.08, 6],
    [10.3, 23.51, 10.3, 19, 62, 1366, 84.77, 45.93, 350, 427, 472, 81.4, 0.36, 0.08, 6],
    [10.3, 23.51, 10.3, 22, 45, 1366, 84.77, 45.93, 350, 427, 472, 81.4, 0.36, 0.08, 6],
    [10.3, 23.51, 10.3, 19, 24, 1366, 84.77, 45.93, 350, 427, 472, 81.4, 0.36, 0.08, 6],
    [10.3, 23.51, 10.3, 19, 43, 1366, 84.77, 45.93, 350, 427, 472, 81.4, 0.36, 0.08, 6],
    [11.76, 23.3, 10.67, 18, 28, 1119, 86.17, 46.33, 309, 415, 473, 85, 0.39, 0.07, 6],
    [11.76, 23.3, 10.67, 18, 31, 1119, 86.17, 46.33, 309, 415, 473, 85, 0.39, 0.07, 6],
    [11.76, 23.3, 10.67, 18, 33, 1119, 86.17, 46.33, 309, 415, 473, 85, 0.39, 0.07, 6],
    [11.76, 23.3, 10.67, 20, 56, 1119, 86.17, 46.33, 309, 415, 473, 85, 0.39, 0.07, 6],
    [11.76, 23.3, 10.67, 20, 58, 1119, 86.17, 46.33, 309, 415, 473, 85, 0.39, 0.07, 6],
    [11.76, 23.3, 10.67, 19, 39, 1119, 86.17, 46.33, 309, 415, 473, 85, 0.39, 0.07, 6],
    [11.76, 23.3, 10.67, 21, 63, 1119, 86.17, 46.33, 309, 415, 473, 85, 0.39, 0.07, 6],
    [11.76, 23.3, 10.67, 21, 44, 1119, 86.17, 46.33, 309, 415, 473, 85, 0.39, 0.07, 6],
    [11.76, 23.3, 10.67, 20, 33, 1119, 86.17, 46.33, 309, 415, 473, 85, 0.39, 0.07, 6],
    [11.86, 23.04, 10.35, 20, 47, 836, 85.82, 46.29, 378, 425, 480, 81.9, 0.34, 0.08, 6],
    [11.86, 23.04, 10.35, 21, 54, 836, 85.82, 46.29, 378, 425, 480, 81.9, 0.34, 0.08, 6],
    [11.86, 23.04, 10.35, 20, 51, 836, 85.82, 46.29, 378, 425, 480, 81.9, 0.34, 0.08, 6],
    [11.86, 23.04, 10.35, 22, 40, 836, 85.82, 46.29, 378, 425, 480, 81.9, 0.34, 0.08, 6],
    [11.86, 23.04, 10.35, 21, 44, 836, 85.82, 46.29, 378, 425, 480, 81.9, 0.34, 0.08, 6],
    [11.86, 23.04, 10.35, 20, 47, 836, 85.82, 46.29, 378, 425, 480, 81.9, 0.34, 0.08, 6],
    [11.86, 23.04, 10.35, 20, 37, 836, 85.82, 46.29, 378, 425, 480, 81.9, 0.34, 0.08, 6],
    [11.86, 23.04, 10.35, 20, 29, 836, 85.82, 46.29, 378, 425, 480, 81.9, 0.34, 0.08, 6],
    [11.86, 23.04, 10.35, 17, 14, 836, 85.82, 46.29, 378, 425, 480, 81.9, 0.34, 0.08, 6],
  [11.57, 23.29, 10.36, 15, 10, 763, 85.98, 46.2, 368, 418,495, 77, 0.39, 0.07, 6],
  [11.57, 23.29, 10.36, 23, 41, 763, 85.98, 46.2, 368, 418,495, 77, 0.39, 0.07, 6],
  [11.57, 23.29, 10.36, 19, 25, 763, 85.98, 46.2, 368, 418,495, 77, 0.39, 0.07, 6],
  [11.57, 23.29, 10.36, 21, 20, 763, 85.98, 46.2, 368, 418,495, 77, 0.39, 0.07, 6],
  [11.57, 23.29, 10.36, 19, 30, 763, 85.98, 46.2, 368, 418,495, 77, 0.39, 0.07, 6],
  [11.57, 23.29, 10.36, 17, 8, 763, 85.98, 46.2, 368, 418,495, 77, 0.39, 0.07, 6]
])

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
X_train, X_test, y_train, y_test = train_test_split(B, Blended_coal_parameters, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_squared_error

modelq = RandomForestRegressor(
    n_estimators=500,
    random_state=42,
)

modelq.fit(X_train, y_train)

y_pred = modelq.predict(X_test)
mse = np.mean((y_test - y_pred) ** 2)

Process_parameters = np.pad(Process_parameters, ((0, 0), (0, 2)), mode='constant', constant_values=0)

Conv_matrix=Blended_coal_parameters+Process_parameters

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
X_train, X_test, y_train, y_test = train_test_split(Conv_matrix, Coke_properties, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()



X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from sklearn.ensemble import RandomForestRegressor


rf_model = RandomForestRegressor(n_estimators=100, random_state=42)


rf_model.fit(X_train, y_train)


y_pred = rf_model.predict(X_test)


from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
# print(f"Mean Squared Error: {mse}")


min_percentages = np.array([25, 25, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0,0])
max_percentages = np.array([45, 65, 25, 20, 20, 5, 4, 0, 0, 0, 0, 0, 0,0])
def generate_combinations(index,current_combination, current_sum):
    target_sum = 100
    if index == len(min_percentages) - 1:
        remaining = target_sum - current_sum
        if min_percentages[index] <= remaining <= max_percentages[index]:
            yield current_combination + [remaining]
        return
    for value in range(min_percentages[index], max_percentages[index] + 1):
        if current_sum + value <= target_sum:
            yield from generate_combinations(index + 1, current_combination + [value], current_sum + value)


all_combinations = np.array(list(generate_combinations(0, [], 0)))
print("Number of valid combinations:", len(all_combinations))
print(all_combinations[:-1000])
print(all_combinations[0])

proces_para=[10.82, 10.75, 0.82, 46.56, 236.30, 312.80, 876.51, 32.46, 19.01, 1266.94, 17.19, 20.62, 14.38, 31.68, 2.55]

b1=np.dot(all_combinations, P)

b1=b1/100

blend1=modelq.predict(b1)

blended_coal_properties=blend1

blend1=blend1+proces_para

coke = rf_model.predict(blend1)


predictions=coke





#Get all weightages for coke properties
ash_weightage = 1
vm_weightage = 1 #i think not needed 
m40_weightage = 1
m10_weightage = 1
csn_weightage = 1
cri_weightage = 1


ash_min = 0
ash_max = 100
vm_min = 0
vm_max = 100
m40_min = 0
m40_max = 100
m10_min = 0
m10_max = 100
csn_min = 0
csn_max = 100
cri_min = 0
cri_max = 100

#desired coke parameters
desired_ash = 15.4 #less
desired_VM = 0.9   #less
desired_m40 = 92   #higher
desired_m10 = 3.2   #less
desired_csr = 65   #higher
desired_cri = 23  #less
desired_coke_parameters = [desired_ash,desired_VM,4,0.8,1.54,19,33,24,6,desired_m40,desired_m10,4,desired_csr,desired_cri]

print("blended_coal_properties1","\n")
print(blended_coal_properties,"\n")

def filter_valid_and_invalid(predictions, combinations, blended_coal_properties):
    valid_indices = []
    invalid_indices = []
    for i, prediction in enumerate(predictions):
        # Check if all values are within the specified range
        if (
            ash_min <= prediction[0] <= ash_max and  # ASH
            vm_min <= prediction[1] <= vm_max and  # VM
            m40_min <= prediction[9] <= m40_max and  # M_40
            m10_min <= prediction[10] <= m10_max and  # M_10
            csn_min <= prediction[12] <= csn_max and  # CSR
            cri_min <= prediction[13] <= cri_max  # CRI
        ):
            valid_indices.append(i)
        else:
            invalid_indices.append(i)
    # Separate valid and invalid predictions, combinations, and blended coal properties
    valid_predictions = predictions[valid_indices]
    valid_combinations = combinations[valid_indices]
    valid_blended_coal_properties = [blended_coal_properties[i] for i in valid_indices]
    print("valid_blended_coal_properties","\n")
    print(valid_blended_coal_properties[0],"\n")
    print("blended_coal_properties","\n")
    print(blended_coal_properties[0],"\n")
    invalid_predictions = predictions[invalid_indices]
    invalid_combinations = combinations[invalid_indices]
    invalid_blended_coal_properties = [blended_coal_properties[i] for i in invalid_indices]

    return (
        valid_predictions,
        valid_combinations,
        valid_blended_coal_properties,
        invalid_predictions,
        invalid_combinations,
        invalid_blended_coal_properties,
    )


# Filtering valid and invalid predictions, combinations, and blended coal properties
(
    valid_predictions,
    valid_combinations,
    valid_blended_coal_properties,
    invalid_predictions,
    invalid_combinations,
    invalid_blended_coal_properties,
) = filter_valid_and_invalid(predictions, all_combinations, blended_coal_properties)

# Printing the count of valid and invalid entries
print(f"Number of valid predictions: {len(valid_predictions)}")
print(f"Number of valid combinations: {len(valid_combinations)}")
print(f"Number of valid blended coal properties: {len(valid_blended_coal_properties)}")
print(f"Number of invalid predictions: {len(invalid_predictions)}")
print(f"Number of invalid combinations: {len(invalid_combinations)}")
print(f"Number of invalid blended coal properties: {len(invalid_blended_coal_properties)}")

# Optionally display the first few valid and invalid entries
#print("First few valid blended coal properties:", valid_blended_coal_properties[:5])
#print("First few invalid blended coal properties:", invalid_blended_coal_properties[:5])

predictions = valid_predictions
all_combinations = valid_combinations
blended_coal_properties1 = valid_blended_coal_properties


# Initialize an array to store differences
differences = []
prediction = valid_predictions
all_combinations = valid_combinations

# Calculate differences
for prediction in predictions:
    diff = []
    
    # ASH (less is better)
    diff.append(((desired_ash - prediction[0]) / desired_ash) * ash_weightage)

    # VM (less is better)
    diff.append(((desired_VM - prediction[1]) / desired_VM) * vm_weightage)

    # M_40 (higher is better)
    diff.append(((prediction[9] - desired_m40) / desired_m40) * m40_weightage)

    # M_10 (less is better)
    diff.append(((desired_m10 - prediction[10]) / desired_m10) * m10_weightage)

    # CSR (higher is better)
    diff.append(((prediction[12] - desired_csr) / desired_csr) * csn_weightage)

    # CRI (less is better)
    diff.append(((desired_cri - prediction[13]) / desired_cri) * cri_weightage)
    
    # AMS (higher is better)
    diff.append(((prediction[14] - desired_csr) / desired_csr) * csn_weightage)

    differences.append(diff)

# Calculate total differences and store in an array
total_differences = [sum(diff) for diff in differences]

# Sort the total differences (greatest first, lowest last) and get indices
sorted_indices = np.argsort(total_differences)[::-1]

# Sort predictions based on these indices
sorted_predictions = predictions[sorted_indices]
sorted_blends = all_combinations[sorted_indices]
# Sorting blended coal properties based on the sorted indices
sorted_blended_coal_properties = [blended_coal_properties1[i] for i in sorted_indices]
print("sorted_blended_coal_properties","\n")
print(sorted_blended_coal_properties,"\n")

blend_1 = sorted_blends[0]
blend_2 = sorted_blends[1]
blend_3 = sorted_blends[2]

blended_coal_1 = sorted_blended_coal_properties[0]
blended_coal_2 = sorted_blended_coal_properties[1]
blended_coal_3 = sorted_blended_coal_properties[2]


blend_1_properties = sorted_predictions[0]
blend_2_properties = sorted_predictions[1]
blend_3_properties = sorted_predictions[2]


# Printing the blend values and their corresponding properties
print("Blend 1:")
print("Blend Values:", blend_1)
print("Properties:", blend_1_properties, "\n")
print("blend_Properties:", blended_coal_1, "\n")



print("Blend 2:")
print("Blend Values:", blend_2)
print("Properties:", blend_2_properties, "\n")
print("blend_Properties:", blended_coal_2, "\n")

print("Blend 3:")
print("Blend Values:", blend_3)
print("Properties:", blend_3_properties, "\n")
print("blend_Properties:", blended_coal_3, "\n")



coal_costs = [0] * 14  # Initializing an array with 13 elements

# Example input: Replace these values with the actual costs
coal_costs = [12000, 5200, 20160, 20160, 20160, 20160, 17000, 17000, 13440, 14200, 13440, 13440, 15000,9240]


# Calculating the total cost for each prediction using the sorted blend values and coal costs
total_costs = [sum(blend[i] * coal_costs[i] / 100 for i in range(13)) for blend in sorted_blends]

total_costs


sorted_indices_by_cost = np.argsort(total_costs)

# Creating lists for sorted blends and predictions based on cost
sorted_blend_cost = sorted_blends[sorted_indices_by_cost]
sorted_prediction_cost = sorted_predictions[sorted_indices_by_cost]
sorted_total_cost = np.array(total_costs)[sorted_indices_by_cost]

sorted_blended_coal_properties_cost = [sorted_blended_coal_properties[i] for i in sorted_indices_by_cost]


# Normalizing total costs and total differences
normalized_costs = (total_costs - np.min(total_costs)) / (np.max(total_costs) - np.min(total_costs))
normalized_differences = (total_differences - np.min(total_differences)) / (np.max(total_differences) - np.min(total_differences))

# Define weights (adjust these as needed)
cost_weight = 1  # Weight for cost (can be adjusted)
performance_weight = 1  # Weight for performance (can be adjusted)

# Calculate combined scores
combined_scores = (cost_weight * normalized_costs) + (performance_weight * normalized_differences)

# Find the index of the best combined score
best_combined_index = np.argmin(combined_scores)

# Extract the best blend and its corresponding properties
best_blend_combined = sorted_blends[best_combined_index]
best_properties_combined = sorted_predictions[best_combined_index]
best_cost_combined = sorted_total_cost[best_combined_index] 
best_blended_coal_combined = sorted_blended_coal_properties_cost[best_combined_index]

# Print the results
print("Best Blend (Balanced):", best_blend_combined)
print("Properties of Best Blend (Balanced):", best_properties_combined)
print("Cost of Best Blend (Balanced):", best_cost_combined)


# Function to calculate the total cost for a blend
def calculate_cost(blend, coal_costs):
    return sum(blend[i] * coal_costs[i] / 100 for i in range(min(len(blend), len(coal_costs))))

# Blend definitions
blend_1 = sorted_blends[0]
blend_2 = sorted_blend_cost[0]
blend_3 = sorted_blends[best_combined_index]

#Blended coal properties
blended_coal_1 = sorted_blended_coal_properties[0]
blended_coal_2 = sorted_blended_coal_properties_cost [0]
blended_coal_3 = sorted_blended_coal_properties_cost[best_combined_index]


# Properties definitions
blend_1_properties = sorted_predictions[0]
blend_2_properties = sorted_prediction_cost[0]
blend_3_properties = sorted_predictions[best_combined_index]

# Calculating costs on the spot
blend_1_cost = calculate_cost(blend_1, coal_costs)
blend_2_cost = sorted_total_cost[0]
blend_3_cost = calculate_cost(blend_3, coal_costs)

# Printing the blend values, properties, and calculated cost
print("Blend 1 (First in Sorted Blends):")
print("Blend Values in %:", blend_1)
print("Properties:", blend_1_properties,"\n")
print("Coal_Blend:", blended_coal_1, "\n")
print("Cost:", blend_1_cost, "\n")

print("Blend 2 (Lowest Cost):")
print("Blend Values in %:", blend_2)
print("Properties:", blend_2_properties)
print("Coal_Blend:", blended_coal_2, "\n")
print("Cost:", blend_2_cost, "\n")

print("Blend 3 (Best Combined):")
print("Blend Values:", blend_3)
print("Properties:", blend_3_properties)
print("Coal_Blend:", blended_coal_3, "\n")
print("Cost:", blend_3_cost, "\n")