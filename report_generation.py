import matplotlib.pyplot as plt
from config import business_plan_data

def generate_report():
    sections = ['Executive Summary', 'Company Description', 'Market Analysis', 'Competitive Analysis', 'Organization & Management', 'Product Line or Services', 'Marketing & Sales Strategy', 'Funding Request', 'Financial Projections', 'Appendix']
    for section in sections:
        if section in business_plan_data:
            print(f"\n{section}:\n")
            print(business_plan_data[section])

def visualize_financials():
    financials = business_plan_data.get('Financial Projections', {})
    years = list(financials.keys())
    values = list(financials.values())

    plt.plot(years, values)
    plt.xlabel('Years')
    plt.ylabel('Projected Revenue')
    plt.title('Financial Projections')
    plt.show()

if __name__ == "__main__":
    generate_report()
    visualize_financials()