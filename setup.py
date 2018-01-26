from setuptools import setup, find_packages

setup(
    name='dimibob',
    version='1.0.0',
    url='https://github.com/ChalkPE/dimibob-py',
    license='MIT',
    author='ChalkPE',
    author_email='chalk@chalk.pe',
    description='Korea Digital Media Highschool meal data crawler',
    packages=find_packages(),
    python_requires='>=3',
    install_requires=['bs4', 'requests'])
