# config.py

```python
# Database configuration
DB_CONFIG = {
    'database': 'business_plan_builder',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'port': '5432',  # default port for PostgreSQL, change as per your DBMS
}

# OpenAI API configuration
OPENAI_CONFIG = {
    'api_key': 'your_openai_api_key'
}

# Google Sheets API configuration
GSHEETS_CONFIG = {
    'credentials_file': 'path_to_your_credentials_file',
    'spreadsheet_id': 'your_spreadsheet_id'
}

# Microsoft Excel API configuration
EXCEL_CONFIG = {
    'credentials_file': 'path_to_your_credentials_file',
    'spreadsheet_id': 'your_spreadsheet_id'
}

# System-wide settings
SYSTEM_CONFIG = {
    'report_format': 'PDF',  # or 'DOCX', 'XLSX'
    'visualization_library': 'D3.js',  # or 'Chart.js'
    'feedback_tool': 'Typeform',  # or 'Google Forms'
}
```