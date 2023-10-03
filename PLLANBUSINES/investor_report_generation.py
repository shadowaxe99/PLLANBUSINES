class InvestorReportGeneration:
    def generate_customized_reports(self, investor_info, business_plan, financial_model):
        report = f'Business Plan Report for {investor_info["name"]}\n'
        report += f'Investment Amount: {investor_info["investment_amount"]}\n'
        report += f'Business Plan: {business_plan}\n'
        report += f'Financial Model: {financial_model}'
        return report