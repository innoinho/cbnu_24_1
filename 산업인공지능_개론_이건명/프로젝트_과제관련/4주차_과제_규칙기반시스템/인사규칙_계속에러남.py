from durable.lang import *

# Rule Definitions
with ruleset('hr_rules'):
    
    # Rule 1: 승진 규칙 - 사원에서 대리로 승진
    @when_all(m.subject == '사원', m.promotion == '대리')
    def promote_to_assistant(c):
        c.assert_fact({ 'subject': '사원', 'promotion': '대리' })
        print("주장: 사원이 대리로 승진되어야 합니다.")
        
    # Rule 2: 징계 규칙 - 결근 3회 이상인 경우 징계
    @when_all(m.subject == '결근', m.count >= 3)
    def discipline_for_absenteeism(c):
        c.assert_fact({ 'subject': '결근', 'count': 3 })
        print("주장: 결근이 3회 이상인 경우 징계되어야 합니다.")
        
    # Rule 3: 퇴사 규칙 - 연차 사용 후 3일 이상 무단 결근한 경우 퇴사
    @when_all(m.subject == '무단결근', m.days >= 3)
    def dismiss_after_unauthorized_absence(c):
        c.assert_fact({ 'subject': '무단결근', 'days': 3 })
        print("주장: 연차 사용 후 3일 이상 무단 결근 시 퇴사되어야 합니다.")
        
    # 추가 규칙 4: 출근 기록이 없는 경우 경고
    @when_all(m.subject == '출근기록', m.status == '없음')
    def warn_for_missing_check_in(c):
        c.assert_fact({ 'subject': '출근기록', 'status': '없음' })
        print("주장: 출근 기록이 없는 경우 경고가 발령되어야 합니다.")
        
    # 추가 규칙 5: 휴가 3일 이상이면 보상 휴가 지급
    @when_all(m.subject == '휴가', m.days >= 3)
    def compensate_long_vacation(c):
        c.assert_fact({ 'subject': '휴가', 'days': 5 })
        print("주장: 휴가가 3일 이상인 경우 보상 휴가가 지급되어야 합니다.")
        
    # 추가 규칙 6: 출장 신청 후 2주 이내에 결재가 이뤄져야 함
    @when_all(m.subject == '출장신청', m.duration <= 14)
    def approve_business_trip_within_2_weeks(c):
        c.assert_fact({ 'subject': '출장신청', 'duration': 10 })
        print("주장: 출장 신청 후 2주 이내에 결재가 이뤄져야 합니다.")
        
    # 추가 규칙 7: 성과평가 점수가 70점 미만이면 개선 계획 수립
    @when_all(m.subject == '성과평가', m.score < 70)
    def create_improvement_plan(c):
        c.assert_fact({ 'subject': '성과평가', 'score': 65 })
        print("주장: 성과평가 점수가 70점 미만인 경우 개선 계획이 수립되어야 합니다.")
        
    # 추가 규칙 8: 연차 사용 신청 후 3일 이내에 결재가 이뤄져야 함
    @when_all(m.subject == '연차신청', m.duration <= 3)
    def approve_leave_within_3_days(c):
        c.assert_fact({ 'subject': '연차신청', 'duration': 2 })
        print("주장: 연차 사용 신청 후 3일 이내에 결재가 이뤄져야 합니다.")
        
    # 추가 규칙 9: 수습기간 동안 업무 수행 미흡 시 수습기간 연장 결정
    @when_all(m.subject == '수습기간', m.performance == '미흡')
    def extend_probation_period_for_poor_performance(c):
        c.assert_fact({ 'subject': '수습기간', 'performance': '미흡' })
        print("주장: 수습기간 동안 업무 수행이 미흡한 경우 수습기간이 연장되어야 합니다.")
        
    # 추가 규칙 10: 휴가 신청 후 1주일 이내에 결재가 이뤄져야 함
    @when_all(m.subject == '휴가신청', m.duration > 3, m.duration <= 7)
    def approve_leave_within_1_week(c):
        c.assert_fact({ 'subject': '휴가신청', 'duration': 2 })
        print("주장: 휴가 신청 후 1주일 이내에 결재가 이뤄져야 합니다.")

        
    # 추가 규칙 11: 연차 잔여 일수가 0인 경우 추가 휴가 지급
    @when_all(m.subject == '휴가잔여일', m.count == 0)
    def provide_additional_leave_when_no_remaining(c):
        c.assert_fact({ 'subject': '휴가잔여일', 'count': 0 })
        print("주장: 연차 잔여 일수가 0일 경우 추가 휴가가 지급되어야 합니다.")
        
    # 추가 규칙 12: 근태 기록이 미비할 경우 직원 교육 실시
    @when_all(m.subject == '근태기록', m.quality == '미흡')
    def conduct_employee_training_for_poor_attendance_records(c):
        c.assert_fact({ 'subject': '근태기록', 'quality': '미흡' })
        print("주장: 근태 기록이 미비한 경우 직원 교육이 실시되어야 합니다.")
        
    # 추가 규칙 13: 직무능력평가 점수가 80점 미만인 경우 개인 발전 계획 수립
    @when_all(m.subject == '직무능력평가', m.score < 80)
    def create_personal_development_plan_for_low_performance(c):
        c.assert_fact({ 'subject': '직무능력평가', 'score': 75 })
        print("주장: 직무능력평가 점수가 80점 미만인 경우 개인 발전 계획이 수립되어야 합니다.")
        
    # 추가 규칙 14: 인사평가 결과에 따라 보상금 지급
    @when_all(m.subject == '인사평가', m.result == '우수')
    def provide_bonus_based_on_performance_evaluation(c):
        c.assert_fact({ 'subject': '인사평가', 'result': '우수' })
        print("주장: 인사평가 결과에 따라 보상금이 지급되어야 합니다.")
        
    # 추가 규칙 15: 직무능력평가 실시 후 2주 이내에 결과 통보
    @when_all(m.subject == '직무능력평가', m.duration == 14)
    def notify_results_within_2_weeks_after_performance_evaluation(c):
        c.assert_fact({ 'subject': '직무능력평가', 'duration': 14 })
        print("주장: 직무능력평가 실시 후 2주 이내에 결과가 통보되어야 합니다.")

        
    # 추가 규칙 16: 경력 개발 프로그램 참여 시간이 지나치게 짧은 경우 경고
    @when_all(m.subject == '경력개발프로그램', m.duration <= 7)
    def warn_for_short_participation_in_career_development_program(c):
        c.assert_fact({ 'subject': '경력개발프로그램', 'duration': 5 })
        print("주장: 경력 개발 프로그램 참여 시간이 짧은 경우 경고가 발령되어야 합니다.")
        
    # 추가 규칙 17: 휴가 신청 후 3일 이내에 결재가 이뤄져야 함
    @when_all(m.subject == '휴가신청', m.duration <= 3)
    def approve_leave_within_3_days_after_request(c):
        c.assert_fact({ 'subject': '휴가신청', 'duration': 2 })
        print("주장: 휴가 신청 후 3일 이내에 결재가 이뤄져야 합니다.")
        
    # 추가 규칙 18: 출장 신청 후 1주 이내에 결재가 이뤄져야 함
    @when_all(m.subject == '출장신청', m.duration <= 7)
    def approve_business_trip_within_1_week(c):
        c.assert_fact({ 'subject': '출장신청', 'duration': 5 })
        print("주장: 출장 신청 후 1주 이내에 결재가 이뤄져야 합니다.")
        
    # 추가 규칙 19: 인사평가 결과에 따라 승진 여부 결정
    @when_all(m.subject == '인사평가', m.result == '우수')
    def decide_promotion_based_on_performance_evaluation(c):
        c.assert_fact({ 'subject': '인사평가', 'result': '우수' })
        print("주장: 인사평가 결과에 따라 승진 여부가 결정되어야 합니다.")
        
    # 추가 규칙 20: 출근 기록이 미비할 경우 훈련 필요성 평가
    @when_all(m.subject == '출근기록', m.quality == '미흡')
    def assess_need_for_training_for_poor_check_in_records(c):
        c.assert_fact({ 'subject': '출근기록', 'quality': '미흡' })
        print("주장: 출근 기록이 미비한 경우 훈련 필요성 평가가 이뤄져야 합니다.")

    # 위에 정의된 규칙에 따라 주장할 사실을 추가합니다.
assert_fact('hr_rules', { 'subject': '사원', 'promotion': '대리' })
assert_fact('hr_rules', { 'subject': '결근', 'count': 3 })
assert_fact('hr_rules', { 'subject': '무단결근', 'days': 3 })
assert_fact('hr_rules', { 'subject': '출근기록', 'status': '없음' })
assert_fact('hr_rules', { 'subject': '휴가', 'days': 5 })
assert_fact('hr_rules', { 'subject': '출장신청', 'duration': 10 })
assert_fact('hr_rules', { 'subject': '성과평가', 'score': 65 })
assert_fact('hr_rules', { 'subject': '연차신청', 'duration': 2 })
assert_fact('hr_rules', { 'subject': '수습기간', 'performance': '미흡' })
assert_fact('hr_rules', { 'subject': '휴가신청', 'duration': 2 })
assert_fact('hr_rules', { 'subject': '휴가잔여일', 'count': 0 })
assert_fact('hr_rules', { 'subject': '근태기록', 'quality': '미흡' })
assert_fact('hr_rules', { 'subject': '직무능력평가', 'score': 75 })
assert_fact('hr_rules', { 'subject': '인사평가', 'result': '우수' })
assert_fact('hr_rules', { 'subject': '직무능력평가', 'duration': 14 })
assert_fact('hr_rules', { 'subject': '경력개발프로그램', 'duration': 5 })



