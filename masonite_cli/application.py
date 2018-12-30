import os
import sys
from pydoc import ErrorDuringImport

from cleo import Application

from masonite_cli.commands.InstallCommand import InstallCommand
from masonite_cli.commands.NewCommand import NewCommand
from masonite_cli.commands.PackageCommand import PackageCommand
from masonite_cli.helpers.helpers import add_venv_site_packages

application = Application('Craft Version:', '2.1.2')
application.add(NewCommand())
application.add(InstallCommand())
application.add(PackageCommand())


ERROR = None

# try to add commands from the service container
sys.path.append(os.getcwd())
try:
    add_venv_site_packages()
    from wsgi import container
except Exception as e:
    try:
        import masonite
        print()
        print('\033[93mWARNING: {}\033[0m'.format(e))
        print()
    except ImportError:
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
        if isinstance(key, str) and key.endswith('Command'):
            commands.append(key)

    for command in commands:
        application.add(
            container.make('{0}'.format(command))
        )
except ErrorDuringImport as e:
    print(e)

except ImportError:
    pass

if __name__ == '__main__':
    application.run()
