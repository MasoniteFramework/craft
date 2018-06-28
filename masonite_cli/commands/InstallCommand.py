from cleo import Command
from subprocess import call
import os
import shutil


class InstallCommand(Command):
    """
    Installs all of Masonite's dependencies

    install
        {--no-key : If set, craft install command will not generate and store a new key}
    """

    def handle(self):

        if not os.path.isfile('.env'.format(name)):
            shutil.copy('.env-example'.format(name), '.env'.format(name))         
        
        call(["pip3", "install", "-r", "requirements.txt"])
            
        if not self.option('no-key'):
            call(["craft", "key", "--store"])

