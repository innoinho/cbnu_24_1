from durable.lang import *

with ruleset('동물'):
    @when_all(c.first << (m.predicate == '먹는다') & (m.object == '파리'),
              (m.predicate == '살고 있다') & (m.object == '물') & (m.subject == c.first.subject))
    def 개구리(c):
        c.assert_fact({'subject': c.first.subject, 'predicate': '은', 'object': '개구리'})
        
    @when_all(c.first << ((m.predicate == '먹는다') & (m.object == '파리')),
              (m.predicate == '살고 있다') & (m.object == '육지') & (m.subject == c.first.subject))
    def 카멜레온(c):
        c.assert_fact({'subject': c.first.subject, 'predicate': '은', 'object': '카멜레온'})

    @when_all((m.predicate == "먹는다") & (m.object == "벌레"))
    def 새(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': '은', 'object': '새'})

    @when_all((m.predicate == "은") & (m.object == "개구리"))
    def 녹색(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': '은', 'object': '녹색'})

    @when_all((m.predicate == "은") & (m.object == "카멜레온"))
    def 회색(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': '은', 'object': '회색'})

    @when_all((m.predicate == "은") & (m.object == "새"))
    def 검정(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': '은', 'object': '검정'})

    @when_all(+m.subject)  # m.subject가 달라질 때
    def 출력(c):
        print('사실: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))

# 사실 주장하기
assert_fact('동물', {'subject': '커밋', 'predicate': '먹는다', 'object': '파리'})
assert_fact('동물', {'subject': '커밋', 'predicate': '살고 있다', 'object': '물'})
assert_fact('동물', {'subject': '그리디', 'predicate': '먹는다', 'object': '파리'})
assert_fact('동물', {'subject': '그리디', 'predicate': '살고 있다', 'object': '육지'})  
assert_fact('동물', {'subject': '트위티', 'predicate': '먹는다', 'object': '벌레'})

