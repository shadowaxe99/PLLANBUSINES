```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import financial_data

def compute_npv(rate, cash_flows):
    npv = 0
    for i in range(len(cash_flows)):
        npv += cash_flows[i] / (1 + rate)**(i+1)
    return npv

def compute_irr(cash_flows):
    rate = 0.1
    for i in range(1000):
        rate -= (compute_npv(rate, cash_flows) / (1 + rate))
    return rate

def compute_cash_flow_projections(revenue, expenses):
    return [r - e for r, e in zip(revenue, expenses)]

def push_to_spreadsheet(npv, irr, cash_flow_projections):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open('Financial Projections').sheet1

    sheet.update_cell(1, 1, 'NPV')
    sheet.update_cell(1, 2, npv)
    sheet.update_cell(2, 1, 'IRR')
    sheet.update_cell(2, 2, irr)
    sheet.update_cell(3, 1, 'Cash Flow Projections')
    for i, cash_flow in enumerate(cash_flow_projections, start=4):
        sheet.update_cell(i, 1, cash_flow)

def compute_financials():
    npv = compute_npv(financial_data['rate'], financial_data['cash_flows'])
    irr = compute_irr(financial_data['cash_flows'])
    cash_flow_projections = compute_cash_flow_projections(financial_data['revenue'], financial_data['expenses'])

    push_to_spreadsheet(npv, irr, cash_flow_projections)
```