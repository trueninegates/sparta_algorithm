shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    set_menus = set(shop_menus)
    set_orders = set(shop_orders)

    if set_orders.intersection(set_menus) == set_orders:
        return True

    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)