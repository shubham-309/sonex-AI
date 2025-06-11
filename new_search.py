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

def search_in_directory(directory, categories, keyword):
    """Search for a keyword across all JSON files in a directory for specified categories."""
    results = {}
    
    for file_name in os.listdir(directory):
        if file_name.endswith(".json"):
            file_path = os.path.join(directory, file_name)
            data = load_json_data(file_path)
            
            for category in categories:
                if category in data:
                    category_results = search_in_category(data, category, keyword)
                    if category_results:
                        if file_name not in results:
                            results[file_name] = {}
                        results[file_name][category] = category_results

    return results

def save_results_to_file(results, save_path):
    """Save search results to a specified file."""
    try:
        with open(save_path, "w", encoding="utf-8") as file:
            json.dump(results, file, ensure_ascii=False, indent=4)
        st.success(f"Results saved to {save_path}")
    except Exception as e:
        st.error(f"An error occurred while saving the file: {e}")

def main():
    st.title("Enhanced Directory Search App")

    # Sidebar inputs
    st.sidebar.header("Search Configuration")
    directory = st.sidebar.text_input("Enter directory path", "./analytics")

    # Categories to search
    categories = [
        "Speakers",
        "Detailed_Summary",
        "Sentiment",
        "Keyword",
        "Insights",
        "Compliance",
        "Analytics",
    ]

    selected_categories = st.sidebar.multiselect("Select categories to search", categories, default=categories)

    keyword = st.sidebar.text_input("Enter keyword to search")

    if st.sidebar.button("Search"):
        if not os.path.exists(directory):
            st.error("The specified directory does not exist.")
        else:
            st.subheader("Search Results")
            results = search_in_directory(directory, selected_categories, keyword)

            if results:
                for file_name, file_results in results.items():
                    st.write(f"**File:** {file_name}")
                    for category, items in file_results.items():
                        st.write(f"  - **Category:** {category}")
                        for item in items:
                            st.write(f"    - {item}")
            else:
                st.warning("No results found.")

            # Option to save results
            save_path = st.text_input("Enter file path to save results", "./results.json")
            if st.button("Save Results"):
                save_results_to_file(results, save_path)

if __name__ == "__main__":
    main()
