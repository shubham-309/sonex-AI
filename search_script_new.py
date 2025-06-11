import streamlit as st
import json
import os
import re
from pathlib import Path

def load_json_data(json_file_path):
    """Load JSON data from a file."""
    try:
        with open(json_file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        st.error("Error decoding JSON. Please check the file format.")
        return {}

def search_in_category(data, category, keyword):
    """Search for a keyword in a selected category."""
    if category not in data:
        return []

    results = []
    category_data = data[category]

    # Handle different data types in the category
    if isinstance(category_data, str):
        if keyword.lower() in category_data.lower():
            results.append(category_data)
    elif isinstance(category_data, list):
        results.extend([item for item in category_data if keyword.lower() in str(item).lower()])
    elif isinstance(category_data, dict):
        for key, value in category_data.items():
            if keyword.lower() in str(value).lower():
                results.append({key: value})

    return results

def search_in_file_regex(filename, keyword):
    """Search for a keyword in a file using regex (case-insensitive, whole word match)."""
    results = []
    pattern = re.compile(r'\b{}\b'.format(re.escape(keyword)), re.IGNORECASE)  # Whole word, case insensitive
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if pattern.search(line):
                    results.append((line_number, line.strip()))  # Return line number and line content
    except FileNotFoundError:
        st.error(f"File not found: {filename}")
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")

    return results

def save_results_to_file(results, save_path):
    """Save search results to a specified file."""
    try:
        with open(save_path, "w", encoding="utf-8") as file:
            if isinstance(results, list):
                for item in results:
                    file.write(json.dumps(item, ensure_ascii=False) + "\n")
            else:
                file.write(json.dumps(results, ensure_ascii=False))
        st.success(f"Results saved to {save_path}")
    except Exception as e:
        st.error(f"An error occurred while saving the file: {e}")

def main():
    st.title("Enhanced Category Search App")

    # Directory containing JSON files (replace with your actual folder path)
    folder_path = "./analytics"  # Replace with the actual folder path

    # List all JSON files in the folder
    if not os.path.exists(folder_path):
        st.error("The folder does not exist! Please ensure the folder exists.")
        return

    files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

    if not files:
        st.warning("No JSON files found in the folder.")
        return

    # Allow user to select a file
    selected_file = st.selectbox("Select a JSON file", files)

    # Path to the selected JSON file
    json_file_path = os.path.join(folder_path, selected_file)

    # Load JSON data
    data = load_json_data(json_file_path)

    # Sidebar: Select category
    categories = list(data.keys())
    selected_category = st.sidebar.selectbox("Select a Category", categories)

    # Search bar
    keyword = st.text_input("Enter a keyword to search")

    # Display results
    if keyword:
        st.subheader(f"Results in '{selected_category}':")
        results = search_in_category(data, selected_category, keyword)

        if results:
            for result in results:
                st.write(result)
        else:
            st.warning("No results found.")

        # Option to save results
        if results:
            save_path = st.text_input("Enter file path to save results", "./results.json")
            if st.button("Save Results"):
                save_results_to_file(results, save_path)

    # Search in files (if applicable)
    if "files" in data:
        st.subheader("Search in Files")
        file_keyword = st.text_input("Enter a keyword to search in files")

        if file_keyword:
            file_results = []
            for file in data["files"]:
                file_path = Path(file['path'])  # Adjust based on your data structure
                matches = search_in_file_regex(file_path, file_keyword)
                if matches:
                    file_results.append({"file": file_path.name, "matches": matches})

            if file_results:
                for result in file_results:
                    st.write(f"**File:** {result['file']}")
                    for line_number, line in result['matches']:
                        st.write(f"Line {line_number}: {line}")

                # Option to save file results
                save_path = st.text_input("Enter file path to save file search results", "./file_results.json")
                if st.button("Save File Results"):
                    save_results_to_file(file_results, save_path)
            else:
                st.warning("No matches found in files.")

if __name__ == "__main__":
    main()
