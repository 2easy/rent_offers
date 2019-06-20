from setuptools import setup

setup(name='scraper',
    version='0.1',
    description='Script scraping for rental offers.',
    author='Piotr Olchawa',
    author_email='piotrekolchawa@gmail.com',
    license='MIT',
    packages=['scraper'],
    entry_points = {
        'console_scripts': ['scraper=scraper:main'],
    },
    zip_safe=False)
