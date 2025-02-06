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
    [16.92, 9.97, 0.76, 1205.54, 1281.45, 1178.54, 122.48, 99.57, 12.46, 73.34, 140.37, 80.7, 20.54, 1048.68, 4.99],
    [17.12, 10.08, 0.79, 1215.63, 1249.91, 1223.36, 122.58, 101.18, 12.79, 74.9, 140.52, 78.03, 20.14, 1059.19, 5.03],
    [16.83, 9.78, 0.76, 1191.42, 1288.62, 1194.38, 122.47, 99.1, 12.92, 73.45, 137.5, 80.22, 19.56, 1025.45, 5.04],
    [16.73, 10.29, 0.78, 1165.75, 1264.94, 1213.05, 123.25, 101.75, 12.7, 73.71, 136.65, 77.93, 20.23, 1030.28, 5.05],
    [16.93, 9.86, 0.78, 1177.12, 1224.8, 1187.04, 126.08, 100.34, 13.06, 72.94, 141.75, 79.19, 19.66, 1056.39, 5.1],
    [16.96, 10, 0.8, 1218.43, 1289.92, 1194.28, 127.38, 102.62, 12.87, 76.42, 138.62, 79.38, 19.82, 1080.65, 4.86],
    [17.46, 10.15, 0.76, 1218.57, 1231.85, 1219.67, 125.93, 98.22, 12.63, 74.53, 140.22, 80.84, 20.36, 1064.06, 4.92],
    [17.3, 10.15, 0.79, 1201.78, 1242.92, 1214.44, 125.1, 99.92, 12.85, 73.53, 140.92, 81.6, 19.69, 1037.42, 5.1],
    [17.38, 10, 0.78, 1203.68, 1289.66, 1212.22, 124.56, 101.95, 12.94, 73.5, 139.52, 80.37, 19.83, 1026.36, 4.93],
    [16.87, 9.79, 0.78, 1187.08, 1260.77, 1229.61, 125.44, 100.9, 12.64, 73.51, 139.45, 79.94, 19.82, 1025.68, 4.99],
    [16.59, 10.14, 0.77, 1170.7, 1218.44, 1232.55, 126.62, 97.83, 12.92, 74.15, 139.22, 82.33, 20.08, 1061.6, 5.11],
    [16.54, 10.04, 0.79, 1164.68, 1268.16, 1205.06, 126.73, 97.45, 12.56, 74, 140.45, 78.52, 19.74, 1067.53, 5.07],
    [16.98, 10.18, 0.79, 1204.57, 1218.51, 1247.24, 128.11, 100.67, 12.62, 76.56, 137.77, 77.99, 20.51, 1049.82, 4.96],
    [17.21, 9.81, 0.78, 1200.46, 1224.74, 1214.05, 122.26, 100.65, 12.97, 74.6, 140.7, 78.02, 20.01, 1019.46, 4.95],
    [16.65, 9.81, 0.78, 1231.9, 1262.77, 1216.79, 121.45, 98, 13.06, 75.52, 141.79, 81.56, 20.12, 1055.72, 4.88],
    [16.69, 10.23, 0.76, 1172.66, 1263.09, 1187.82, 126.45, 101.55, 13.02, 73.77, 140.47, 81.34, 19.54, 1071.95, 4.89],
    [17.39, 10.28, 0.77, 1216.42, 1265.51, 1210.24, 122.57, 100.74, 13.16, 72.78, 136.32, 81.8, 20.5, 1027.3, 4.96],
    [17.39, 9.72, 0.79, 1219.22, 1255.28, 1197.23, 124.67, 101.45, 12.59, 73.1, 135.8, 78.69, 20.26, 1050.07, 5.08],
    [16.97, 10.23, 0.78, 1177.43, 1224.53, 1185.88, 122.72, 102.62, 13.04, 76.87, 138.94, 80.9, 20.27, 1040.4, 5.06],
    [17.18, 9.93, 0.78, 1228.93, 1250.15, 1192.42, 127.89, 100.54, 13.01, 75.72, 139.33, 79.54, 19.86, 1028.6, 4.98],
    [17.31, 10.14, 0.77, 1189.61, 1261.31, 1249.18, 123.03, 100.1, 13.01, 76.63, 137.6, 79.12, 19.92, 1066.46, 5.08],
    [17.35, 10.19, 0.8, 1206.35, 1270.56, 1207.9, 126.69, 101.27, 12.79, 75.02, 140.27, 80.04, 20.11, 1026.33, 5.1],
    [16.89, 10, 0.77, 1179.32, 1280.46, 1225.35, 122.68, 101.14, 13.11, 75.1, 139.54, 78.74, 19.94, 1081.11, 5],
    [16.85, 10.02, 0.8, 1223.59, 1225.14, 1225.41, 122.43, 97.47, 12.72, 73.42, 142.45, 82.23, 20.28, 1068.32, 5.05],
    [17.31, 9.94, 0.76, 1214.73, 1222.43, 1223.56, 122.16, 100.6, 13.09, 72.76, 143.32, 77.88, 20.07, 1081.36, 4.9],
    [17.3, 9.8, 0.79, 1197.29, 1282.95, 1243.13, 121.6, 97.2, 12.88, 75.83, 136.83, 80.3, 19.93, 1020.12, 4.99],
    [16.59, 10, 0.76, 1163.92, 1245.96, 1206.76, 127.85, 97.28, 12.7, 74.76, 143.71, 78.01, 19.82, 1057.62, 4.86],
    [17.32, 9.76, 0.77, 1204.39, 1263.09, 1178.77, 125.48, 99.04, 12.97, 72.76, 139.53, 79.88, 20.29, 1056.89, 5.06],
    [16.73, 9.76, 0.79, 1201.58, 1272.11, 1230.79, 124.94, 98.23, 12.76, 73.51, 143.78, 78.46, 20.15, 1080.73, 5.14],
    [16.74, 10.27, 0.77, 1233.16, 1242.43, 1230.97, 128.07, 98.38, 13.02, 76.95, 142.48, 79, 20.28, 1077.96, 4.91],
    [16.95, 9.71, 0.8, 1185.98, 1275.65, 1181.36, 121.3, 102.14, 12.97, 75.71, 136.02, 78.24, 20.21, 1059.04, 5],
    [16.92, 9.96, 0.79, 1199.8, 1251.2, 1216.91, 127.48, 98.1, 12.56, 73.75, 143.8, 80.17, 19.49, 1060.92, 4.97],
    [17.01, 9.9, 0.76, 1231.28, 1225.06, 1221.7, 121.62, 100.82, 12.76, 76.05, 143.44, 78.98, 19.64, 1035.16, 4.98],
    [16.52, 10.08, 0.79, 1196.42, 1247.09, 1185.91, 125.86, 102.63, 12.99, 76.72, 136.43, 81.89, 19.42, 1034.46, 5.04],
    [17.22, 9.78, 0.77, 1202.38, 1276.35, 1195.54, 124.46, 97.24, 12.92, 74.76, 138.97, 80.16, 20.04, 1049.42, 4.95],
    [17.31, 10.18, 0.76, 1193.15, 1290.59, 1215.38, 127.62, 100.5, 12.73, 72.98, 142.66, 81.15, 19.53, 1031.85, 4.94],
    [16.5, 9.96, 0.79, 1208.75, 1248.21, 1241.44, 121.85, 100.26, 12.53, 77.17, 140.34, 79.61, 19.77, 1059.23, 4.95],
    [16.52, 9.85, 0.76, 1196.79, 1260.56, 1230.26, 126.37, 98.99, 12.75, 76.14, 136.6, 79.87, 20.32, 1067.72, 5.11],
    [17.07, 10.02, 0.77, 1202.17, 1247.86, 1246.33, 124.54, 100.76, 12.58, 75.54, 139.58, 79.16, 19.99, 1024.18, 5.04],
    [16.93, 9.9, 0.8, 1232.6, 1233.73, 1249.87, 128.5, 99.12, 12.65, 76.87, 141.96, 81.25, 19.71, 1057.45, 5.11],
    [16.94, 10.25, 0.8, 1201.5, 1287.38, 1185.08, 127.17, 97.14, 12.48, 76.62, 140.84, 81.61, 19.47, 1043.63, 5.03],
    [17.08, 10.1, 0.76, 1186.09, 1230.78, 1192.76, 126.74, 98.2, 12.82, 74.61, 141.97, 78.76, 19.85, 1068.91, 4.99],
    [16.72, 10.15, 0.76, 1185.53, 1217.82, 1206.88, 127.28, 97.51, 12.87, 75.53, 137.45, 81.27, 19.54, 1052.03, 4.98],
    [16.52, 10.04, 0.79, 1228.77, 1272.12, 1225.8, 121.94, 102.45, 12.47, 73.94, 140.56, 80.07, 20.44, 1040.21, 5.15],
    [17.49, 9.72, 0.77, 1195.63, 1274.97, 1218.35, 122.14, 102.41, 12.93, 74.06, 142.23, 79.27, 19.53, 1069.16, 4.89],
    [17.12, 10.22, 0.77, 1181.48, 1251.66, 1217.33, 122.86, 101.19, 13.2, 74.23, 139.31, 79.2, 20.19, 1080.01, 5.07],
    [16.68, 10.05, 0.77, 1232.88, 1278.42, 1240.78, 123.84, 98.85, 13.13, 74.21, 143.97, 81.01, 20.3, 1039.95, 4.85],
    [16.57, 9.94, 0.8, 1192.91, 1243.91, 1243.33, 126.36, 102.45, 12.71, 74.37, 138.22, 78.15, 19.98, 1037.04, 4.89],
    [16.49, 9.96, 0.77, 1201.76, 1230.23, 1228.05, 128.69, 100.65, 13.14, 74.95, 140.5, 77.85, 19.79, 1074.12, 4.86],
    [17.09, 10.12, 0.76, 1182.6, 1239.51, 1248.9, 127.38, 102.97, 12.94, 76.26, 136.5, 78.11, 19.69, 1067.85, 4.95],
    [16.69, 10.3, 0.79, 1180.91, 1276.16, 1204.04, 124.09, 98.86, 12.86, 73.15, 138.41, 81.93, 20.16, 1032.29, 4.87],
    [16.87, 9.75, 0.8, 1216.11, 1270.07, 1220.16, 124.75, 99.61, 12.59, 74.17, 136.38, 77.71, 19.62, 1059.03, 5.08]

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