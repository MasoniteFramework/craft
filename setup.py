from setuptools import setup

setup(
    name="craft",
    version='0.0.1',
    packages=['craft'],
    install_requires=[
        'masonite',
    ],
    include_package_data=True,
    entry_points='''
        [console_scripts]
        craft=craft.application:application.run
    ''',
)
