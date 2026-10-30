🧠 Advanced HR Performance Predictor - Fuzzy Logic System

📌 Project Overview

This project implements an Advanced Fuzzy Inference System (FIS) designed to evaluate and predict employee performance based on multiple variables. Moving beyond basic linear models, this system leverages Gaussian Membership Functions and complex logical rules (including the Fuzzy Complement/NOT operator) to mimic human-like decision-making and handle the inherent uncertainty in HR evaluations.

Built with an interactive Streamlit dashboard, the project features real-time predictions and a dynamic 3D Control Surface visualization that maps the non-linear relationships between inputs and the predicted output.

✨ Key Features

Non-Linear Reasoning: Utilizes skfuzzy.gaussmf (Gaussian curves) instead of basic triangular functions for smoother, more accurate transitions between linguistic variables.

Complex Rule Base: Implements sophisticated Fuzzy IF-THEN rules utilizing AND, OR, and the highly efficient NOT (~ Fuzzy Complement) operators.

Interactive UI: A fully responsive Streamlit dashboard allowing users to tweak crisp inputs via sliders and see real-time fuzzification/defuzzification results.

3D Visualization: Generates a dynamic 3D surface plot (matplotlib & mpl_toolkits.mplot3d) to visualize the inference engine's decision surface.

🏗️ System Architecture

The Fuzzy Logic System is built upon three main components:

1. Antecedents (Inputs)

Experience: (0 - 30 Years) ➔ [Junior, Mid-Level, Senior]

Training: (0 - 100 Hours) ➔ [Low, Medium, High]

Projects: (0 - 50 Projects) ➔ [Few, Average, Many]

2. Consequent (Output)

Performance Score: (0 - 100%) ➔ [Poor, Average, Excellent]

3. Inference Engine & Defuzzification

The system processes the crisp inputs through the rule base using minimum implication and maximum aggregation.

The final crisp output is calculated using the Centroid defuzzification method.

🚀 Installation & Usage

Prerequisites

Make sure you have Python 3.8+ installed on your machine.

Step 1: Clone the Repository

git clone https://github.com/YourUsername/Advanced-HR-Fuzzy-System.git
cd Advanced-HR-Fuzzy-System


Step 2: Install Dependencies

It is recommended to use a virtual environment.

pip install -r requirements.txt


(Dependencies: streamlit, scikit-fuzzy, numpy, matplotlib, networkx)

Step 3: Run the Dashboard

python -m streamlit run app.py


The dashboard will automatically open in your default web browser at http://localhost:8501.

📸 Dashboard Screenshots

(Placeholder for your amazing screenshots! Add an image of your Streamlit UI and the 3D Plot here)
<img width="1831" height="809" alt="Screenshot 2026-10-30 225831" src="https://github.com/user-attachments/assets/9ef69586-f2d1-405f-aa7b-14269ad3b859" />
<img width="1739" height="781" alt="Screenshot 2026-10-30 230137" src="https://github.com/user-attachments/assets/2c436c37-5303-4d31-8701-70036508a911" />


👨‍💻 Author

Mohamed Ayman Abdellatif Mahmoud

AI & Machine Learning Engineer

This project was developed as a comprehensive demonstration of Fuzzy Logic System Design for advanced AI applications.
