import json


def write_order_to_json(item, quatity, price, buyer, date):
    dict_to_json = {"item": item, "quantity": quatity,
                    "price": price, "buyer": buyer, "date": date}

    with open('orders.json', 'w') as file:

        json.dump(dict_to_json, file, indent=4, ensure_ascii=False)


write_order_to_json("штаны", "1", "1200", "masha", "07.12.2022")
