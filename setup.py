from setuptools import setup

setup(
    name='gen-board.h',
    version='0.1.0',
    packages=['gbdh'],
    url='https://github.com/HarkonenBade/gen-board.h',
    license='MIT',
    author='HarkonenBade',
    author_email='gen-board@harkonen.net',
    description='Board header file generator for ChibiOS',
    install_requires=['ruamel.yaml', 'jinja2', 'setuptools'],
    entry_points={
        'console_scripts': ['gen-board.h = gbdh.core:main']
    },
    package_data={'gbdh': ['board.tmpl',
                           'mcu/*.yaml']},
)
