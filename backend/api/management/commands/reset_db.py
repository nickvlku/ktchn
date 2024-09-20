from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings

class Command(BaseCommand):
    help = 'Resets the database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Resetting the database...')
        
        with connection.cursor() as cursor:
            # Get all table names in the current schema
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
            """)
            tables = cursor.fetchall()
            
            # Disable foreign key checks
            cursor.execute("SET CONSTRAINTS ALL DEFERRED;")
            
            # Drop all tables
            for table in tables:
                cursor.execute(f'DROP TABLE IF EXISTS "{table[0]}" CASCADE')
            
            # Re-enable foreign key checks
            cursor.execute("SET CONSTRAINTS ALL IMMEDIATE;")

        # Run migrations
        from django.core.management import call_command
        call_command('makemigrations')
        call_command('migrate')

        self.stdout.write(self.style.SUCCESS('Database has been reset successfully.'))