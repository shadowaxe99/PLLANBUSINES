class DataValidation:
    def validate_data(self, data):
        # Check if data is not empty
        if not data:
            return False
        # Check if data is a dictionary
        if not isinstance(data, dict):
            return False
        return True

if __name__ == '__main__':
    data_validation = DataValidation()
    data = {'product': 'AI Assistant Pro', 'market': 'Global', 'revenue': 2000000, 'expenses': 600000}
    print(data_validation.validate_data(data))

if __name__ == '__main__':
    data_validation = DataValidation()
    data = {'product': 'AI Assistant Pro', 'market': 'Global', 'revenue': 2000000, 'expenses': 600000}
    print(data_validation.validate_data(data))