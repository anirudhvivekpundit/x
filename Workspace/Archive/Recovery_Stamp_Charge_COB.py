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
      [27.38, 10.3, 1.15, 1067.92, 1320.55, 1283.18, 225.34, 98.02, 20.57, 76.46, 185.06, 79.07, 26.14, 1018.84, 5.08],
    [26.39, 10.4, 1.15, 1124.59, 1358.13, 1254.71, 222.42, 102.3, 20.98, 74.01, 194.44, 80.38, 26.47, 999.16, 4.91],
    [27.19, 10.48, 1.14, 1096.96, 1389, 1310.37, 214.97, 100.37, 20.96, 74.29, 187.37, 79.71, 26.57, 1006.84, 5.06],
    [26.74, 10.71, 1.12, 1117.54, 1364.5, 1247.4, 219.71, 102.77, 20.64, 74.12, 189.35, 77.91, 26.32, 996.05, 5.03],
    [26.45, 10.43, 1.12, 1125.49, 1372.44, 1257.94, 213.5, 98.07, 21.1, 75.08, 188.64, 78.49, 25.99, 989.61, 5.04],
    [27.42, 10.58, 1.17, 1107.81, 1316.62, 1254.84, 217.84, 102.13, 21.31, 76.63, 192.13, 81.74, 26.61, 1015.56, 4.89],
    [27.34, 10.68, 1.13, 1118.87, 1376.18, 1257.21, 218.69, 101.94, 20.11, 75.59, 193.26, 80.87, 25.63, 985.71, 4.89],
    [26.39, 10.69, 1.12, 1098.89, 1344.53, 1296.48, 223.12, 100.22, 21.15, 76.93, 195.19, 79.25, 26.46, 982.7, 5],
    [27.24, 10.57, 1.17, 1101.25, 1351.05, 1269.6, 215.29, 100.19, 21.1, 75.56, 184.41, 80.05, 26.28, 992.68, 5],
    [26.68, 10.78, 1.14, 1099.66, 1339.5, 1245.57, 220.04, 101.97, 20.77, 74.55, 188.25, 82.31, 25.29, 1012.4, 5.05],
    [26.29, 10.69, 1.15, 1077.66, 1369, 1267.82, 219.11, 101.66, 20.29, 76.38, 192.48, 78.59, 25.89, 983.1, 4.94],
    [27.39, 10.32, 1.17, 1103.48, 1323.08, 1265.26, 217.24, 99.93, 20.65, 75.58, 189.76, 79.57, 25.87, 1005.15, 5.09],
    [27.52, 10.78, 1.15, 1106.46, 1389.62, 1290.91, 215.69, 98.53, 20.25, 74.77, 192.76, 81.29, 26.68, 1022.67, 5.01],
    [27.66, 10.75, 1.12, 1076.31, 1350.61, 1245.65, 218.34, 102.96, 20.5, 77.93, 194.78, 79.03, 26.04, 1023.33, 5.02],
    [26.44, 10.73, 1.18, 1072.86, 1363.88, 1274.76, 217.85, 97.47, 20.89, 76.3, 192.48, 81.57, 26.68, 1003.61, 5.08],
    [27.57, 10.55, 1.13, 1083.56, 1352.78, 1293.5, 221.23, 102.38, 20.43, 77.42, 194.31, 82.05, 25.28, 1023.19, 4.91],
    [26.8, 10.77, 1.12, 1088.03, 1350.65, 1288.54, 225.77, 101.8, 20.44, 75, 188.47, 81.24, 25.89, 981.74, 5.01],
    [26.9, 10.47, 1.18, 1085.7, 1387.61, 1305.47, 218.01, 99.03, 20.15, 75.69, 191, 78.02, 26.14, 1016.94, 4.88],
    [26.55, 10.63, 1.15, 1119.43, 1343.46, 1300.59, 222.18, 98.04, 20.28, 78.27, 185.19, 78.11, 25.64, 989.54, 4.93],
    [26.59, 10.5, 1.15, 1088.52, 1319.02, 1301.34, 215.58, 97.16, 20.32, 77.88, 187.03, 82.24, 26.33, 971.06, 5.06],
    [26.28, 10.56, 1.15, 1069.15, 1315.77, 1263.87, 225.03, 102.43, 20.22, 75.38, 188.5, 77.87, 25.73, 992.33, 5.03],
    [27.31, 10.53, 1.18, 1092.67, 1383.5, 1257.1, 225.23, 99.51, 20.89, 73.93, 184.62, 80.06, 26.63, 995.91, 5.04],
    [27.01, 10.38, 1.18, 1130.15, 1315.68, 1270.76, 223.83, 102.41, 20.34, 75.11, 192.1, 80.63, 25.29, 1021.18, 4.87],
    [26.81, 10.41, 1.14, 1120.73, 1387.34, 1301.68, 214.26, 97.15, 21.19, 77.11, 193.16, 81.42, 26.63, 1014.44, 4.91],
    [26.21, 10.32, 1.13, 1069.19, 1381.66, 1255.39, 220.25, 102.29, 20.39, 74.74, 194.84, 81.93, 26.62, 1022.82, 4.89],
     [26.82, 10.75, 1.16, 1117.62, 1339.39, 1241.9, 218.76, 99.07, 21.1, 74.47, 192.1, 80.87, 26.08, 1028.62, 5],
    [26.73, 10.43, 1.17, 1079.25, 1314.67, 1309.35, 224.37, 99.86, 20.39, 75.09, 193.93, 80.79, 26.37, 1003.15, 4.88],
    [26.43, 10.59, 1.12, 1127.93, 1341.28, 1288.03, 215.99, 102.09, 20.39, 77.65, 184.61, 78.34, 26.47, 1027.74, 4.99],
    [26.29, 10.46, 1.12, 1099.03, 1352.62, 1276.09, 224.94, 101.44, 20.92, 74.92, 189.14, 79.2, 25.33, 1010.09, 4.94],
    [26.67, 10.65, 1.18, 1096.92, 1343.45, 1254.17, 221.81, 99.63, 21.18, 77.03, 192.06, 81.8, 26.36, 1025.44, 4.95],
    [27.76, 10.29, 1.14, 1104.22, 1347.52, 1303.21, 221.26, 100.36, 21.28, 76.69, 194.16, 80.53, 26.67, 995.1, 4.96],
    [26.62, 10.39, 1.18, 1106.28, 1344.61, 1268.87, 223.63, 102, 20.96, 76.41, 188.14, 80.99, 26.31, 1020.45, 4.98],
    [26.91, 10.66, 1.16, 1071.26, 1366.45, 1300.79, 213.8, 102.53, 20.9, 75.54, 186.45, 79.48, 25.86, 1022.68, 5.02],
    [27.04, 10.79, 1.12, 1117.63, 1378.31, 1249.21, 218.58, 101.33, 21.28, 75.2, 195.26, 79.34, 25.27, 1013.71, 5.02],
    [26.37, 10.52, 1.16, 1120.75, 1382.17, 1306.85, 223.47, 99.39, 20.87, 77.27, 186.4, 80.06, 26.49, 994.85, 4.86],
    [26.57, 10.56, 1.16, 1124.14, 1362.61, 1274.37, 214.26, 101.34, 20.81, 76.45, 184.51, 81.19, 26.27, 982, 5],
    [27.41, 10.34, 1.17, 1115.5, 1338.39, 1263.41, 222.1, 98.52, 20.64, 77.73, 185.68, 78.13, 25.22, 970.08, 4.85],
    [26.3, 10.35, 1.12, 1100.07, 1374.08, 1265.71, 226.16, 99.33, 20.63, 75.23, 191.76, 80.13, 26.4, 1000.75, 5.15],
    [26.43, 10.3, 1.16, 1126.59, 1344.07, 1266.51, 214.08, 99.97, 21.14, 76.89, 190.42, 80.66, 25.29, 986.3, 5.08],
    [26.72, 10.72, 1.15, 1115.89, 1317.63, 1291.72, 222.33, 98.54, 21.28, 76.23, 186.01, 81.49, 25.73, 984.86, 4.94],
    [27.25, 10.71, 1.18, 1071.68, 1353.42, 1308.58, 215.21, 98.85, 20.62, 76.03, 194.54, 80.45, 26.77, 994.78, 4.99],
    [26.21, 10.29, 1.12, 1078.91, 1355.78, 1269.57, 216.65, 102.3, 21.11, 77.2, 188.38, 77.96, 25.71, 1008.88, 5.13],
    [26.77, 10.64, 1.15, 1068.99, 1326.32, 1302.78, 226.31, 99.72, 20.83, 77.56, 187.76, 77.64, 25.28, 1007.84, 4.93],
    [26.44, 10.45, 1.17, 1100.74, 1316.71, 1301.6, 220.99, 102.95, 20.86, 74.92, 186.22, 78.52, 25.85, 976.53, 5],
    [26.51, 10.49, 1.14, 1098.16, 1374.45, 1292.45, 221.87, 99.69, 20.65, 74.83, 194, 78.8, 26.07, 1026.26, 5.04],
    [27.3, 10.81, 1.12, 1078.29, 1388.09, 1248.19, 218.82, 102.12, 21.22, 74.51, 193.12, 81.27, 26.65, 999.49, 5.11],
    [27.32, 10.81, 1.16, 1068.22, 1375.53, 1271.78, 224.01, 98.56, 20.69, 75.14, 187.9, 82.13, 26.09, 979, 5],
    [26.71, 10.22, 1.17, 1083.48, 1367.06, 1255.72, 219.52, 102.44, 20.5, 77.62, 194.03, 80.46, 25.89, 995.44, 5.01],
    [26.51, 10.21, 1.16, 1116.73, 1348.74, 1243.28, 225.78, 100.7, 21.1, 76.54, 186.68, 79.24, 26.43, 970.38, 5],
    [27.44, 10.29, 1.12, 1072.1, 1331.16, 1314.42, 226.41, 97.88, 20.94, 76.68, 190.38, 81.9, 26.58, 1001.77, 4.96],
    [26.42, 10.4, 1.13, 1090.22, 1362.55, 1313.42, 219.95, 102.38, 21.26, 76.32, 190.52, 81.52, 25.65, 1011.72, 5.1],
    [26.84, 10.47, 1.13, 1110.08, 1356.57, 1292.75, 213.89, 98.96, 20.63, 76.05, 192.39, 80.33, 25.9, 1027.34, 5.09]
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