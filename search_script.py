import os
import shutil
import streamlit as st
from pathlib import Path

st.set_page_config("Advance Services", page_icon="logo/image.png", layout="wide")

col1, col2 = st.columns([1, 8])

with col1:
    st.image("logo/image.png", width=80)

with col2:
    st.title("Transcript Management and Search")

# Helper Functions
def copy_selected_files(selected_files, dest_folder):
    """Copy only selected files to the destination folder."""
    copied_files = []
    for file_path in selected_files:
        dest_file = Path(dest_folder) / file_path.name
        shutil.copy(file_path, dest_file)
        copied_files.append(dest_file)
    return copied_files

def search_keywords_in_file(file_path, keywords):
    """Search for keywords in a single file and return True if any are found."""
    with open(file_path, 'r', encoding="utf-8") as f:
        content = f.read()
        for keyword in keywords:
            if keyword.lower() in content.lower():
                return True
    return False

def filter_files_by_keywords(folder, keywords):
    """Filter files by keywords and return matching files."""
    matching_files = []
    for file in Path(folder).glob("*"):
        if file.is_file() and search_keywords_in_file(file, keywords):
            matching_files.append(file)
    return matching_files

def download_file(file_path):
    """Create a download link for a file."""
    with open(file_path, 'rb') as f:
        file_data = f.read()
    return file_data

# User inputs for input/output folders
input_folder = st.text_input("Enter Input Folder Path:", value="/home/shubham.pandey/Data Engineering/SonexAI Tool/transcripts")
output_folder = st.text_input("Enter Output Folder Path:", value="/home/shubham.pandey/Data Engineering/SonexAI Tool/dest")

# File Selection and Copying Section
st.header("File Copying")

# Display available files with checkboxes
files_in_input_folder = list(Path(input_folder).glob("*"))
selected_files = []
if files_in_input_folder:
    st.write("Select files to copy:")
    for file_path in files_in_input_folder:
        if file_path.is_file():
            if st.checkbox(file_path.name, key=file_path.name):
                selected_files.append(file_path)
else:
    st.write("No files found in the input folder.")

# Copy selected files to the destination folder
if st.button("Copy Selected Files to Destination"):
    if selected_files:
        copied_files = copy_selected_files(selected_files, output_folder)
        st.write(f"Copied {len(copied_files)} files to the destination folder.")
    else:
        st.write("Please select at least one file to copy.")

# Search Section
st.header("Keyword Search")

keywords_input = st.text_input("Enter keywords for search (comma-separated)")

# Perform Search
if st.button("Search"):
    if keywords_input:
        keywords = [k.strip() for k in keywords_input.split(",")]
        matching_files = filter_files_by_keywords(input_folder, keywords)

        if matching_files:
            st.write(f"Found {len(matching_files)} files matching the keywords:")
            for file in matching_files:
                st.write(file.name)
                st.download_button(label="Download", data=download_file(file), file_name=file.name)
        else:
            st.write("No files matched the search criteria.")
    else:
        st.write("Please enter at least one keyword for the search.")
