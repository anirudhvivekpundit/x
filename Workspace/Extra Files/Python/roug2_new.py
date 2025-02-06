import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import base64
import numpy as np
df = px.data.iris()

@st.cache_data 
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("image.jpg")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://w0.peakpx.com/wallpaper/384/363/HD-wallpaper-dark-blue-background-navy-blue.jpg");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

custom_css = """
<style>
body {
    color: whitesmoke;
    background-color: black; /* Example background color */
}

h1, h2, h3, h4, h5, h6, p, label, div, span {
    color: #dddddd !important;
    
}

button {
    background-color: #50C878 !important; /* Red background for buttons */
    color: white !important; /* White text color for buttons */
}
</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)
def normalize(matrix):
    mean = np.mean(matrix, axis=0)
    std_dev = np.std(matrix, axis=0)
    normalized_matrix = (matrix - mean) / std_dev
    return normalized_matrix, mean, std_dev

def denormalize(normalized_matrix, mean, std_dev):
    denormalized_matrix = (normalized_matrix * std_dev) + mean
    return denormalized_matrix

def calculate_matrices(D, P, R, K, regularization=1e-10):
    D_normalized, D_mean, D_std_dev = normalize(D)
    P_normalized, P_mean, P_std_dev = normalize(P)
    R_normalized, R_mean, R_std_dev = normalize(R)
    K_normalized, K_mean, K_std_dev = normalize(K)

    # Compute matrix C
    C = np.dot(D_normalized, np.dot(P_normalized, R_normalized))
    
    # Add regularization to the diagonal of C
    U, S, VT = np.linalg.svd(C, full_matrices=False)
    S = np.diag(S)
    S_inv = np.diag(1. / (S.diagonal() + regularization))
    C_pseudo_inv = np.dot(VT.T, np.dot(S_inv, U.T))
    
    # Compute the weight matrix W
    W = np.dot(C_pseudo_inv, K_normalized)
    
    # Verification
    verification = np.dot(np.dot(D_normalized, np.dot(P_normalized, R_normalized)), W)
    verification_denormalized = denormalize(verification, K_mean, K_std_dev)
    
    errors = []
    for i in range(len(verification_denormalized)):
        row_errors = []
        for j in range(len(verification_denormalized[0])):
            if K[i][j] != 0:
                error = round(abs((K[i][j] - verification_denormalized[i][j])) / K[i][j], 2)
                #  error = round(abs(K[i][j]-verification_denormalized[i][j]), 2)
            else:
                error = np.nan
            row_errors.append(error)
        errors.append(row_errors)
    
    errors = np.array(errors)
    
    return W, verification_denormalized, errors


def display_matrix(matrix, title):
    st.write(f"## {title}")
    st.dataframe(pd.DataFrame(matrix))

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = -3
if 'a' not in st.session_state:
    st.session_state.a = 0
if 'b' not in st.session_state:
    st.session_state.b = 0
if 'c' not in st.session_state:
    st.session_state.c = 0
if 'd' not in st.session_state:
    st.session_state.d = 0
if 'e' not in st.session_state:
    st.session_state.e = 0
if 'D' not in st.session_state:
    st.session_state.D = None
if 'P' not in st.session_state:
    st.session_state.P = None
if 'R' not in st.session_state:
    st.session_state.R = None
if 'K' not in st.session_state:
    st.session_state.K = None
if 'W' not in st.session_state:
    st.session_state.W = None
if 'verification_denormalized' not in st.session_state:
    st.session_state.verification_denormalized = None
if 'errors' not in st.session_state:
    st.session_state.errors = None

# Navigation
def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1
def curr_page():
    st.session_state.page+=0
# Page -1 (About this Digital Twin)
if st.session_state.page == -3:
    # st.markdown(custom_css_bn, unsafe_allow_html=True)
    st.title("About this Digital Twin")

    st.write("""
    <div style='font-size: 22px;'>
         Quality of coke plays a critical role in steel manufacturing plants, as a primary fuel and reducing agent.<br><br>
         Coke quality, in turn, is dependendent on various factors, including the input coal blend and process parameters.<br><br>
    </div>
    """, unsafe_allow_html=True)
    st.write("""
    <div style='font-size: 22px;'>
        This Software Platform is a Digital Twin of the Coal to Coke Manufacturing Process. <br><br>
             This innovative platform allows users to input specific coal blend compositions and process parameters,<br>
             to accurately predict the final properties of the coke output. <br><br>
             This Digital Twin enhances cost efficiency and also streamlines labor efforts, ensuring more reliable and consistent results in coke production.
    <br><br>
             </div>
    """, unsafe_allow_html=True)


    if st.button("Proceed"):
        next_page()  # Move to the next page
# Page 0
# Page 0
elif st.session_state.page == -2:
    st.title("Coke Quality Prediction using Matrix Inverse Approach")
    st.write("""
        <div style='font-size: 20px;'>
            Our Coke Quality Predictor uses advanced matrix computations and normalization techniques to deliver accurate predictions. Here is a brief detail of the approach.
            <br><br>
            1. <b>Normalization</b>: The <code>normalize</code> function standardizes each input matrix by calculating its mean and standard deviation. This transformation centers the data around a mean of 0 and scales it to have a standard deviation of 1. This step is crucial for ensuring consistent scaling and improving the accuracy of subsequent computations.
            <br><br>
            2. <b>Matrix Calculation</b>: In the <code>calculate_matrices</code> function, we normalize four matrices: D, P, R, and K. The matrix C is computed by multiplying the normalized matrices D, P, and R. This product represents the interaction between different factors affecting Coke quality.
            <br><br>
            3. <b>Weight Matrix using Inverse</b>: After multiplication of D, P, R matrices and taking pre-multiplication of the inverse of the resultant matrix, a weight matrix is obtained.
            <br><br>
            4. <b>Verification and Denormalization</b>: The model’s predictions are verified by comparing the computed values with the actual values in matrix K. The <code>denormalize</code> function is used to transform the normalized predictions back to their original scale. Errors are calculated as the absolute percentage difference between the actual and predicted values, providing insight into the model’s accuracy.
            <br><br>
            These steps ensure that our Coke Quality Predictor is robust, accurate, and reliable, leveraging sophisticated mathematical techniques to provide precise quality assessments.
        <br><br>
             </div>
        """, unsafe_allow_html=True)


    if st.button("Proceed"):
        next_page()  # Move to the next page
# Page 0
elif st.session_state.page == -1:
    st.title("Welcome to Coke Quality Predictor")
    
    st.subheader("Enter your details below:")
    name = st.text_input("Enter your Name*")
    id = st.text_input("Enter your ID")
    
    if st.button("Submit"):
        if not name or not id:
            st.error("Both Name and ID fields are required.")
        else:
            st.session_state.name = name
            st.session_state.id = id
            st.session_state.page = 0  # Move to the next page

# Page 1: Number of Sources and Select Sources
elif st.session_state.page == 0:
    st.title("Enter Number of Sources and select sources")
    
    b = st.number_input("Enter Number of Sources", min_value=1)
    st.write(""" Note : As this is the matrix approach, to ensure invertibility of matrices make sure that the number of properties of coal should be equal to number of process parameters""" )
    sources = ["KEDLA", "KATHARA", "BELATAND", "MADHUBAN", "CHASNALA", "PATHARDIH", "JHAMADOBA",
               "AUST. HARD", "AUST. LVHR", "USA HARD", "BENGA HARD", "APPIN HARD", "TUHUP HARD",
               "AUST. SOFT", "UAS SOFT", "RUSSIAN SOFT"]

    if 'dynamic_sources' not in st.session_state:
        st.session_state.dynamic_sources = sources

    if b:
        st.write("Select Sources:")
        col_sources = st.columns(4)
        selected_sources = []
        for i, source in enumerate(st.session_state.dynamic_sources):
            selected_sources.append(col_sources[i % 4].checkbox(source, key=f"source_checkbox_{i}"))

        new_source = st.text_input("Add New Source")
        if new_source and new_source not in st.session_state.dynamic_sources:
            st.session_state.dynamic_sources.append(new_source)
            st.experimental_rerun()

    if st.button("Next Page1"):
        st.session_state.b = b
        st.session_state.selected_sources = [k for k, v in zip(st.session_state.dynamic_sources, selected_sources) if v]
        next_page()

    if st.button("Previous Page1"):
        prev_page()

# Page 2: Number of Coal Properties and Select Properties
# Page 2: Number of Coal Properties and Select Properties
elif st.session_state.page == 1:
    st.title("Enter Number of Coal Properties and Select Properties")

    c = st.number_input("Enter Number of Coal Properties", min_value=1)

    properties = ["Ash", "VM", "Moisture", "FC", "Bulk Density", "Crushing index", "Crushing index (0.5 mm)",
                  "MMR", "Fluidity", "CSN / FSI", "Softening temperature", "Resolidification temperature",
                  "Sulpher", "Phosporous"]

    if 'dynamic_properties' not in st.session_state:
        st.session_state.dynamic_properties = properties

    if c:
        st.write("Select Properties:")
        col_props = st.columns(4)
        selected_properties = []
        for i, prop in enumerate(st.session_state.dynamic_properties):
            selected_properties.append(col_props[i % 4].checkbox(prop, key=f"prop_checkbox_{i}"))

        new_property = st.text_input("Add New Property")
        if new_property and new_property not in st.session_state.dynamic_properties:
            st.session_state.dynamic_properties.append(new_property)
            st.experimental_rerun()

    if sum(selected_properties) > c:
        st.error(f"You can select up to {c} properties only.")

    if st.button("Next Page2"):
        st.session_state.c = c
        st.session_state.a = c
        st.session_state.selected_properties = [k for k, v in zip(st.session_state.dynamic_properties, selected_properties) if v]
        next_page()

    if st.button("Previous Page2"):
        prev_page()

# Page 3: Number of Coal Process Parameters and Select Parameters
elif st.session_state.page == 2:
    st.title("Enter Number of Coal Process Parameters and Select Parameters")

    d = st.number_input("Enter Number of Coal Process Parameters", min_value=1)

    process_parameters = ["Charging tonnage (Dry)", "Moisture content", "Bulk Density of charging coal",
                          "Average Charging temperature (P/S)", "Average Charging temperature (C/S)",
                          "Coke Mass Temperature in degC", "Cross wall temperature", "Push Force / Pushing Current (Min)",
                          "Push Force / Pushing Current (Max)", "PRI ( Pushing regularity Index)", "Coke per push in dry basis",
                          "Gross coke Yield", "GCM Pressure", "GCM Temperature", "Coking time", "Coke end temperature",
                          "Quenching time", "Quenching water volume", "GCV of mixed gas", "GCV of BF Gas",
                          "Underfiring CO Gas Qty / day", "Underfiring BF Gas Qty / day"]

    if 'dynamic_process_parameters' not in st.session_state:
        st.session_state.dynamic_process_parameters = process_parameters

    if d:
        st.write("Select Process Parameters:")
        col_params = st.columns(4)
        selected_process_parameters = []
        for i, param in enumerate(st.session_state.dynamic_process_parameters):
            selected_process_parameters.append(col_params[i % 4].checkbox(param, key=f"param_checkbox_{i}"))

        new_parameter = st.text_input("Add New Parameter")
        if new_parameter and new_parameter not in st.session_state.dynamic_process_parameters:
            st.session_state.dynamic_process_parameters.append(new_parameter)
            st.experimental_rerun()

    if sum(selected_process_parameters) > d:
        st.error(f"You can select up to {d} process parameters only.")

    if st.button("Next Page3"):
        st.session_state.d = d
        st.session_state.selected_process_parameters = [k for k, v in zip(st.session_state.dynamic_process_parameters, selected_process_parameters) if v]
        next_page()

    if st.button("Previous Page3"):
        prev_page()

# Page 4: Number of Output Coke Properties and Select Properties
elif st.session_state.page == 3:
    st.title("Enter Number of Output Coke Properties and Select Properties")

    e = st.number_input("Enter Number of Output Coke Properties", min_value=1)

    output_coke_properties = ["Ash", "VM", "Moisture", "FC", "AMS", "<25 mm", ">80mm", "CSR", "CRI", "M40", "M10", "S", "P"]

    if 'dynamic_output_coke_properties' not in st.session_state:
        st.session_state.dynamic_output_coke_properties = output_coke_properties

    if e:
        st.write("Select Output Coke Properties:")
        col_output_props = st.columns(4)
        selected_output_coke_properties = []
        for i, prop in enumerate(st.session_state.dynamic_output_coke_properties):
            selected_output_coke_properties.append(col_output_props[i % 4].checkbox(prop, key=f"output_prop_checkbox_{i}"))

        new_output_property = st.text_input("Add New Output Coke Property")
        if new_output_property and new_output_property not in st.session_state.dynamic_output_coke_properties:
            st.session_state.dynamic_output_coke_properties.append(new_output_property)
            st.experimental_rerun()

    if sum(selected_output_coke_properties) > e:
        st.error(f"You can select up to {e} output coke properties only.")

    if st.button("Next Page4"):
        st.session_state.e = e
        st.session_state.selected_output_coke_properties = [k for k, v in zip(st.session_state.dynamic_output_coke_properties, selected_output_coke_properties) if v]
        next_page()

    if st.button("Previous Page4"):
        prev_page()

# Continue with the rest of the pages
elif st.session_state.page == 4:
    st.write(f"""
        <div style='font-size: 50px;'>
            Data Requirement for Model Working
             <br>
        </div>
    """, unsafe_allow_html=True)
    st.write(f"""
        <div style='font-size: 20px;'>
            On the basis of your chosen parameters of processes and properties, the model requires {st.session_state.a} days of data for the given parameters.
            <br><br>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Proceed Next"):
        next_page()

# Page 5: Input Coal Percentages Matrix (D)
elif st.session_state.page == 5:
    st.title("Enter Percentages of Input Coal from Different Sources")
    
    D = np.zeros((st.session_state.a, st.session_state.b))
    for i in range(st.session_state.a):
        cols = st.columns(st.session_state.b + 1)  # Create columns for inputs + day label
        cols[0].write(f"Day {i+1}")
        for j in range(st.session_state.b):
            D[i, j] = cols[j + 1].number_input(f"{st.session_state.selected_sources[j]}", min_value=0.0, step=0.01, key=f"D_{i}_{j}")

    if st.button("Previous Page5"):
        st.session_state.D = D
        prev_page()
    if st.button("Next Page5"):
        st.session_state.D = D
        next_page()

# Page 6: Input Coal Properties Matrix (P)
elif st.session_state.page == 6:
    st.title("Enter Properties of Individual Coal from Different Sources")
    
    P = np.zeros((st.session_state.b, st.session_state.c))
    for i in range(st.session_state.b):
        cols = st.columns(st.session_state.c + 1)  # Create columns for inputs + source label
        cols[0].write(st.session_state.selected_sources[i])
        for j in range(st.session_state.c):
            P[i, j] = cols[j + 1].number_input(f"{st.session_state.selected_properties[j]}", min_value=0.0, step=0.01, key=f"P_{i}_{j}")

    if st.button("Previous Page6"):
        st.session_state.P = P
        prev_page()
    if st.button("Next Page6"):
        st.session_state.P = P
        next_page()

# Page 7: Input Process Parameters Matrix (R)
elif st.session_state.page == 7:
    st.title("Enter Process Parameters")
    
    R = np.zeros((st.session_state.a, st.session_state.d))
    for i in range(st.session_state.a):
        cols = st.columns(st.session_state.d + 1)  # Create columns for inputs + day label
        cols[0].write(f"Day {i+1}")
        for j in range(st.session_state.d):
            R[i, j] = cols[j + 1].number_input(f"{st.session_state.selected_process_parameters[j]}", min_value=0.0, step=0.01, key=f"R_{i}_{j}")

    if st.button("Previous Page7"):
        st.session_state.R = R
        prev_page()
    if st.button("Next Page7"):
        st.session_state.R = R
        next_page()

# Page 8: Input Coke Properties Matrix (K)
elif st.session_state.page == 8:
    st.title("Enter Properties of Output Coke")

    K = np.zeros((st.session_state.a, st.session_state.e))
    for i in range(st.session_state.a):
        cols = st.columns(st.session_state.e + 1)  # Create columns for inputs + day label
        cols[0].write(f"Day {i+1}")
        for j in range(st.session_state.e):
            K[i, j] = cols[j + 1].number_input(f"{st.session_state.selected_output_coke_properties[j]}", min_value=0.0, step=0.01, key=f"K_{i}_{j}")

    if st.button("Previous Page8"):
        st.session_state.K = K
        prev_page()
    if st.button("Next Page8"):
        st.session_state.K = K
        next_page()

# Page 9: Calculate Mat
# elif st.session_state.page == 8:
#     next_page()
# Page 6: Calculate Matrices and Show Results
elif st.session_state.page == 9:
    st.title("Calculation and Results")

    D = st.session_state.D
    P = st.session_state.P
    R = st.session_state.R
    K = st.session_state.K

    if D is None or P is None or R is None or K is None:
        st.error("One of the matrices is not initialized. Please check your inputs.")
    else:
        W, verification_denormalized, errors = calculate_matrices(D, P, R, K)

        st.session_state.W = W
        st.session_state.verification_denormalized = verification_denormalized
        st.session_state.errors = errors

    if st.button("Previous Page6"):
        
        curr_page()
    if st.button("Show Results"):
        
        next_page()

# Page 7: Display Weight Matrix
elif st.session_state.page == 10:
    st.title("Weight Matrix")
    display_matrix(st.session_state.W, "Weight Matrix")

    if st.button("Previous page7"):
        
        prev_page()
    if st.button("Next page7"):
        
        next_page()

# Page 8: Display Verification Results
elif st.session_state.page == 11:
    st.title("Verification Results")
    display_matrix(st.session_state.verification_denormalized, "Verification Results")

    if st.button("Previous Page8"):
        
        prev_page()
    if st.button("Next Page8"):
        
        next_page()

# Page 9: Display Error Matrix
elif st.session_state.page == 12:
    st.title("Error Matrix")
    display_matrix(st.session_state.errors, "Error Matrix")

    if st.button("Previous page9"):
        
        prev_page()
    if st.button("Next page9"):
        
        next_page()

# Page 10: Thank You
elif st.session_state.page == 13:
    st.title("Thank You")
    st.write("Thank you for using the application!")

    if st.button("Previous Page10"):
        prev_page()
