from durable.lang import *

with ruleset('inventory_management'):
    
    # 규칙 1: 재고 부족 알림
    @when_all(m.quantity < 10)
    def low_stock(c):
        c.post({'type': 'alert', 'message': '재고 부족 - 품목 {}의 재고가 부족합니다'.format(c.m.item_id)})

    # 규칙 2: 신규 재고 입고 알림
    @when_all(m.action == 'add')
    def new_stock(c):
        c.post({'type': 'alert', 'message': '신규 재고 입고 - 품목 {}의 새로운 재고가 입고되었습니다'.format(c.m.item_id)})

    # 규칙 3: 과다 재고 알림
    @when_all(m.quantity >= 100)
    def excess_stock(c):
        c.post({'type': 'alert', 'message': '과다 재고 - 품목 {}의 재고가 과다합니다'.format(c.m.item_id)})

    # 규칙 4: 주문 처리
    @when_all(m.action == 'sell')
    def process_order(c):
        c.assert_fact({'item_id': c.m.item_id, 'quantity': c.m.quantity * -1, 'action': 'update'})

    # 규칙 5: 재고 업데이트
    @when_all(m.action == 'update')
    def update_stock(c):
        print('{} 개의 품목 {}이 판매되었습니다'.format(c.m.quantity, c.m.item_id))

    # 규칙 6: 최소 주문 수량 제한
    @when_all((m.action == 'sell') & (m.quantity < 5))
    def min_order_limit(c):
        print('최소 주문 수량 미달 - 품목 {}의 최소 주문 수량을 충족하지 못했습니다'.format(c.m.item_id))

    # 규칙 7: 재고 회수
    @when_all(m.action == 'return')
    def return_stock(c):
        
        c.assert_fact({'item_id': c.m.item_id, 'quantity': c.m.quantity, 'action': 'update'})

    # 규칙 8: 재고 이동
    @when_all(m.action == 'move')
    def move_stock(c):
        print('{} 개의 품목 {}이 이동되었습니다'.format(c.m.quantity, c.m.item_id))

    # 규칙 9: 유통 기한 경과 알림
    @when_all((m.expiry_date < '2024-12-31') & (m.quantity > 0))
    def expiry_alert(c):
        print('유통 기한 경과 - 품목 {}의 유통 기한이 지났습니다'.format(c.m.item_id))

    # 규칙 10: 제품 세트 할인
    @when_all(m.action == 'discount')
    def apply_discount(c):
        print('제품 세트 할인 적용 - 특정 제품 세트를 구매하면 할인을 제공합니다')

    # 규칙 11: 최신 제품 홍보
    @when_all(m.action == 'promotion')
    def product_promotion(c):
        print('최신 제품 홍보 시작 - 새로운 제품이 출시되면 관련된 마케팅 활동을 시작합니다')

    # 규칙 12: 재고 이동 로그 기록
    @when_all(m.action == 'move')
    def stock_movement_log(c):
        print('재고 이동 로그 기록 - 품목 {}의 재고가 이동되었습니다'.format(c.m.item_id))

    # 규칙 13: 입고 예정 알림
    @when_all(m.action == 'incoming')
    def incoming_stock_alert(c):
        print('입고 예정 알림 - 입고 예정인 제품에 대한 알림을 관리자에게 전송합니다')

    # 규칙 14: 인기 제품 재고 관리
    @when_all((m.popularity == 'high') & (m.quantity < 20))
    def popular_item_stock_management(c):
        print('인기 제품 재고 관리 - 인기 있는 제품에 대한 재고를 신속하게 관리하여 수요를 충족합니다')

    # 규칙 15: 선구매 특전 제공
    @when_all(m.action == 'preorder')
    def preorder_benefit(c):
        print('선구매 특전 제공 - 새로운 제품 출시 전 선구매자에게 특전을 제공합니다')

    # 규칙 16: 제품 할인 이벤트
    @when_all((m.action == 'discount_event') & (m.discount_period == '2024-04-01'))
    def product_discount_event(c):
        print('제품 할인 이벤트 - 특정 기간 동안 일부 제품에 할인 이벤트를 진행합니다')

    # 규칙 17: 재고 손실 관리
    @when_all(m.action == 'loss')
    def stock_loss_management(c):
        print('재고 손실 관리 - 재고 손실 발생 시 해당 사항을 추적하고 조치를 취합니다')

    # 규칙 18: 시즌 제품 재고 관리
    @when_all(m.season == 'summer')
    def seasonal_item_stock_management(c):
        print('시즌 제품 재고 관리 - 시즌에 따라 수요가 변하는 제품의 재고를 관리합니다')

    # 규칙 19: 입고 우선순위
    @when_all((m.priority == 'high') & (m.action == 'incoming'))
    def incoming_priority(c):
        print('입고 우선순위 - 긴급한 주문이나 중요한 제품에 대한 입고 우선순위를 부여합니다')

    # 규칙 20: 재고 재조정
    @when_all((m.readjustment == 'scheduled') & (m.action == 'rearrange'))
    def stock_readjustment(c):
        print('재고 재조정 - 재고 수량과 수요를 기반으로 재고를 정기적으로 재조정합니다')

# 규칙을 테스트하기 위한 사실들을 주장합니다.
assert_fact('inventory_management', {'item_id': 'solar charger', 'quantity': 6, 'action': 'add'})
assert_fact('inventory_management', {'item_id': '12345', 'quantity': 0, 'action': 'sell'})

# 재고 부족 알림을 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item1', 'quantity': 5, 'action': 'add'})
assert_fact('inventory_management', {'item_id': 'item2', 'quantity': 8, 'action': 'add'})

# 신규 재고 입고 알림을 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item3', 'quantity': 20, 'action': 'add'})

# 과다 재고 알림을 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item4', 'quantity': 120, 'action': 'add'})

# 주문 처리를 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item5', 'quantity': 10, 'action': 'sell'})

# 재고 업데이트를 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item6', 'quantity': 15, 'action': 'update'})

# 최소 주문 수량 제한을 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item7', 'quantity': 3, 'action': 'sell'})

# 재고 회수를 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item8', 'quantity': 5, 'action': 'return'})

# 재고 이동을 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item9', 'quantity': 8, 'action': 'move'})

# 유통 기한 경과 알림을 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item10', 'quantity': 3, 'expiry_date': '2024-03-15'})

# 제품 세트 할인을 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item11', 'quantity': 10, 'action': 'discount'})

# 최신 제품 홍보를 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item12', 'quantity': 20, 'action': 'promotion'})

# 재고 이동 로그 기록을 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item13', 'quantity': 5, 'action': 'move'})

# 입고 예정 알림을 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item14', 'quantity': 50, 'action': 'incoming'})

# 인기 제품 재고 관리를 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item15', 'quantity': 15, 'popularity': 'high'})

# 선구매 특전 제공을 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item16', 'quantity': 10, 'action': 'preorder'})

# 제품 할인 이벤트를 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item17', 'quantity': 20, 'action': 'discount_event', 'discount_period': '2024-04-01'})

# 재고 손실 관리를 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item18', 'quantity': -5, 'action': 'loss'})

# 시즌 제품 재고 관리를 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item19', 'quantity': 30, 'season': 'summer'})

# 입고 우선순위를 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item20', 'quantity': 40, 'priority': 'high', 'action': 'incoming'})

# 재고 재조정을 테스트하는 예시
assert_fact('inventory_management', {'item_id': 'item21', 'quantity': 60, 'readjustment': 'scheduled', 'action': 'rearrange'})

