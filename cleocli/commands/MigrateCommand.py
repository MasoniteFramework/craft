from cleo import Command
import os
from subprocess import check_output


class MigrateCommand(Command):
    """
    Run migrations.

    migrate
    """

    def handle(self):
        try:
            from wsgi import container
        except ImportError:
            self.comment(
                'This command must be ran at the Masonite root directory')
            return

        migration_directory = ['databases/migrations']
        for key, value in container.providers.items():
            if '_MigrationDirectory' in key:
                migration_directory.append(value)

        for directory in reversed(migration_directory):
            self.info('Migrating: {0}'.format(directory))
            try:
                output = bytes(check_output(
                        ['orator', 'migrate', '-c', 'config/database.py', '-p', directory, '-f']
                    )).decode('utf-8')

                self.info(output)
            except:
                pass
