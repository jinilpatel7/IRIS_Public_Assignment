# FastAPI Excel Processor Assignment

## Overview

This project is a **FastAPI-based Excel Processing API** that reads an Excel sheet and exposes endpoints to:
- 🔍 List all detected tables in the file
- 📋 Retrieve row names from a specific table
- ➕ Compute the sum of all numerical values in a specific row of a selected table

---

## 📁 Directory Structure
```
IRIS_Public_Assignment/
├── app/
│ └── api.py # All FastAPI route definitions.
| └── main.py # Entry point - app setup, routers
├── src/
│ └── parser.py # Core logic to parse Excel files
├── Data/
│ └── capbudg.xls # Excel file to be processed
├── requirements.txt # Python dependencies
├── FastAPI_Excel_Processor.postman_collection.json
└── README.md # Project documentation
```
---

## 🚀 Features

✅ Supports `.xls`, `.xlsx`, and `.csv`  
✅ Automatically detects multiple tables in each sheet  
✅ API-first design, tested via Postman  
✅ Modular architecture

---

🌐 API Endpoints

### 1. `GET /list_tables`

**Functionality**:  
Lists all the table names extracted from the Excel sheet.

**Example Response**:
```json
{
  "tables": [
    "salvage_value",
    "operating_cashflows",
    "book_value_deprication",
    "cashflow_details",
    "initial_investment",
    "working_capital",
    "Growth_rate",
    "Discount_rate",
    "Investment_measure_2",
    "initial_investment2"
  ]
}
```

### 2. `GET /get_table_details?table_name=<table_name>`

**Functionality**: 
Returns the names of all rows in the first column for a given table.

**Example Request**:
http://127.0.0.1:9090/get_table_details?table_name=OPERATING%20CASHFLOWS

**Example Request**:
```
{
  "table_name": "OPERATING CASHFLOWS",
  "row_names": [
    "OPERATING CASHFLOWS",
    "Lifetime Index",
    "Revenues",
    "-Var. Expenses",
    "- Fixed Expenses",
    "EBITDA",
    "- Depreciation",
    "EBIT",
    "-Tax",
    "EBIT(1-t)",
    "+ Depreciation",
    "- ∂ Work. Cap",
    "NATCF",
    "Discount Factor",
    "Discounted CF"
  ]
}
```

### 3. ` GET /row_sum?table_name=<table_name>&row_name=<row_name> `
**Functionality**: 
Calculates and returns the sum of all numerical values in a given row.

**Example Request**:
http://localhost:9090/row_sum?table_name=INITIAL%20INVESTMENT&row_name=%2B%20Opp.%20Cost

**Example Request**:
```
{
  "table": "INITIAL INVESTMENT",
  "row": "+ Opp. Cost",
  "sum": 7484
}
```
---

## 🛠️ Setup Instructions

```
1. **Clone the repository**

   In bash
   git clone https://github.com/jinilpatel7/IRIS_Public_Assignment.git
   cd IRIS_Public_Assignment

2. **Create virtual environment & install dependencies**
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt

3. **Run the application**
   uvicorn app.main:app --reload --port 9090

```
