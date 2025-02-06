import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.model_selection import train_test_split



# Define the D matrix
D= np.loadtxt('./coal_percentages/coal_percentages.csv', delimiter=',')
# Define the P matrix
P =  np.loadtxt('./Individual_coal_properties/Individual_coal_properties.csv', delimiter=',')
# coke_properties
Coke_properties = np.loadtxt('./Coke_properties/coke_properties.csv', delimiter=',')

Option = 1
# 1 -> Recovery top charge
# 2 -> Recovery Stamp Charge
# 3 -> Non-recovery Stamp Charge

Process_parameters =[]
if (Option ==1):
    Process_parameters = np.loadtxt('./Process_Parameter_data/Process_parameter_for_Rec_Top_Char.csv', delimiter=',')
elif (Option ==2):
    Process_parameters = np.loadtxt('./Process_Parameter_data/Process_parameter_for_Rec_Stam_Char.csv', delimiter=',')
elif (Option==3):
    Process_parameters = np.loadtxt('./Process_Parameter_data/Process_parameter_for_Non_Rec_Stam_Char.csv', delimiter=',')

B = np.dot(D, P)
B = B / 100
Blended_coal_parameters =  np.loadtxt('./Blended_Coal_data/blended_coal_data.csv', delimiter=',')
X_train, X_test, y_train, y_test = train_test_split(B, Blended_coal_parameters, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()

modelq = RandomForestRegressor(
    n_estimators=500,
    random_state=42,
)

modelq.fit(X_train, y_train)

y_pred = modelq.predict(X_test)
mse = np.mean((y_test - y_pred) ** 2)


if (Option==3):
    Process_parameters = np.pad(Process_parameters, ((0, 0), (0, 2)), mode='constant', constant_values=0)
Conv_matrix=Blended_coal_parameters+Process_parameters


X_train, X_test, y_train, y_test = train_test_split(Conv_matrix, Coke_properties, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()



X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


rf_model = RandomForestRegressor(n_estimators=100, random_state=42)


rf_model.fit(X_train, y_train)


y_pred = rf_model.predict(X_test)


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