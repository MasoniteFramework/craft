import os
import sys
import platform


def append_system_path():
    # sys.path.append(os.getcwd())
    print(os.getcwd())


def add_venv_site_packages():
    try:
        from config import packages
        # Add additional site packages to vendor if they exist
        for directory in packages.SITE_PACKAGES:
            path = os.path.join(os.getcwd(), directory)
            sys.path.append(path)
    except ImportError:
        pass
        # raise ImportError('Not inside a Masonite project')

    if 'VIRTUAL_ENV' in os.environ:
        python_version = None
        venv_directory = os.listdir(
            os.path.join(os.environ['VIRTUAL_ENV'], 'lib')
        )

        for directory in venv_directory:
            if directory.startswith('python'):
                python_version = directory
                break

        if python_version:
            site_packages_directory = os.path.join(
                os.environ['VIRTUAL_ENV'],
                'lib',
                python_version,
                'site-packages'
            )
            sys.path.append(site_packages_directory)

        elif platform.system() == 'Windows':
            site_packages_directory = os.path.join(
                os.environ['VIRTUAL_ENV'],
                'Lib',
                'site-packages'
            )
            
            sys.path.append(site_packages_directory)
        else:
            print('\033[93mWARNING: Could not add the virtual environment you are currently in. Attempting to add: {0}\033[93m'.format(
                os.environ['VIRTUAL_ENV']))
