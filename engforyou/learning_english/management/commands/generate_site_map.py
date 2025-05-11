import os
from django.core.management.base import BaseCommand
from django.urls import get_resolver
import graphviz

class Command(BaseCommand):
    help = 'generate struct'
    def handle(self, *args, **options):
        dot = graphviz.Digraph(comment='Структура сайта')
        resolver = get_resolver()
        print(resolver)
        for pattern in resolver.url_patterns:
            path = pattern.pattern._regex.pattern.replace('^', '').replace('$', '')
            dot.node(pattern.name, f'{pattern.name}|n/{path}')

            if hasaatr(pattern, 'url_patterns'):
                self.add_included_urls(dot, pattern.url_patterns, pattern.name)


        dot.render('structure', format='png')