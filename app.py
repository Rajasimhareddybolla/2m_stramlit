import streamlit as st
import pandas as pd
import os

# Set the folder containing CSV files
DATA_FOLDER = "school_data_csv"

# Title of the App
st.title("School Data Viewer")

# Sidebar for selecting a file
st.sidebar.header("Select a CSV File")
csv_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith('.csv')]

# Check if there are any CSV files in the folder
if len(csv_files) == 0:
    st.error("No CSV files found in the 'school-data' folder.")
else:
    # Dropdown menu for selecting a file
    selected_file = st.sidebar.selectbox("Available Files", csv_files)

    # Load and display the selected file
    if selected_file:
        file_path = os.path.join(DATA_FOLDER, selected_file)

        try:
            # Read CSV
            df = pd.read_csv(file_path)

            # Show file name and shape
            st.subheader(f"File: {selected_file}")
            st.write(f"**Rows:** {df.shape[0]} | **Columns:** {df.shape[1]}")

            # Preview the top rows
            st.subheader("Data Preview")
            st.write(df.head())

            # Optional: Allow the user to choose columns for visualization
            st.subheader("Data Visualization")
            columns = df.columns.tolist()

            if len(columns) >= 2:
                x_col = st.selectbox("Select X-axis", columns, index=0)
                y_col = st.selectbox("Select Y-axis", columns, index=1)

                # Display chart
                st.bar_chart(df[[x_col, y_col]].dropna())
            else:
                st.warning("Not enough columns for visualization.")
        except Exception as e:
            st.error(f"Error loading file: {e}")
