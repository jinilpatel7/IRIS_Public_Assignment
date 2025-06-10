import pandas as pd
import os

def read_excel_tables(file_path: str) -> dict:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")

    df = pd.read_excel(file_path, None)  # Read all sheets
    tables = {}

    for sheet_name, sheet in df.items():
        rows, cols = sheet.shape
        table_name = None
        current_table = {}
        for i in range(rows):
            row = sheet.iloc[i].fillna("").astype(str)
            for j in range(cols):
                cell = row.iloc[j].strip()
                if cell.isupper() and len(cell) > 2 and " " in cell:
                    if table_name and current_table:
                        tables[table_name] = current_table
                        current_table = {}
                    table_name = cell
                elif table_name and row.iloc[0]:
                    key = row.iloc[0].strip()
                    values = pd.to_numeric(row.iloc[1:], errors="coerce").dropna().tolist()
                    current_table[key] = values
        if table_name and current_table:
            tables[table_name] = current_table
    return tables

def list_all_tables(parsed_data: dict) -> list:
    return list(parsed_data.keys())

def get_row_names(parsed_data: dict, table_name: str) -> list:
    table = parsed_data.get(table_name)
    if not table:
        raise ValueError(f"Table '{table_name}' not found.")
    return list(table.keys())

def get_row_sum(parsed_data: dict, table_name: str, row_name: str) -> float:
    table = parsed_data.get(table_name)
    if not table:
        raise ValueError(f"Table '{table_name}' not found.")
    row = table.get(row_name)
    if row is None:
        raise ValueError(f"Row '{row_name}' not found in table '{table_name}'.")
    return sum(row)
