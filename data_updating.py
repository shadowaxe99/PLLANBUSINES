import pandas as pd

class DataUpdating:
    def update_data(self, data, new_data):
        df = pd.DataFrame(data)
        df.update(new_data)
        return df.to_dict()

if __name__ == '__main__':
    data_updating = DataUpdating()
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    new_data = {'A': [7, 8, 9], 'B': [10, 11, 12]}
    print(data_updating.update_data(data, new_data))