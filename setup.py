import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='parsefw',
    version='0.1.0',
    description='Parsing data representation tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aleasims/parsefw',
    author='Evgin Alexander (ISP RAS)',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
    ],
    keywords='parse ddl',
    packages=['parsefw'],
    package_dir={'parsefw': 'parsefw'},
    python_requires='>=3.5',
    install_requires=[
        'kaitaistruct>=0.8',
        'graphviz>=0.11.1',
        'pyyaml>=5.1.1',
        'pylint',
        'flake8',
        'autopep8'
    ],
    package_data={
        'kspyspector': ['parsefw/kaitai/tests/data/*'],
    },
    entry_points={
        'console_scripts': [
            'parsefw=scripts.main:main',
        ]
    }
)
