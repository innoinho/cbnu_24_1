from durable.lang import *

with ruleset('inventory_management'):
    # 재고 수준이 낮을 때 알림
    @when_all(m.quantity < 10)
    def low_stock(c):
        c.post({'type': 'alert', 'message': 'Low stock for item {}'.format(c.m.item_id)})

    # 재고가 없을 때 알림
    @when_all(m.quantity == 0)
    def out_of_stock(c):
        c.post({'type': 'alert', 'message': 'Out of stock for item {}'.format(c.m.item_id)})

    # 재고가 충분할 때 알림
    @when_all(m.quantity >= 50)
    def stock_sufficient(c):
        c.post({'type': 'info', 'message': 'Sufficient stock for item {}'.format(c.m.item_id)})

    # 새로운 재고가 추가될 때
    @when_all(m.action == 'add')
    def add_stock(c):
        # 재고 추가 로직
        print('Added {} units to item {}'.format(c.m.quantity, c.m.item_id))

    # 재고가 판매될 때
    @when_all(m.action == 'sell')
    def sell_stock(c):
        # 재고 판매 로직
        print('Sold {} units of item {}'.format(c.m.quantity, c.m.item_id))

    # 재고가 반환될 때
    @when_all(m.action == 'return')
    def return_stock(c):
        # 재고 반환 로직
        print('Returned {} units of item {}'.format(c.m.quantity, c.m.item_id))

    # ... 나머지 규칙들을 여기에 정의합니다 ...

# 규칙을 테스트하기 위한 사실들을 주장합니다.
assert_fact('inventory_management', {'item_id': 'solar charger', 'quantity': 6, 'action': 'add'})
assert_fact('inventory_management', {'item_id': '12345', 'quantity': 0, 'action': 'sell'})

