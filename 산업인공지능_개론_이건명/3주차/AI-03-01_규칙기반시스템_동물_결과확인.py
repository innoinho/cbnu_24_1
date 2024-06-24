from durable.lang import *

with ruleset('animal'):
    @when_all(c.first << (m.predicate == 'eats') & (m.object == 'flies'),
              (m.predicate == 'lives') & (m.object == 'water') & (m.subject == c.first.subject))
    def frog(c):
        c.assert_fact({'subject': c.first.subject, 'predicate': 'is', 'object': 'frog'})
        
        
    @when_all(c.first << ((m.predicate == 'eats') & (m.object == 'flies')),
              (m.predicate == 'lives') & (m.object == 'land') & (m.subject == c.first.subject))
    def chameleon(c):
        c.assert_fact({'subject': c.first.subject, 'predicate': 'is', 'object': 'chameleon'})

    @when_all((m.predicate == "eats") & (m.object == "worms"))
    def bird(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'is', 'object': 'bird'})

    @when_all((m.predicate == "is") & (m.object == "frog"))
    def green(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'is', 'object': 'green'})

    @when_all((m.predicate == "is") & (m.object == "chameleon"))
    def grey(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'is', 'object': 'grey'})

    @when_all((m.predicate == "is") & (m.object == "bird"))
    def black(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'is', 'object': 'black'})

    @when_all(+m.subject)  # m.subject가 달라질 때
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))

# 사실 주장하기
assert_fact('animal', {'subject': 'Kermit', 'predicate': 'eats', 'object': 'flies'})
assert_fact('animal', {'subject': 'Kermit', 'predicate': 'lives', 'object': 'water'})
assert_fact('animal', {'subject': 'Greedy', 'predicate': 'eats', 'object': 'flies'})
assert_fact('animal', {'subject': 'Greedy', 'predicate': 'lives', 'object': 'land'})  
assert_fact('animal', {'subject': 'Tweety', 'predicate': 'eats', 'object': 'worms'})