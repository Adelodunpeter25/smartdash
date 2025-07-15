from django.core.management.base import BaseCommand
from dashboard.models import Utility

class Command(BaseCommand):
    help = 'Creates default utilities for the dashboard'

    def handle(self, *args, **kwargs):
        utilities = [
            {
                'name': 'Random Quote Generator',
                'description': 'Get inspired with a random quote every time you visit',
                'icon': '💬',
                'url_name': 'random_quote',
            },
            {
                'name': 'Calculator',
                'description': 'Perform basic arithmetic calculations easily',
                'icon': '🧮',
                'url_name': 'calculator',
            },
            {
                'name': 'Notepad',
                'description': 'Take quick notes or keep a daily journal',
                'icon': '📝',
                'url_name': 'notepad',
            },
            {
                'name': 'Currency Converter',
                'description': 'Convert between world currencies in real-time',
                'icon': '💱',
                'url_name': 'currency_converter',
            },
        ]
        
        created_count = 0
        for utility_data in utilities:
            utility, created = Utility.objects.get_or_create(
                name=utility_data['name'],
                defaults={
                    'description': utility_data['description'],
                    'icon': utility_data['icon'],
                    'url_name': utility_data['url_name'],
                }
            )
            if created:
                created_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} utilities'))