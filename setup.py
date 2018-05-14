from setuptools import setup

setup(
    name="masonite-cli",
    version='2.0.2',
    packages=[
        'masonite_cli',
        'masonite_cli.commands',
        'masonite_cli.helpers',
    ],
    py_modules=['masonite_cli'],
    install_requires=[
        'cleo==0.6.5',
        'cryptography',
        'requests==2.18.4',
    ],
    include_package_data=True,
    entry_points='''
        [console_scripts]
        craft=masonite_cli.application:application.run
    ''',
)
