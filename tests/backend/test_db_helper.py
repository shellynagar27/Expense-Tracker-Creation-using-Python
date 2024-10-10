# TDD -test driven development
from backend import db_helper

import os
import sys

print(__file__)

def test_fetch_expense_for_date_for_valid_date():
    expenses=db_helper.fetch_expense_for_date('2024-08-15')
    assert len(expenses)==1
    assert expenses[0]['amount']==10
    assert expenses[0]['category']=='Shopping'
    assert expenses[0]['notes']=='Bought potatoes'

def test_fetch_expense_for_date_for_invalid_date():
    expenses=db_helper.fetch_expense_for_date('2024-10-01')
    assert len(expenses)==0

def test_fetch_expense_summary_by_category_invalid_range():
    summary=db_helper.fetch_expense_summary("2099-01-01","2099-12-01")
    assert len(summary)==0

def test_fetch_expense_summary_by_month():
    data=db_helper.fetch_expense_summary_by_month()
    assert len(data)==2
