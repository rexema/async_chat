import yaml

data = {
    1: [23, 345, 56],
    2: 20,
    3: {1: '4€',
        2: '6₽',

        }
}

with open('test.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False, allow_unicode=True)
