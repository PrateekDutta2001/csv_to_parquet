from setuptools import setup

setup(
    name='csv-to-parquet',
    version='1.1',
    packages=['csv_to_parquet'],
    install_requires=['pandas'],
    entry_points={
        'console_scripts': [
            'csv-to-parquet=csv_to_parquet.converter:main',
        ],
    },
    author='Prateek Dutta',
    author_email='prateekdutta2001@gmail.com',
    description='A Python package to convert CSV files to Parquet format.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/PrateekDutta2001/csv_to_parquet',
    license='MIT',
)
