import os
import pandas as pd

def load_excel_data(file_name):
    """Load Excel file and return structured data."""
    
    base_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "..", "data", file_name)

    print(f"Loading data from: {file_path}")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Excel file not found: {file_path}")

    # Ensure the correct file format is used
    df = pd.read_excel(file_path, engine='openpyxl')  # Explicitly specify the engine for .xlsx files

    df.columns = df.columns.str.lower()
    
    if "category" not in df.columns or "text" not in df.columns:
        raise ValueError("Expected columns 'category' and 'text' not found in the dataset.")

    return [{"category": row["category"], "text": row["text"]} for _, row in df.iterrows()]

# Call function with correct file extension
data = load_excel_data("bbc-text.xlsx")
print("Loaded Data Sample:", data[:3])
