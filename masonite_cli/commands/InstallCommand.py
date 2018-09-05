from cleo import Command
from subprocess import call
import shutil


class InstallCommand(Command):
    """
    Installs all of Masonite's dependencies

    install
        {--no-key : If set, craft install command will not generate and store a new key}
    """

    def handle(self):

        shutil.copy('.env-example', '.env')         

        call(["pip3", "install", "-r", "requirements.txt"])
            
        if not self.option('no-key'):
            call(["craft", "key", "--store"])

