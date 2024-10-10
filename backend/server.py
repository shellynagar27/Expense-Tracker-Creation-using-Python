from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

app=FastAPI()

class Expense(BaseModel):
    amount:float
    category:str
    notes:str

class DateRange(BaseModel):
    start_date:date
    end_date:date


@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date:date):
    expenses=db_helper.fetch_expense_for_date(expense_date)
    if expenses is None:
        raise HTTPException (status_code=500, detail="Failed to retrieve expense summary from the Database")
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date:date,expenses:List[Expense]):
    db_helper.delete_expense_for_date(expense_date)
    for expense in expenses:
        expenses=db_helper.insert_expense(expense_date,expense.amount,expense.category, expense.notes)
    return {"message": "Expense Updated successfully"}

@app.post("/analytics_by_category/")
def get_analytics_by_category(date_range: DateRange):
    data = db_helper.fetch_expense_summary_by_category(date_range.start_date,date_range.end_date)
    if data is None:
        raise HTTPException (status_code=500, detail="Failed to retrieve expense summary from the Database")
    
    # calculating total amount
    total=sum([row["total"] for row in data])

    breakdown={}

    # calculating percenatage share of each category in total expending
    for row in data:
        percentage=round((row["total"]/total)*100,2) if total!=0 else 0
        breakdown[row['category']]={
            "total":row['total'],
            "percentage":percentage
        }
    return breakdown
    
@app.get("/analytics_by_month/")
def get_analytics_by_month():
    data=db_helper.fetch_expense_summary_by_month()
    if data is None:
        raise HTTPException (status_code=500, detail="Failed to retrieve expense summary from the Database")
    
    # calculating total amount
    total=sum([row["total_expenditure"] for row in data])

    breakdown={}

    # calculating percenatage share of each category in total expending
    for row in data:
        percentage=round((row["total_expenditure"]/total)*100,2) if total!=0 else 0
        breakdown[row['month']]={
            "total_expenditure":row['total_expenditure'],
            "percentage":percentage
        }
    return breakdown


    
    