# Part 1: Imports and UI Setup
import streamlit as st
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Configure the Streamlit page layout
st.set_page_config(page_title="Advanced Fuzzy System", layout="wide")

# Part 2: Core Fuzzy System Logic (Cached for performance)
@st.cache_resource
def build_fuzzy_system():
    # 1. Variables
    experience = ctrl.Antecedent(np.arange(0, 31, 1), 'experience')
    training = ctrl.Antecedent(np.arange(0, 101, 1), 'training')
    projects = ctrl.Antecedent(np.arange(0, 51, 1), 'projects')
    performance = ctrl.Consequent(np.arange(0, 101, 1), 'performance')

    # 2. Gaussian Membership Functions
    experience['junior'] = fuzz.gaussmf(experience.universe, 0, 4)
    experience['mid_level'] = fuzz.gaussmf(experience.universe, 10, 4)
    experience['senior'] = fuzz.gaussmf(experience.universe, 25, 5)

    training['low'] = fuzz.gaussmf(training.universe, 0, 15)
    training['medium'] = fuzz.gaussmf(training.universe, 50, 15)
    training['high'] = fuzz.gaussmf(training.universe, 100, 15)

    projects['few'] = fuzz.gaussmf(projects.universe, 0, 8)
    projects['average'] = fuzz.gaussmf(projects.universe, 20, 8)
    projects['many'] = fuzz.gaussmf(projects.universe, 45, 8)

    performance['poor'] = fuzz.gaussmf(performance.universe, 0, 15)
    performance['average'] = fuzz.gaussmf(performance.universe, 50, 15)
    performance['excellent'] = fuzz.gaussmf(performance.universe, 100, 15)

    # 3. Fuzzy Rules
    rule1 = ctrl.Rule(experience['junior'] & training['low'] & projects['few'], performance['poor'])
    rule2 = ctrl.Rule(experience['junior'] & training['high'], performance['average'])
    rule3 = ctrl.Rule(experience['mid_level'] & training['medium'], performance['average'])
    rule4 = ctrl.Rule(experience['senior'] & training['high'] & projects['many'], performance['excellent'])
    
    # 4. Control System
    perf_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
    return ctrl.ControlSystemSimulation(perf_ctrl)

# Initialize the system
fuzzy_sim = build_fuzzy_system()

# Part 3: Dashboard UI - Sidebar Inputs
st.title("🧠 Advanced HR Performance Fuzzy System")
st.markdown("**Developed by: Mohamed Ayman Abdellatif Mahmoud | AI Engineer**")

st.sidebar.header("🎛️ Employee Data Inputs")
st.sidebar.markdown("Adjust the sliders to see real-time fuzzy predictions.")

# Sliders for Crisp Inputs
input_exp = st.sidebar.slider("Experience (Years)", 0, 30, 12)
input_train = st.sidebar.slider("Training (Hours)", 0, 100, 80)
input_proj = st.sidebar.slider("Projects Completed", 0, 50, 35)

# Pass inputs to Fuzzy Engine
fuzzy_sim.input['experience'] = input_exp
fuzzy_sim.input['training'] = input_train
fuzzy_sim.input['projects'] = input_proj

# Compute the Result
fuzzy_sim.compute()
final_score = fuzzy_sim.output['performance']

# Display Metrics
st.markdown("### 📊 Prediction Results")
col1, col2 = st.columns(2)
col1.metric(label="Predicted Performance Score", value=f"{final_score:.2f}%")

# Part 4: 3D Visualization of the Fuzzy Logic Surface
st.markdown("---")
st.markdown("### 🌐 3D Control Surface")
st.markdown("Mapping Experience and Training against Performance Score (Projects kept constant).")

# Generate grid data
x_val, y_val = np.meshgrid(np.linspace(0, 30, 20), np.linspace(0, 100, 20))
z_val = np.zeros_like(x_val)

# Compute Z values
for i in range(20):
    for j in range(20):
        fuzzy_sim.input['experience'] = x_val[i, j]
        fuzzy_sim.input['training'] = y_val[i, j]
        fuzzy_sim.input['projects'] = input_proj  # Dynamic constant from slider
        fuzzy_sim.compute()
        z_val[i, j] = fuzzy_sim.output['performance']

# Plot 3D Surface
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x_val, y_val, z_val, cmap='plasma', edgecolor='none')

ax.set_xlabel('Experience (Years)', fontweight='bold')
ax.set_ylabel('Training (Hours)', fontweight='bold')
ax.set_zlabel('Performance Score', fontweight='bold')
fig.colorbar(surf, shrink=0.5, aspect=5)

# Render plot in Streamlit
st.pyplot(fig)