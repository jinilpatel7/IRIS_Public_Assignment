from fastapi import APIRouter, Query, HTTPException
from src.parser import read_excel_tables, list_all_tables, get_row_names, get_row_sum

FILE_PATH = "Data/capbudg.xls"
parsed_data = read_excel_tables(FILE_PATH)

router = APIRouter()

@router.get("/list_tables")
def list_tables():
    try:
        tables = list_all_tables(parsed_data)
        return {"tables": tables}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_table_details")
def get_table_details(table_name: str = Query(...)):
    try:
        rows = get_row_names(parsed_data, table_name)
        return {"table_name": table_name, "row_names": rows}
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/row_sum")
def row_sum(table_name: str = Query(...), row_name: str = Query(...)):
    try:
        total = get_row_sum(parsed_data, table_name, row_name)
        return {"table": table_name, "row": row_name, "sum": total}
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
