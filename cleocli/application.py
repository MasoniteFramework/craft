from cleo import Application, Command

from .commands.AuthCommand import AuthCommand
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

application = Application()
application.add(AuthCommand())
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

if __name__ == '__main__':
    application.run()
