class InvestorProfile:
    def collect_investor_information(self):
        investor_info = {}
        investor_info['name'] = input('Enter investor name: ')
        investor_info['total_raise_amount'] = input('Enter total raise amount (leave blank if undecided): ')
        return investor_info

if __name__ == '__main__':
    investor_profile = InvestorProfile()
    print(investor_profile.collect_investor_information())