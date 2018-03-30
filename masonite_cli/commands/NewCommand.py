from cleo import Command
import os
import shutil
import requests
import zipfile


class NewCommand(Command):
    """
    Creates a new Masonite project

    new
        {name : Name of your Masonite project}
        {--b|--branch=False : Specify which branch from the Masonite repo you would like to install}
        {--r|--release=False : Specify which version of Masonite you would like to install}
    """

    def handle(self):
        name = self.argument('name')
        branch = self.option('branch')
        version = self.option('release')
        if not os.path.isdir(os.path.join(os.getcwd(),name)):
            from io import BytesIO
            import requests

            for directory in os.listdir(os.getcwd()):
                if directory.startswith('masonite-'):
                    return self.comment('There is a folder that starts with "masonite-" and therefore craft cannot create a new project')

            if branch:
                get_branch = requests.get(
                    'https://api.github.com/repos/MasoniteFramework/masonite/branches/{0}'.format(branch))
                
                if not 'name' in get_branch.json():
                    return self.comment('Branch {0} does not exist.'.format(branch))

                zipball = 'http://github.com/MasoniteFramework/masonite/archive/{0}.zip'.format(branch)
            elif version:
                get_zip_url = requests.get(
                    'https://api.github.com/repos/MasoniteFramework/masonite/releases/tags/v{0}'.format(version))

                try:
                    zipball = get_zip_url.json()['zipball_url']
                except:
                    return self.comment('Version {0} does not exist.'.format(version))
            else:
                get_zip_url = requests.get(
                    'https://api.github.com/repos/MasoniteFramework/masonite/releases/latest')
                
                zipball = get_zip_url.json()['zipball_url']

            success = False
            
            zipurl = zipball

            self.info('Crafting Application ...')

            try:
                # Python 3
                from urllib.request import urlopen
                
                with urlopen(zipurl) as zipresp:
                    with zipfile.ZipFile(BytesIO(zipresp.read())) as zfile:
                        zfile.extractall(os.getcwd())
                
                success = True
            except:
                # Python 2
                import urllib
                r = urllib.urlopen(zipurl)
                with zipfile.ZipFile(BytesIO(r.read())) as z:
                    z.extractall(os.getcwd())
                
                success = True

            if success:
                for directory in os.listdir(os.getcwd()):
                    if directory.startswith('MasoniteFramework-masonite') or directory.startswith('masonite-'):
                        os.rename(
                            os.path.join(os.getcwd(), '{0}'.format(directory)), os.getcwd() + '/' +name)
                        self.info('\nApplication Created Successfully!\n\nNow just cd into your project and run\n\n    $ craft install\n\nto install the project dependencies.\n\nCreate Something Amazing!')
            else:
                self.comment('Could Not Create Application :(')
        else:
            self.comment('Directory {0} already exists. Please choose another project name'.format(name))
