```python
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_section_content(prompt):
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=prompt,
        temperature=0.5,
        max_tokens=200
    )
    return response.choices[0].text.strip()

def generate_executive_summary(data):
    prompt = f"The company, {data['company_name']}, is a {data['industry']} company. Generate an executive summary."
    return generate_section_content(prompt)

def generate_company_description(data):
    prompt = f"The company, {data['company_name']}, was founded in {data['founding_year']} and is located in {data['location']}. Generate a company description."
    return generate_section_content(prompt)

def generate_market_analysis(data):
    prompt = f"The company, {data['company_name']}, operates in the {data['industry']} industry. Generate a market analysis."
    return generate_section_content(prompt)

def generate_competitive_analysis(data):
    prompt = f"The company, {data['company_name']}, has several competitors in the {data['industry']} industry. Generate a competitive analysis."
    return generate_section_content(prompt)

def generate_organization_management(data):
    prompt = f"The company, {data['company_name']}, has a team of {data['team_size']} people. Generate an organization and management description."
    return generate_section_content(prompt)

def generate_product_line_services(data):
    prompt = f"The company, {data['company_name']}, offers {data['products_services']}. Generate a description of the product line or services."
    return generate_section_content(prompt)

def generate_marketing_sales_strategy(data):
    prompt = f"The company, {data['company_name']}, plans to market its products/services through {data['marketing_channels']}. Generate a marketing and sales strategy."
    return generate_section_content(prompt)

def generate_funding_request(data):
    if data['funding_required']:
        prompt = f"The company, {data['company_name']}, is seeking {data['funding_amount']} in funding. Generate a funding request."
        return generate_section_content(prompt)
    else:
        return None

def generate_financial_projections(data):
    prompt = f"The company, {data['company_name']}, expects to achieve {data['financial_projections']} over the next five years. Generate financial projections."
    return generate_section_content(prompt)

def generate_appendix(data):
    prompt = f"The company, {data['company_name']}, has additional information to include in the appendix. Generate an appendix."
    return generate_section_content(prompt)
```