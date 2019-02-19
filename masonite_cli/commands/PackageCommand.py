from cleo import Command
import os


class PackageCommand(Command):
    """
    Creates a new package

    package
        {name : Name of your Masonite project}
    """

    def handle(self):
        name = self.argument('name')

        if not os.path.exists(name):
            os.makedirs(os.path.join(name, name))

        # create setup.py
        setup = open(os.path.join(os.getcwd(), name, 'setup.py'), 'w+')
        setup.write("from setuptools import setup\n\n")
        setup.write('setup(\n    ')
        setup.write('name="{0}",\n    '.format(name))
        setup.write("version='0.0.1',\n    ")
        setup.write("packages=['{0}'],\n    ".format(name))
        setup.write("install_requires=[\n        ")
        setup.write("'masonite',\n    ")
        setup.write("],\n    ")
        setup.write('include_package_data=True,\n')
        setup.write(')\n')
        setup.close()

        manifest = open(os.path.join(os.getcwd(), name, 'MANIFEST.in'), 'w+')
        manifest.close()


        init_file = open(os.path.join(
            os.getcwd(), name, '{0}/{1}'.format(name, '__init__.py')), 'w+')
        init_file.close()

        integration_file = open(os.path.join(
            os.getcwd(), name, '{0}/{1}'.format(name, 'integration.py')), 'w+')
        integration_file.write('import os\n\n')
        integration_file.write(
            'package_directory = os.path.dirname(os.path.realpath(__file__))\n\n')
        integration_file.close()
        self.info('Package Created Successfully!')
