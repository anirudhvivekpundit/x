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
    [16.00, 0.93, 4.17, 0.78, 1.56, 18.64, 33.00, 24.25, 6.93, 92.47, 6.20, 4.33, 67.10, 25.10],
    [15.52, 0.85, 4.60, 0.78, 1.71, 19.08, 34.57, 22.63, 6.50, 92.47, 6.13, 4.40, 67.40, 23.90],
    [16.18, 0.90, 4.63, 0.78, 1.74, 19.37, 33.23, 22.70, 6.37, 92.33, 6.27, 4.40, 67.80, 24.00],
    [16.02, 0.97, 3.77, 0.78, 1.59, 18.95, 33.21, 22.98, 6.67, 92.40, 6.27, 4.33, 67.50, 24.10],
    [15.77, 0.90, 4.37, 0.78, 1.76, 18.41, 33.91, 23.94, 6.63, 92.96, 6.22, 3.82, 67.20, 23.40],
    [15.48, 0.97, 4.20, 0.78, 1.62, 18.86, 34.32, 23.31, 6.60, 92.74, 5.73, 4.53, 68.80, 22.00],
    [15.40, 0.90, 4.20, 0.78, 1.37, 18.99, 33.76, 24.48, 6.43, 92.60, 6.13, 4.27, 68.50, 23.30],
    [15.13, 0.92, 4.17, 0.78, 1.31, 19.58, 33.30, 25.10, 6.03, 92.80, 6.13, 4.07, 68.70, 22.10],
    [15.13, 0.95, 4.20, 0.78, 1.44, 19.49, 33.14, 24.37, 6.53, 92.87, 6.13, 4.00, 68.90, 23.10],
    [15.25, 0.88, 4.00, 0.71, 1.59, 19.33, 32.89, 23.62, 6.37, 92.67, 6.95, 4.38, 68.40, 22.60],
    [15.70, 0.97, 4.10, 0.78, 1.61, 16.47, 36.76, 25.95, 6.47, 92.60, 6.20, 4.20, 67.80, 24.00],
    [15.20, 0.90, 4.07, 0.78, 0.99, 17.94, 34.52, 24.72, 6.40, 92.67, 6.13, 4.20, 65.60, 23.40],
    [15.10, 0.90, 4.40, 0.78, 1.59, 18.96, 33.30, 23.35, 6.60, 93.00, 6.20, 3.80, 0.78, 0.78],
    [14.75, 0.83, 3.90, 0.78, 1.12, 17.56, 35.63, 24.15, 6.35, 92.50, 6.10, 4.40, 68.30, 23.00],
    [15.33, 0.93, 4.20, 0.78, 1.88, 18.48, 33.05, 24.82, 6.40, 92.53, 6.93, 4.53, 69.03, 22.39],
    [16.03, 0.95, 3.84, 1.00, 1.72, 18.90, 33.78, 23.07, 6.70, 92.50, 6.00, 4.50, 67.89, 25.14],
    [15.73, 0.98, 4.03, 0.78, 1.57, 20.23, 32.53, 23.42, 6.43, 92.80, 6.20, 4.00, 69.88, 22.44],
    [15.07, 0.90, 4.85, 0.78, 1.41, 19.46, 32.60, 23.80, 6.70, 92.40, 6.00, 4.60, 67.10, 23.60],
    [15.00, 1.00, 4.43, 1.20, 2.08, 18.29, 33.53, 24.30, 6.03, 92.60, 6.07, 4.33, 68.05, 24.06],
    [15.35, 0.88, 3.80, 0.85, 1.70, 17.97, 33.86, 24.66, 6.50, 92.07, 6.33, 4.60, 68.10, 24.43],
    [14.95, 0.98, 3.80, 0.91, 1.70, 19.02, 34.25, 23.17, 5.87, 92.80, 6.87, 4.33, 68.73, 24.22],
    [15.45, 1.00, 3.77, 1.39, 1.68, 19.65, 31.61, 24.28, 6.77, 92.60, 6.13, 4.27, 69.70, 23.30],
    [15.10, 1.04, 3.57, 0.88, 1.66, 18.54, 34.18, 23.76, 5.97, 92.67, 6.00, 4.33, 68.70, 23.60],
    [15.22, 1.00, 3.77, 0.78, 1.57, 18.64, 33.21, 24.00, 6.00, 92.60, 6.00, 4.40, 69.20, 23.80],
    [15.15, 1.08, 3.57, 0.78, 1.83, 19.42, 32.12, 23.92, 6.53, 92.60, 6.13, 4.27, 68.90, 23.40],
    [15.25, 0.97, 3.80, 0.78, 1.73, 19.19, 32.63, 23.52, 6.67, 92.47, 6.13, 4.40, 66.10, 26.50],
    [14.92, 1.08, 3.60, 0.78, 1.62, 18.91, 32.97, 24.27, 6.80, 92.40, 6.13, 4.47, 67.30, 24.30],
    [14.88, 0.98, 3.87, 0.78, 1.49, 18.71, 32.70, 23.71, 6.43, 92.47, 6.13, 4.40, 67.00, 23.00],
    [15.48, 0.97, 4.20, 0.78, 1.62, 18.86, 34.32, 23.31, 6.60, 92.74, 5.73, 4.53, 68.80, 22.00],
    [15.40, 0.90, 4.20, 0.78, 1.37, 18.99, 33.76, 24.48, 6.43, 92.60, 6.13, 4.27, 68.50, 23.30],
    [15.13, 0.92, 4.17, 0.78, 1.31, 19.58, 33.30, 25.10, 6.03, 92.80, 6.13, 4.07, 68.70, 22.10],
    [15.13, 0.95, 4.20, 0.78, 1.44, 19.49, 33.14, 24.37, 6.53, 92.87, 6.13, 4.00, 68.90, 23.10],
    [15.25, 0.88, 4.00, 0.71, 1.59, 19.33, 32.89, 23.62, 6.37, 92.67, 5.95, 4.38, 68.40, 22.60],
    [15.70, 0.97, 4.10, 0.78, 1.61, 16.47, 36.76, 25.95, 6.47, 92.60, 6.20, 4.20, 67.80, 24.00],
    [15.20, 0.90, 4.07, 0.78, 0.99, 17.94, 34.52, 24.72, 6.40, 92.67, 6.13, 4.20, 65.60, 23.40],
    [15.10, 0.90, 4.40, 0.78, 1.59, 18.96, 33.30, 23.35, 6.60, 93.00, 6.20, 3.80, 68.50, 23.30],
    [14.75, 0.83, 3.90, 0.78, 1.12, 17.56, 35.63, 24.15, 6.35, 92.50, 6.10, 4.40, 68.30, 23.00],
    [15.33, 0.93, 4.20, 0.78, 1.88, 18.48, 33.05, 24.82, 6.40, 92.53, 5.93, 4.53, 69.03, 22.39],
    [16.03, 0.95, 3.84, 1.00, 1.72, 18.90, 33.78, 23.07, 6.70, 92.50, 6.00, 4.50, 67.89, 25.14],
    [15.73, 0.98, 4.03, 0.78, 1.57, 20.23, 32.53, 23.42, 6.43, 92.80, 6.20, 4.00, 69.88, 22.44],
    [15.07, 0.90, 4.85, 0.78, 1.41, 19.46, 32.60, 23.80, 6.70, 92.40, 6.00, 4.60, 67.10, 23.60],
    [15.00, 1.00, 4.43, 1.20, 2.08, 18.29, 33.53, 24.30, 6.03, 92.60, 6.07, 4.33, 68.05, 24.06],
    [15.35, 0.88, 3.80, 0.85, 1.70, 17.97, 33.86, 24.66, 6.50, 92.07, 6.33, 4.60, 68.10, 24.43],
    [14.95, 0.98, 3.80, 0.91, 1.70, 19.02, 34.25, 23.17, 5.87, 92.80, 5.87, 4.33, 68.73, 24.22],
    [15.45, 1.00, 3.77, 1.39, 1.68, 19.65, 31.61, 24.28, 6.77, 92.60, 6.13, 4.27, 69.70, 23.30],
    [15.10, 1.04, 3.57, 0.88, 1.66, 18.54, 34.18, 23.76, 5.97, 92.67, 6.00, 4.33, 68.70, 23.60],
    [15.22, 1.00, 3.77, 0.78, 1.57, 18.64, 33.21, 24.00, 6.00, 92.60, 6.00, 4.40, 69.20, 23.80],
    [15.15, 1.08, 3.57, 0.78, 1.83, 19.42, 32.12, 23.92, 6.53, 92.60, 6.13, 4.27, 68.90, 23.40],
    [15.25, 0.97, 3.80, 0.78, 1.73, 19.19, 32.63, 23.52, 6.67, 92.47, 6.13, 4.40, 66.10, 26.50],
    [14.92, 1.08, 3.60, 0.78, 1.62, 18.91, 32.97, 24.27, 6.80, 92.40, 6.13, 4.47, 67.30, 24.30],
    [14.88, 0.98, 3.87, 0.78, 1.49, 18.71, 32.70, 23.71, 6.43, 92.47, 6.13, 4.40, 67.00, 23.00],
    [14.65, 0.95, 3.77, 0.78, 1.62, 19.29, 32.63, 24.13, 6.27, 92.67, 6.13, 4.20, 65.93, 23.42]

])


#crushing_size	percentage_of_moisture	bulk_density	blend_coal_quality_parameters	GCM_pressure	GCM_temperature	charging_temperature	Battery_operation_temp	coking_time	coke_end_temp	push_force	PRI	coke_per_push	volume_of_water	Quenching_time

import numpy as np

Process_parameters = np.array([
    [10.82, 10.75, 0.82, 46.56, 236.30, 312.80, 876.51, 32.46, 19.01, 1266.94, 17.19, 20.62, 14.38, 31.68, 2.55],
    [10.84, 10.77, 0.83, 46.54, 236.27, 312.81, 876.49, 32.45, 19.00, 1266.96, 17.20, 20.63, 14.39, 31.70, 2.56],
    [10.83, 10.74, 0.81, 46.53, 236.28, 312.79, 876.53, 32.48, 19.03, 1266.92, 17.16, 20.64, 14.40, 31.71, 2.57],
    [10.81, 10.76, 0.84, 46.55, 236.31, 312.83, 876.54, 32.47, 18.99, 1266.95, 17.17, 20.61, 14.37, 31.69, 2.58],
    [10.82, 10.75, 0.82, 46.57, 236.29, 312.82, 876.50, 32.49, 19.04, 1266.93, 17.18, 20.65, 14.38, 31.72, 2.55],
    [10.85, 10.78, 0.83, 46.54, 236.26, 312.84, 876.52, 32.46, 19.02, 1266.94, 17.15, 20.62, 14.41, 31.67, 2.59],
    [10.83, 10.75, 0.82, 46.58, 236.32, 312.81, 876.48, 32.47, 19.01, 1266.92, 17.19, 20.64, 14.39, 31.68, 2.54],
    [10.82, 10.74, 0.81, 46.55, 236.30, 312.82, 876.53, 32.48, 18.99, 1266.94, 17.16, 20.63, 14.37, 31.71, 2.58],
    [10.84, 10.76, 0.84, 46.56, 236.31, 312.80, 876.50, 32.49, 19.03, 1266.95, 17.17, 20.65, 14.41, 31.69, 2.56],
    [10.81, 10.77, 0.83, 46.57, 236.29, 312.83, 876.51, 32.46, 19.02, 1266.93, 17.18, 20.62, 14.38, 31.70, 2.55],
    [10.83, 10.75, 0.82, 46.55, 236.28, 312.81, 876.49, 32.48, 19.00, 1266.96, 17.20, 20.63, 14.39, 31.71, 2.57],
    [10.84, 10.74, 0.81, 46.53, 236.27, 312.80, 876.53, 32.47, 19.01, 1266.92, 17.15, 20.64, 14.38, 31.68, 2.59],
    [10.85, 10.76, 0.83, 46.54, 236.30, 312.84, 876.54, 32.46, 18.99, 1266.95, 17.16, 20.61, 14.37, 31.70, 2.58],
    [10.82, 10.78, 0.84, 46.57, 236.26, 312.83, 876.52, 32.49, 19.03, 1266.94, 17.17, 20.65, 14.41, 31.67, 2.56],
    [10.81, 10.75, 0.82, 46.56, 236.29, 312.82, 876.50, 32.48, 19.02, 1266.96, 17.18, 20.62, 14.39, 31.69, 2.55],
    [10.84, 10.77, 0.81, 46.55, 236.31, 312.80, 876.51, 32.46, 19.00, 1266.93, 17.15, 20.63, 14.38, 31.71, 2.57],
    [10.83, 10.76, 0.82, 46.53, 236.32, 312.79, 876.48, 32.47, 18.99, 1266.94, 17.16, 20.64, 14.37, 31.68, 2.59],
        [10.82, 10.75, 0.82, 46.56, 236.30, 312.80, 876.51, 32.46, 19.01, 1266.94, 17.19, 20.62, 14.38, 31.68, 2.55],
    [10.84, 10.77, 0.83, 46.54, 236.27, 312.81, 876.49, 32.45, 19.00, 1266.96, 17.20, 20.63, 14.39, 31.70, 2.56],
    [10.83, 10.74, 0.81, 46.53, 236.28, 312.79, 876.53, 32.48, 19.03, 1266.92, 17.16, 20.64, 14.40, 31.71, 2.57],
    [10.81, 10.76, 0.84, 46.55, 236.31, 312.83, 876.54, 32.47, 18.99, 1266.95, 17.17, 20.61, 14.37, 31.69, 2.58],
    [10.82, 10.75, 0.82, 46.57, 236.29, 312.82, 876.50, 32.49, 19.04, 1266.93, 17.18, 20.65, 14.38, 31.72, 2.55],
    [10.85, 10.78, 0.83, 46.54, 236.26, 312.84, 876.52, 32.46, 19.02, 1266.94, 17.15, 20.62, 14.41, 31.67, 2.59],
    [10.83, 10.75, 0.82, 46.58, 236.32, 312.81, 876.48, 32.47, 19.01, 1266.92, 17.19, 20.64, 14.39, 31.68, 2.54],
    [10.82, 10.74, 0.81, 46.55, 236.30, 312.82, 876.53, 32.48, 18.99, 1266.94, 17.16, 20.63, 14.37, 31.71, 2.58],
    [10.84, 10.76, 0.84, 46.56, 236.31, 312.80, 876.50, 32.49, 19.03, 1266.95, 17.17, 20.65, 14.41, 31.69, 2.56],
    [10.81, 10.77, 0.83, 46.57, 236.29, 312.83, 876.51, 32.46, 19.02, 1266.93, 17.18, 20.62, 14.38, 31.70, 2.55],
    [10.83, 10.75, 0.82, 46.55, 236.28, 312.81, 876.49, 32.48, 19.00, 1266.96, 17.20, 20.63, 14.39, 31.71, 2.57],
    [10.84, 10.74, 0.81, 46.53, 236.27, 312.80, 876.53, 32.47, 19.01, 1266.92, 17.15, 20.64, 14.38, 31.68, 2.59],
    [10.85, 10.76, 0.83, 46.54, 236.30, 312.84, 876.54, 32.46, 18.99, 1266.95, 17.16, 20.61, 14.37, 31.70, 2.58],
    [10.82, 10.78, 0.84, 46.57, 236.26, 312.83, 876.52, 32.49, 19.03, 1266.94, 17.17, 20.65, 14.41, 31.67, 2.56],
    [10.81, 10.75, 0.82, 46.56, 236.29, 312.82, 876.50, 32.48, 19.02, 1266.96, 17.18, 20.62, 14.39, 31.69, 2.55],
    [10.84, 10.77, 0.81, 46.55, 236.31, 312.80, 876.51, 32.46, 19.00, 1266.93, 17.15, 20.63, 14.38, 31.71, 2.57],
    [10.83, 10.76, 0.82, 46.53, 236.32, 312.79, 876.48, 32.47, 18.99, 1266.94, 17.16, 20.64, 14.37, 31.68, 2.59],
        [10.82, 10.75, 0.82, 46.56, 236.30, 312.80, 876.51, 32.46, 19.01, 1266.94, 17.19, 20.62, 14.38, 31.68, 2.55],
    [10.84, 10.77, 0.83, 46.54, 236.27, 312.81, 876.49, 32.45, 19.00, 1266.96, 17.20, 20.63, 14.39, 31.70, 2.56],
    [10.83, 10.74, 0.81, 46.53, 236.28, 312.79, 876.53, 32.48, 19.03, 1266.92, 17.16, 20.64, 14.40, 31.71, 2.57],
    [10.81, 10.76, 0.84, 46.55, 236.31, 312.83, 876.54, 32.47, 18.99, 1266.95, 17.17, 20.61, 14.37, 31.69, 2.58],
    [10.82, 10.75, 0.82, 46.57, 236.29, 312.82, 876.50, 32.49, 19.04, 1266.93, 17.18, 20.65, 14.38, 31.72, 2.55],
    [10.85, 10.78, 0.83, 46.54, 236.26, 312.84, 876.52, 32.46, 19.02, 1266.94, 17.15, 20.62, 14.41, 31.67, 2.59],
    [10.83, 10.75, 0.82, 46.58, 236.32, 312.81, 876.48, 32.47, 19.01, 1266.92, 17.19, 20.64, 14.39, 31.68, 2.54],
    [10.82, 10.74, 0.81, 46.55, 236.30, 312.82, 876.53, 32.48, 18.99, 1266.94, 17.16, 20.63, 14.37, 31.71, 2.58],
    [10.84, 10.76, 0.84, 46.56, 236.31, 312.80, 876.50, 32.49, 19.03, 1266.95, 17.17, 20.65, 14.41, 31.69, 2.56],
    [10.81, 10.77, 0.83, 46.57, 236.29, 312.83, 876.51, 32.46, 19.02, 1266.93, 17.18, 20.62, 14.38, 31.70, 2.55],
    [10.83, 10.75, 0.82, 46.55, 236.28, 312.81, 876.49, 32.48, 19.00, 1266.96, 17.20, 20.63, 14.39, 31.71, 2.57],
    [10.84, 10.74, 0.81, 46.53, 236.27, 312.80, 876.53, 32.47, 19.01, 1266.92, 17.15, 20.64, 14.38, 31.68, 2.59],
    [10.85, 10.76, 0.83, 46.54, 236.30, 312.84, 876.54, 32.46, 18.99, 1266.95, 17.16, 20.61, 14.37, 31.70, 2.58],
    [10.82, 10.78, 0.84, 46.57, 236.26, 312.83, 876.52, 32.49, 19.03, 1266.94, 17.17, 20.65, 14.41, 31.67, 2.56],
    [10.81, 10.75, 0.82, 46.56, 236.29, 312.82, 876.50, 32.48, 19.02, 1266.96, 17.18, 20.62, 14.39, 31.69, 2.55],
    [10.84, 10.77, 0.81, 46.55, 236.31, 312.80, 876.51, 32.46, 19.00, 1266.93, 17.15, 20.63, 14.38, 31.71, 2.57],
    [10.83, 10.76, 0.82, 46.53, 236.32, 312.79, 876.48, 32.47, 18.99, 1266.94, 17.16, 20.64, 14.37, 31.68, 2.59],
    [10.83, 10.76, 0.82, 46.53, 236.32, 312.79, 876.48, 32.47, 18.99, 1266.94, 17.16, 20.64, 14.37, 31.68, 2.59]
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
print(f"Mean Squared Error: {mse:.2f}")


import numpy as np

def calculate_ams(M_minus_10):

    target_min=93 
    target_max=95
    original_values= Coke_properties[:, 11]
    # Ensure original values are in a NumPy array
    original_values = np.array(original_values)
    
    # Min-Max scaling
    original_min = np.min(original_values)
    original_max = np.max(original_values)

    # Scale the input value
    ams_value = target_min + (M_minus_10 - original_min) * (target_max - target_min) / (original_max - original_min)

    # Return the rounded integer value
    return ams_value


Conv_matrix=Blended_coal_parameters+Process_parameters

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
X_train, X_test, y_train, y_test = train_test_split(Conv_matrix, Coke_properties, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()


# Fit the scaler on the training data and transform both training and test data
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from sklearn.ensemble import RandomForestRegressor

# Define the model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Predict on new data
y_pred = rf_model.predict(X_test)

# Evaluate the model
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")


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

blend1+=proces_para

coke = rf_model.predict(blend1)

# Create an array of AMS values for each row
AMS_values = np.array([calculate_ams(row[11]) for row in coke])

# Add the AMS values as a new column to the `coke` array
coke = np.column_stack((coke, AMS_values))


predictions=coke

blended_coal_properties=blend1


#Get all weightages for coke properties
ash_weightage = 1
vm_weightage = 1 #i think not needed 
m40_weightage = 1
m10_weightage = 1
csn_weightage = 1
cri_weightage = 1

#Get all min-max ranges for coke properties
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

# Corrected function to filter predictions and combinations along with blended coal properties
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
blended_coal_properties = valid_blended_coal_properties


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
    #diff.append(((prediction[<value here>] - desired_csr) / desired_csr) * csn_weightage)

    differences.append(diff)

# Calculate total differences and store in an array
total_differences = [sum(diff) for diff in differences]

# Sort the total differences (greatest first, lowest last) and get indices
sorted_indices = np.argsort(total_differences)[::-1]

# Sort predictions based on these indices
sorted_predictions = predictions[sorted_indices]
sorted_blends = all_combinations[sorted_indices]
# Sorting blended coal properties based on the sorted indices
sorted_blended_coal_properties = [blended_coal_properties[i] for i in sorted_indices]


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
print("Blend Values:", blend_1)
print("Properties:", blend_1_properties)
print("Cost:", blend_1_cost, "\n")

print("Blend 2 (Lowest Cost):")
print("Blend Values:", blend_2)
print("Properties:", blend_2_properties)
print("Cost:", blend_2_cost, "\n")

print("Blend 3 (Best Combined):")
print("Blend Values:", blend_3)
print("Properties:", blend_3_properties)
print("Cost:", blend_3_cost, "\n")

print(blended_coal_1)

print(blended_coal_2)

print(blended_coal_3)
