from cleo import Application, Command
import os
import sys
from pydoc import ErrorDuringImport
from .helpers.helpers import add_venv_site_packages

from .commands.AuthCommand import AuthCommand
from .commands.CommandCommand import CommandCommand
from .commands.ControllerCommand import ControllerCommand
from .commands.InstallCommand import InstallCommand
from .commands.JobCommand import JobCommand
from .commands.KeyCommand import KeyCommand
from .commands.MakeMigrationCommand import MakeMigrationCommand
from .commands.MigrateCommand import MigrateCommand
from .commands.MigrateRefreshCommand import MigrateRefreshCommand
from .commands.MigrateResetCommand import MigrateResetCommand
from .commands.MigrateRollbackCommand import MigrateRollbackCommand
from .commands.ModelCommand import ModelCommand
from .commands.NewCommand import NewCommand
from .commands.PackageCommand import PackageCommand
from .commands.ProviderCommand import ProviderCommand
from .commands.ServeCommand import ServeCommand
from .commands.ViewCommand import ViewCommand

application = Application('Craft Version:', '1.1.8')
application.add(AuthCommand())
application.add(CommandCommand())
application.add(ControllerCommand())
application.add(InstallCommand())
application.add(JobCommand())
application.add(KeyCommand())
application.add(MakeMigrationCommand())
application.add(MigrateCommand())
application.add(MigrateRefreshCommand())
application.add(MigrateResetCommand())
application.add(MigrateRollbackCommand())
application.add(ModelCommand())
application.add(NewCommand())
application.add(ProviderCommand())
application.add(ServeCommand())
application.add(ViewCommand())


ERROR = None

# try to add commands from the service container
sys.path.append(os.getcwd())
try:
    add_venv_site_packages()
    from wsgi import container
except Exception:
    pass

try:
    from config import packages
    # Add additional site packages to vendor if they exist
    for directory in packages.SITE_PACKAGES:
        path = os.path.join(os.getcwd(), directory)
        sys.path.append(path)
    from wsgi import container

    commands = []
    for key, value in container.providers.items():
        if key.endswith('Command'):
            commands.append(key)

    for command in commands:
        application.add(
            container.make('{0}'.format(command))
        )
except ErrorDuringImport:
    pass

except ImportError:
    pass

if __name__ == '__main__':
    application.run()
