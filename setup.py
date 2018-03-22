from setuptools import setup

setup(
    name="cleocli",
    version='0.0.1',
    packages=['cleocli'],
    install_requires=[
        'masonite',
    ],
    include_package_data=True,
    entry_points='''
        [console_scripts]
        cli=cleocli.application:application.run
    ''',
)
