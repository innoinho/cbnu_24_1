from durable.lang import *

# 새로운 규칙 세트 생성
with ruleset('business_rules_new'):
    
    # 규칙 1: 품목이 300개 이하라면 품목의 재고가 부족하다 알려줌
    @when_all((m.action == 'inventory') & (m.item_count <= 300)) 
    def low_inventory(c):
        print('규칙1: 품목 {}의 재고가 부족합니다.'.format(c.m.item_name))

    # 규칙 2: 품목이 1000개 이상이라면 품목의 재고가 과다하다 알려줌
    @when_all((m.action == 'inventory') & (m.item_count >= 1000))
    def excessive_inventory(c):
        print('규칙2: 품목 {}의 재고가 과다합니다.'.format(c.m.item_name))

    # 규칙 3: 품목 0이 된다면 품목의 재고가 없다고 알려줌
    @when_all((m.action == 'inventory') & (m.item_count == 0))
    def zero_inventory(c):
        print('규칙3: 품목 {}의 재고가 없습니다.'.format(c.m.item_name))

    # 규칙 4: 품목이 판매가 된다면 개수를 알려줌
    @when_all((m.action == 'sales'))
    def sales_notification(c):
        print('규칙4: 품목 {}이(가) {}개가 판매되었습니다.'.format(c.m.item_name, c.m.item_count))

    # 규칙 5: 품목이 반품이 되었다면 개수를 알려줌
    @when_all((m.action == 'return'))
    def return_notification(c):
        print('규칙5: 품목 {}이(가) {}개가 반품되었습니다.'.format(c.m.item_name, c.m.item_count))

    # 규칙 6: 품목이 이동한다면 개수를 알려줌
    @when_all((m.action == 'movement'))
    def movement_notification(c):
        print('규칙6: 품목 {}이(가) {}개가 이동되었습니다.'.format(c.m.item_name, c.m.item_count))

    # 규칙 7: 품목이 5개월의 기간이 지났다면 알려줌
    @when_all((m.action == 'expired'))
    def expired_notification(c):
        print('규칙7: 품목 {}의 판매기간이 지났습니다.'.format(c.m.item_name))

    # 규칙 8: 품목을 한번에 100개 이상 구매한다면 10% 할인율을 적용
    @when_all((m.action == 'purchase') & (m.item_count >= 100))
    def discount_10_percent(c):
        print('규칙8: 품목 {}을(를) 한번에 100개 이상 구매하면 10% 할인됩니다.'.format(c.m.item_name))

    # 규칙 9: 품목을 한번에 200개 이상을 구매한다면 20% 할인율을 적용
    @when_all((m.action == 'purchase') & (m.item_count >= 200))
    def discount_20_percent(c):
        print('규칙9: 품목 {}을(를) 한번에 200개 이상 구매하면 20% 할인됩니다.'.format(c.m.item_name))

    # 규칙 10: 새로운 품목이 입고된다면 프로모션 시작
    @when_all((m.action == 'new_item'))
    def promotion_start(c):
        print('규칙10: 새로운 품목 {}이(가) {}개 입고되어 프로모션을 시작합니다.'.format(c.m.item_name, c.m.item_count))

    # 규칙 11: 품목을 한번에 300개 이상을 구매한다면 30% 할인율을 적용
    @when_all((m.action == 'purchase') & (m.item_count >= 300))
    def discount_30_percent(c):
        print('규칙11: 품목 {}을(를) 한번에 300개 이상 구매하면 30% 할인됩니다.'.format(c.m.item_name))

    # 규칙 12: 신규고객이 구매시 무료배송 제공
    @when_all((m.action == 'purchase') & (m.customer_type == 'new'))
    def free_shipping(c):
        print('규칙12: 신규고객이 구매시 무료배송 제공됩니다.')

    # 규칙 13: VIP고객이라면 1+1 혜택 제공
    @when_all((m.action == 'purchase') & (m.customer_type == 'vip'))
    def buy_one_get_one_free(c):
        print('규칙13: VIP고객이라면 1+1 혜택이 제공됩니다.')

    # 규칙 14: 시즌에 따라 수요가 변하는 품목은 이동처리
    @when_all((m.action == 'seasonal_demand'))
    def handle_seasonal_demand(c):
        print('규칙14: 시즌에 따라 수요가 변하는 품목 {}은(는) 이동처리할 수 있도록 해주십시오.'.format(c.m.item_name))

    # 규칙 15: 선주문을 넣은 사람에게는 특전을 제공
    @when_all((m.action == 'pre_order'))
    def pre_order_benefit(c):
        print('규칙15: 선주문을 넣은 사람에게는 특전을 제공합니다.')

# 사실을 주장
assert_fact('business_rules_new', {'action': 'inventory', 'item_count': 250, 'item_name': 'A'})
assert_fact('business_rules_new', {'action': 'inventory', 'item_count': 1200, 'item_name': 'B'})
assert_fact('business_rules_new', {'action': 'inventory', 'item_count': 0, 'item_name': 'C'})
assert_fact('business_rules_new', {'action': 'sales', 'item_name': 'D', 'item_count': 50})
assert_fact('business_rules_new', {'action': 'return', 'item_name': 'E', 'item_count': 10})
assert_fact('business_rules_new', {'action': 'movement', 'item_name': 'F', 'item_count': 30})
assert_fact('business_rules_new', {'action': 'expired', 'item_name': 'G'})
assert_fact('business_rules_new', {'action': 'purchase', 'item_name': 'H', 'item_count': 150})
assert_fact('business_rules_new', {'action': 'new_item', 'item_name': 'I', 'item_count': 200})
assert_fact('business_rules_new', {'action': 'purchase', 'item_name': 'J', 'item_count': 350})
assert_fact('business_rules_new', {'action': 'purchase', 'item_name': 'K', 'item_count': 100, 'customer_type': 'new'})
assert_fact('business_rules_new', {'action': 'purchase', 'item_name': 'L', 'item_count': 200, 'customer_type': 'vip'})
assert_fact('business_rules_new', {'action': 'seasonal_demand', 'item_name': 'M'})
assert_fact('business_rules_new', {'action': 'pre_order', 'item_name': 'N'})



