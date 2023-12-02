import pickle

import pandas as pd


def get_smt(name):
    with open(
            f'/Users/sergeybudygin/PycharmProjects/pythonProject1/project_of_car_prices/real_flask/utils/files/{name}.pickle',
            'rb') as f:
        return pickle.load(f)


def description_func(name):
    name = name.lower()
    if name in ['shape', 'size']:
        return f'{name}: {get_smt(name)}', False
    elif name == 'std':
        df = pd.read_csv(
            '/Users/sergeybudygin/PycharmProjects/pythonProject1/project_of_car_prices/real_flask/utils/files/std.csv')

        df = list(map(lambda x: x.split(), str(df).split('\n')))[1:]
        return df, True
    elif name in ['median', 'mean', 'max', 'min']:
        df = [['name', 'year', 'mileage', 'power', 'price'],
              ['median', '2012.000000', '45000.000000', '147.000000', '1.130000e+06'],
              ['mean', '2011.013801', '86251.180033', '157.507497', '1.780628e+06'],
              ['max', '2023.000000', '1000000.000000', '830.000000', '1.500000e+08'],
              ['min', '1936.000000', '0.000000', '1.000000', '2.700000e+02']]

        return [df[0], *list(filter(lambda x: x[0] == name, df))], True
    else:
        return "Choose from ['shape', 'std', 'size', 'median', 'mean', 'max', 'min']", False


print(description_func('std'))
