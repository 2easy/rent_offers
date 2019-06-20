from setuptools import setup

setup(name='notifier',
    version='0.1',
    description='Simple console notifier - should be replaced with notifier of your choice',
    author='Piotr Olchawa',
    author_email='piotrekolchawa@gmail.com',
    license='MIT',
    packages=['notifier'],
    entry_points = {
        'console_scripts': ['notifier=notifier:main'],
    },
    zip_safe=False)
