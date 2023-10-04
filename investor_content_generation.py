class InvestorContentGeneration:
    def generate_personalized_content(self, investor_info):
        content = f"Hello {investor_info['name']},\n"
        content += f"We have a great investment opportunity for you. We are looking for an investment of {investor_info['total_raise_amount']}"
        return content

if __name__ == '__main__':
    investor_content_generation = InvestorContentGeneration()
    investor_info = {'name': 'John Doe', 'total_raise_amount': '1000000'}
    print(investor_content_generation.generate_personalized_content(investor_info))