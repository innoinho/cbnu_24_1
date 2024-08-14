from durable.lang import *

with ruleset('인사관리'):
    # 규칙1. 새 직원 입사
    @when_all((m.predicate == '입사') & (m.object == '새 직원'))
    def welcome_new_employee(c):
        print('새 직원이 입사했습니다.')

    # 규칙2. 기존 직원 입사
    @when_all((m.predicate == '입사') & (m.object == '기존 직원'))
    def welcome_existing_employee(c):
        print('기존 직원이 승진했습니다.')

    # 규칙3. 직원 퇴사
    @when_all((m.predicate == '퇴사') & (m.object == '직원'))
    def farewell_employee(c):
        print('직원이 퇴사했습니다.')

    # 규칙4. 새 해 시작
    @when_all((m.predicate == '새 해') & (m.object == '시작'))
    def new_year_start(c):
        print('새 해가 시작되었습니다.')

    # 규칙5. 사내 행사
    @when_all((m.predicate == '사내') & (m.object == '행사'))
    def company_event(c):
        print('사내 행사가 있습니다.')

    # 규칙6. 인사팀 회의
    @when_all((m.predicate == '인사팀') & (m.object == '회의'))
    def hr_meeting(c):
        print('인사팀 회의 중입니다.')

    # 규칙7. 새 프로젝트 시작
    @when_all((m.predicate == '새') & (m.object == '프로젝트') & (m.subject == '시작'))
    def new_project_start(c):
        print('새 프로젝트가 시작되었습니다.')

    # 규칙8. 팀 변경
    @when_all((m.predicate == '팀') & (m.object == '변경'))
    def team_change(c):
        print('팀이 변경되었습니다.')

    # 규칙9. 업무 증가
    @when_all((m.predicate == '업무') & (m.object == '증가'))
    def increased_workload(c):
        print('업무가 증가했습니다.')

    # 규칙10. 직원 성과
    @when_all((m.predicate == '직원') & (m.object == '성과'))
    def employee_achievement(c):
        print('직원의 성과가 있었습니다.')

    # 규칙11. 사내 교육
    @when_all((m.predicate == '사내') & (m.object == '교육'))
    def internal_training(c):
        print('사내 교육이 진행 중입니다.')

    # 규칙12. 업무 프로세스 변경
    @when_all((m.predicate == '업무') & (m.object == '프로세스') & (m.subject == '변경'))
    def process_change(c):
        print('업무 프로세스가 변경되었습니다.')

    # 규칙13. 프로젝트 마감
    @when_all((m.predicate == '프로젝트') & (m.object == '마감'))
    def project_deadline(c):
        print('프로젝트가 마감되었습니다.')

    # 규칙14. 클라이언트 회의
    @when_all((m.predicate == '클라이언트') & (m.object == '회의'))
    def client_meeting(c):
        print('클라이언트와 회의 중입니다.')

    # 규칙15. 연차 신청
    @when_all((m.predicate == '연차') & (m.object == '신청'))
    def leave_request(c):
        print('연차를 신청했습니다.')

    # 규칙16. 업무 지시
    @when_all((m.predicate == '업무') & (m.object == '지시'))
    def task_assignment(c):
        print('새로운 업무를 받았습니다.')

    # 규칙17. 프로모션
    @when_all((m.predicate == '프로모션') & (m.object == '받음'))
    def promotion(c):
        print('프로모션을 받았습니다.')

    # 규칙18. 업무 이관
    @when_all((m.predicate == '업무') & (m.object == '이관'))
    def task_transfer(c):
        print('업무가 이관되었습니다.')

    # 규칙19. 수습 기간 시작
    @when_all((m.predicate == '수습') & (m.object == '기간') & (m.subject == '시작'))
    def probation_period_start(c):
        print('수습 기간이 시작되었습니다.')

    # 규칙20. 수습 기간 종료
    @when_all((m.predicate == '수습') & (m.object == '기간') & (m.subject == '종료'))
    def probation_period_end(c):
        print('수습 기간이 종료되었습니다.')

    # 규칙21. 인사 관련 공지
    @when_all((m.predicate == '인사') & (m.object == '공지'))
    def hr_notice(c):
        print('인사 관련 공지가 있습니다.')
        
    @when_all(+m.subject)    
    def 출력(c):
        print('사실: {0} {1} {2}'.format(c.m.predicate, c.m.object, c.m.subject))    

# 사실 주장하기
assert_fact('인사관리', {'predicate': '입사', 'object': '새 직원'})
assert_fact('인사관리', {'predicate': '입사', 'object': '기존 직원'})
assert_fact('인사관리', {'predicate': '퇴사', 'object': '직원'})
assert_fact('인사관리', {'predicate': '새 해', 'object': '시작'})
assert_fact('인사관리', {'predicate': '사내', 'object': '행사'})
assert_fact('인사관리', {'predicate': '인사팀', 'object': '회의'})
assert_fact('인사관리', {'predicate': '새', 'object': '프로젝트', 'subject': '시작'})
assert_fact('인사관리', {'predicate': '팀', 'object': '변경'})
assert_fact('인사관리', {'predicate': '업무', 'object': '증가'})
assert_fact('인사관리', {'predicate': '직원', 'object': '성과'})
assert_fact('인사관리', {'predicate': '사내', 'object': '교육'})
assert_fact('인사관리', {'predicate': '업무', 'object': '프로세스', 'subject': '변경'})
assert_fact('인사관리', {'predicate': '프로젝트', 'object': '마감'})
assert_fact('인사관리', {'predicate': '클라이언트', 'object': '회의'})
assert_fact('인사관리', {'predicate': '연차', 'object': '신청'})
assert_fact('인사관리', {'predicate': '업무', 'object': '지시'})
assert_fact('인사관리', {'predicate': '프로모션', 'object': '받음'})
assert_fact('인사관리', {'predicate': '업무', 'object': '이관'})
assert_fact('인사관리', {'predicate': '수습', 'object': '기간', 'subject': '시작'})
assert_fact('인사관리', {'predicate': '수습', 'object': '기간', 'subject': '종료'})
assert_fact('인사관리', {'predicate': '인사', 'object': '공지'})

