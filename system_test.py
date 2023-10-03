import unittest
from main import Main
from data_collection import DataCollection
from ai_integration import AIIntegration
from financial_computation import FinancialComputation
from report_generation import ReportGeneration

class TestSystem(unittest.TestCase):

    def setUp(self):
        self.main = Main()
        self.data_collection = DataCollection()
        self.ai_integration = AIIntegration()
        self.financial_computation = FinancialComputation()
        self.report_generation = ReportGeneration()

    def test_data_collection(self):
        data = self.data_collection.collect_data()
        self.assertIsNotNone(data, "Data collection failed.")

    def test_ai_integration(self):
        content = self.ai_integration.generate_content("Test prompt")
        self.assertIsNotNone(content, "AI content generation failed.")

    def test_financial_computation(self):
        financials = self.financial_computation.compute_financials({"revenue": 1000, "expenses": 500})
        self.assertIsNotNone(financials, "Financial computation failed.")

    def test_report_generation(self):
        report = self.report_generation.generate_report({"section1": "content1", "section2": "content2"})
        self.assertIsNotNone(report, "Report generation failed.")

    def test_main_workflow(self):
        result = self.main.run()
        self.assertTrue(result, "Main workflow failed.")

if __name__ == '__main__':
    unittest.main()