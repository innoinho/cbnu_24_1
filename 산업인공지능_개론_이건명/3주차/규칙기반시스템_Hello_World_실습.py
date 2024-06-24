from durable.lang import *

with ruleset('testRS'):
        @when_all(m.subject == 'World')
        def say_hello(c):
            print('Hello', c.m.subject)
            
post('testRS', {'subject': 'World'})
