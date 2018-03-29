from cleo import Command
import os
from subprocess import call


class MakeMigrationCommand(Command):
    """
    Makes a new migration

    migration
        {name : Name of your migration}
        {--t|--table=False : Table you are migrating for}
        {--c|--create=False : Table you want to create with this migration}
    """

    def handle(self):
        name = self.argument('name')

        if self.option('create'):
            call(['orator', 'make:migration', name,
                            '-p', 'databases/migrations', '--table', self.option('create'), '--create'])
        elif self.option('table'):
            call(['orator', 'make:migration', name,
                            '-p', 'databases/migrations', '--table', self.option('table')])
        else:
            call(['orator', 'make:migration', name,
                            '-p', 'databases/migrations'])