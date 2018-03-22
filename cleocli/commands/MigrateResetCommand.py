from cleo import Command
import os
from subprocess import check_output


class MigrateResetCommand(Command):
    """
    Migrate reset.

    migrate:reset
    """

    def handle(self):
        try:
            from wsgi import container
        except ImportError:
            self.comment(
                'This command must be ran at the Masonite root directory')
            return

        # Get any migration files from the Service Container
        migration_directory = ['databases/migrations']
        for key, value in container.providers.items():
            if '_MigrationDirectory' in key:
                migration_directory.append(value)

        # Load in the Orator migration system
        from orator.migrations import Migrator, DatabaseMigrationRepository
        from config import database
        repository = DatabaseMigrationRepository(database.DB, 'migrations')
        migrator = Migrator(repository, database.DB)
        if not migrator.repository_exists():
            repository.create_repository()

        # Create a new list of migrations with the correct file path instead
        migration_list = []
        for migration in migrator.get_repository().get_ran():
            for directory in migration_directory:
                if os.path.exists(os.path.join(directory, migration + '.py')):
                    migration_list.append(os.path.join(os.getcwd(), directory))
                    break

        # Rollback the migrations
        notes = []
        for migration in migrator.get_repository().get_ran():
            for migration_directory in migration_list:
                try:
                    migrator.reset(migration_directory)

                except:
                    pass

                if migrator.get_notes():
                    notes += migrator.get_notes()

        # Show notes from the migrator
        for note in notes:
            if not 'Nothing to rollback.' in note:
                self.line(note)
        if not notes:
            self.info('Nothing to rollback')
