from cleo import Command
from subprocess import call
import os
import shutil

class InstallCommand(Command):
    """
    Installs all of Masonite's dependencies

    install
        {name=None : Name of your Masonite project}
        {--no-key : If set, craft install command will not generate and store a new key.}
    """

    def handle(self):
        name = self.argument('name')

        # Name is specified
        if self.argument('name') != 'None':
            if not os.path.isfile('{}/.env'.format(name)):
                shutil.copy('{}/.env-example'.format(name), '{}/.env'.format(name))
        else:
            if not os.path.isfile('.env'.format(name)):
                shutil.copy('.env-example'.format(name), '.env'.format(name))         
        
        call(["pip3", "install", "-r", "requirements.txt"])
            
        if self.argument('name') != 'None':
            call(["craft", "key", "--store"], cwd='{}'.format(name))
        else:
            if not self.option('no-key'):
                call(["craft", "key", "--store"])