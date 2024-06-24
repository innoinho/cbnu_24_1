from durable.lang import *

# 새로운 규칙 세트 생성
with ruleset('business_rules_new_2'):
    # 규칙 1: 주문 금액이 1000 이상인 경우 무료 배송
    @when_all((m.action == 'order') & (m.amount >= 1000))
    def free_shipping(c):
        c.post({'action': 'shipping', 'status': 'free'})

    # 규칙 2: 신규 고객인 경우 할인 쿠폰 제공
    @when_all((m.action == 'signup') & (m.customer_type == 'new'))
    def discount_coupon(c):
        c.post({'action': 'coupon', 'type': 'discount', 'amount': 10})  # 예시 금액

    # 규칙 3: 제품 재고가 10개 미만인 경우 재고 알림
    @when_all((m.action == 'inventory') & (m.stock_level < 10))
    def low_inventory(c):
        c.post({'action': 'notification', 'type': 'inventory', 'status': 'low'})

    # 규칙 4: VIP 고객인 경우 추가 혜택 제공
    @when_all((m.action == 'order') & (m.customer_type == 'vip'))
    def vip_benefit(c):
        c.post({'action': 'benefit', 'type': 'additional', 'description': 'Free express shipping'})  # 예시 혜택

    # 기존 규칙들...
    @when_all((m.action == 'shipping') & (m.status == 'free'))
    def print_shipping_result(c):
        print('Shipping status: Free')

    @when_all((m.action == 'coupon') & (m.type == 'discount'))
    def print_coupon_result(c):
        print('Coupon type: Discount, Amount: {}'.format(c.m.amount))

    @when_all((m.action == 'notification') & (m.type == 'inventory') & (m.status == 'low'))
    def print_notification_result(c):
        print('Inventory status: Low')

    @when_all((m.action == 'benefit') & (m.type == 'additional'))
    def print_benefit_result(c):
        print('Additional benefit: {}'.format(c.m.description))

    # 주문이 발생하고 'order'와 'amount'가 주어졌지만 VIP 고객이 아닌 경우에 대한 디버깅
    @when_all((m.action == 'order') & (m.amount >= 1000))
    def debug_no_vip_benefit(c):
        if 'customer_type' in c.m and c.m['customer_type'] != 'vip':
            print("Order received but customer is not a VIP. No additional benefit will be provided.")
            
assert_fact('business_rules_new_2', {'action': 'shipping', 'status': 'free'})



            