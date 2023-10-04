import pandas as pd

class DataIntegration:
    def incorporate_data(self, business_plan, financial_model, data):
        business_plan.update(data)
        financial_model.update(data)
        return business_plan, financial_model

if __name__ == '__main__':
    data_integration = DataIntegration()
    business_plan = {'product': 'AI Assistant', 'market': 'Global'}
    financial_model = {'revenue': 1000000, 'expenses': 500000}
    data = {'product': 'AI Assistant Pro', 'market': 'Global', 'revenue': 2000000, 'expenses': 600000}
    print(data_integration.incorporate_data(business_plan, financial_model, data))