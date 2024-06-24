from durable.lang import *

with ruleset('inventory_management'):
    
    # 재고 부족 알림
    @when_all((m.quantity < 300) & (m.quantity > 0))
    def low_stock(c):
        c.assert_fact({'type': 'alert', 'message': '재고 부족 - 품목 {}의 재고가 부족합니다'.format(c.m.item_id)})
        print('재고 부족 알림 - 품목 {}의 재고 부족'.format(c.m.item_id))

    # 과다 재고 알림
    @when_all(m.quantity >= 1000)
    def excess_stock(c):
        c.assert_fact({'type': 'alert', 'message': '과다 재고 - 품목 {}의 재고가 과다합니다'.format(c.m.item_id)})
        print('과다 재고 알림 - 품목 {}의 재고 과다'.format(c.m.item_id))

    # 재고가 판매될 때
    @when_all((m.action == 'sell') & (m.quantity > 0))
    def process_order(c):
        c.assert_fact('inventory_management', {'item_id': c.m.item_id, 'quantity': -1 * c.m.quantity, 'action': 'update'})
        print('{} 개의 품목 {}이 판매되었습니다'.format(c.m.quantity, c.m.item_id))

    # 재고가 반품될 때
    @when_all((m.action == 'return') & (m.quantity > 0))
    def return_stock(c):
        c.assert_fact('inventory_management', {'item_id': c.m.item_id, 'quantity': c.m.quantity, 'action': 'update'})
        print('{} 개의 품목 {}이 반품되었습니다'.format(c.m.quantity, c.m.item_id))

    # 재고 부족시 알림
    @when_all((m.quantity == 0))
    def out_of_stock(c):
        c.assert_fact({'type': 'alert', 'message': '재고 부족 - 품목 {}의 재고가 없습니다'.format(c.m.item_id)})
        print('재고 부족 알림 - 품목 {}의 재고 부족'.format(c.m.item_id))

    # 재고 충분시 알림
    @when_all((m.quantity >= 500) & (m.quantity < 1000))
    def sufficient_stock(c):
        c.assert_fact({'type': 'alert', 'message': '품목 {}의 재고가 충분합니다'.format(c.m.item_id)})
        print('충분한 재고 알림 - 품목 {}의 재고 충분'.format(c.m.item_id))

    # 재고 이동시
    @when_all((m.action == 'move') & (m.quantity > 0))
    def move_stock(c):
        print('{} 개의 품목 {}이 이동되었습니다'.format(c.m.quantity, c.m.item_id))

    # 판매 기간 경과 알림
    @when_all((m.expiry_date < '2024-12-31') & (m.quantity > 0))
    def expiry_alert(c):
        print('유통 기한 경과 - 품목 {}의 판매 기한이 지났습니다'.format(c.m.item_id))

    # MOQ할인 - 100개 이상 구매시
    @when_all((m.action == 'discount') & (m.quantity >= 100))
    def moq_discount(c):
        print('MOQ 할인 적용 - 품목 {}의 주문이 100개 이상으로 할인율이 적용됩니다'.format(c.m.item_id))

    # 주문 처리
    @when_all(m.action == 'sell')
    def process_order(c):
        c.assert_fact({'item_id': c.m.item_id, 'quantity': c.m.quantity * -1, 'action': 'update'})
        print('주문 처리 - {} 개의 품목 {}이 판매됨'.format(c.m.quantity, c.m.item_id))

    # 반품 처리
    @when_all(m.action == 'return')
    def return_stock(c):
        c.assert_fact({'item_id': c.m.item_id, 'quantity': c.m.quantity, 'action': 'update'})
        print('반품 처리 - {} 개의 품목 {}이 반품됨'.format(c.m.quantity, c.m.item_id))

    # 이동 처리
    @when_all(m.action == 'move')
    def move_stock(c):
        print('{} 개의 품목 {}이 이동됨'.format(c.m.quantity, c.m.item_id))

    # 할인 처리
    @when_all(m.action == 'discount')
    def apply_discount(c):
        print('할인 처리 - 특정 제품 세트를 구매하면 할인을 제공합니다')

    # 최신 제품 홍보
    @when_all(m.action == 'promotion')
    def product_promotion(c):
        print('최신 제품 홍보 시작 - 새로운 제품이 출시되면 관련된 마케팅 활동을 시작합니다')

    # 재고 이동 로그 기록
    @when_all(m.action == 'move')
    def stock_movement_log(c):
        print('재고 이동 로그 기록 - 품목 {}의 재고가 이동됨'.format(c.m.item_id))

    # 입고 예정 알림
    @when_all(m.action == 'incoming')
    def incoming_stock_alert(c):
        print('입고 예정 알림 - 입고 예정인 제품에 대한 알림을 관리자에게 전송합니다')

    # 인기 제품 재고 관리
    @when_all((m.popularity == 'high') & (m.quantity < 20))
    def popular_item_stock_management(c):
        print('인기 제품 재고 관리 - 인기 있는 제품에 대한 재고를 신속하게 관리하여 수요를 충족합니다')

    # 선구매 특전 제공
    @when_all(m.action == 'preorder')
    def preorder_benefit(c):
        print('선구매 특전 제공 - 새로운 제품 출시 전 선구매자에게 특전을 제공합니다')

    # 제품 할인 이벤트
    @when_all((m.action == 'discount_event') & (m.discount_period == '2024-04-01'))
    def product_discount_event(c):
        print('제품 할인 이벤트 - 특정 기간 동안 일부 제품에 할인 이벤트를 진행합니다')

    # 재고 손실 관리
    @when_all(m.action == 'loss')
    def stock_loss_management(c):
        print('재고 손실 관리 - 재고 손실 발생 시 해당 사항을 추적하고 조치를 취합니다')

    # 시즌 제품 재고 관리
    @when_all(m.season == 'summer')
    def seasonal_item_stock_management(c):
        print('시즌 제품 재고 관리 - 시즌에 따라 수요가 변하는 제품의 재고를 관리합니다')


# 재고 데이터
inventory = {
    '2024 3월호-투석기': 3796,
    '2024 3월호-동전분리': 3819,
    '2024 3월호-글러브': 3327,
    '2024 3월호-전기없이': 3839,
    '4월호-디딜방아': 4220,
    '4월호-도미노': 5120,
    '4월호-봉선화': 2946,
    '4월호-과학자 등록증': 4190,
    '키잼펜': 0,
    '20색 필라멘트': 360,
    '크리스탈 대': 752,
    '크리스탈 대-패드': 1102,
    '크리스탈 대-스펀지': 1000,
    '크리스탈 소': 1185,
    '크리스탈 소-패드': 1018,
    '크리스탈 소-스펀지': 948,
    '키모도장 블루': 470,
    '키모도장 핑크': 101,
    '키모도장 퍼플': 0,
    '키모도장-패드': 661,
    '키모도장-스펀지': 1073,
    '키모도장-뚜껑': 2843,
    '베이직도장 블루': 677,
    '베이직도장 핑크': 596,
    '베이직도장 퍼플': 104,
    '베이직도장-패드': 1042,
    '베이직도장-뚜껑': 2147,
    'Stampmaker장비(P90)': 11,
    '레이저프린터': 3,
    '크리스탈 6구 케이스': 800,
    '청사초롱': 319,
    '캠퍼밴': 475,
    '만년달력': 114,
    '아크릴 무드등': 122,
    '공기청정기': 336,
    '사인보드': 77,
    '강아지집': 297,
    '고양이집': 204,
    '선풍기-블루블랙': 590,
    '선풍기-화이트핑크': 684,
    '늘봄돌봄1호': 828,
    '늘봄돌봄2호': 838,
    '늘봄돌봄3호': 870,
    '늘봄돌봄4호': 870,
    '늘봄돌봄5호': 990,
    '퍼즐 Pre-A4': 968,
    '퍼즐 pre-A1': 1000,
    '3월-TV무드등': 0,
    '오리스쿠터': 435,
    '프로펠러 비행기': 241,
    '엘리베이터': 263,
    '양날개 프로펠러 비행기': 655,
    '회전목마': 515,
    '대포': 651,
    '천칭레이더': 651,
    '페널티킥': 651,
    '다람쥐': 797
}


# 재고 부족 알림 테스트 (투석기)
assert_fact('inventory_management', {'item_id': '2024 3월호-투석기', 'quantity': 200, 'action': 'sell'})

# 과다 재고 알림 테스트 (4월호-디딜방아)
assert_fact('inventory_management', {'item_id': '4월호-디딜방아', 'quantity': 1500})

# 재고가 판매될 때 테스트 (크리스탈 대)
assert_fact('inventory_management', {'item_id': '크리스탈 대', 'quantity': 100, 'action': 'sell'})

# 재고가 반품될 때 테스트 (크리스탈 대-패드)
assert_fact('inventory_management', {'item_id': '크리스탈 대-패드', 'quantity': 50, 'action': 'return'})

# 재고 부족시 알림 테스트 (키잼펜)
assert_fact('inventory_management', {'item_id': '키잼펜', 'quantity': 0})

# 재고 충분시 알림 테스트 (20색 필라멘트)
assert_fact('inventory_management', {'item_id': '20색 필라멘트', 'quantity': 800})

# 재고 이동시 테스트 (크리스탈 대-패드)
assert_fact('inventory_management', {'item_id': '크리스탈 대-패드', 'quantity': 20, 'action': 'move'})

# 판매 기간 경과 알림 테스트 (3월-TV무드등)
assert_fact('inventory_management', {'item_id': '3월-TV무드등', 'quantity': 50, 'expiry_date': '2024-03-15'})

# MOQ할인 테스트 (Stampmaker장비(P90))
assert_fact('inventory_management', {'item_id': 'Stampmaker장비(P90)', 'quantity': 120, 'action': 'discount'})

# 주문 처리 테스트 (퍼즐 pre-A1)
assert_fact('inventory_management', {'item_id': '퍼즐 pre-A1', 'quantity': 50, 'action': 'sell'})

# 반품 처리 테스트 (퍼즐 Pre-A4)
assert_fact('inventory_management', {'item_id': '퍼즐 Pre-A4', 'quantity': 20, 'action': 'return'})

# 이동 처리 테스트 (청사초롱)
assert_fact('inventory_management', {'item_id': '청사초롱', 'quantity': 100, 'action': 'move'})

# 할인 처리 테스트 (베이직도장-패드)
assert_fact('inventory_management', {'item_id': '베이직도장-패드', 'quantity': 150, 'action': 'discount'})

# 최신 제품 홍보 테스트 (Stampmaker장비(P90))
assert_fact('inventory_management', {'item_id': 'Stampmaker장비(P90)', 'action': 'promotion'})

# 재고 이동 로그 기록 테스트 (베이직도장-뚜껑)
assert_fact('inventory_management', {'item_id': '베이직도장-뚜껑', 'quantity': 30, 'action': 'move'})

# 입고 예정 알림 테스트 (다람쥐)
assert_fact('inventory_management', {'item_id': '다람쥐', 'action': 'incoming'})

# 인기 제품 재고 관리 테스트 (늘봄돌봄5호)
assert_fact('inventory_management', {'item_id': '늘봄돌봄5호', 'quantity': 10, 'popularity': 'high'})

# 선구매 특전 제공 테스트 (베이직도장 블루)
assert_fact('inventory_management', {'item_id': '베이직도장 블루', 'action': 'preorder'})

# 제품 할인 이벤트 테스트 (2024년 4월 1일에 할인 이벤트를 진행하는 상품)
assert_fact('inventory_management', {'item_id': '크리스탈 대-패드', 'action': 'discount_event', 'discount_period': '2024-04-01'})

# 재고 손실 관리 테스트 (레이저프린터)
assert_fact('inventory_management', {'item_id': '레이저프린터', 'action': 'loss'})

# 시즌 제품 재고 관리 테스트 (오리스쿠터)
assert_fact('inventory_management', {'item_id': '오리스쿠터', 'season': 'summer'})



