from setuptools import setup
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='BO4ML',
    version='0.1',
    packages=['BanditOpt', 'Component','Component.mHyperopt'],
    url='https://github.com/ECOLE-ITN/BO4ML',
    license='GPL-3.0 License',
    author='Duc Anh Nguyen',
    author_email='d.a.nguyen@liacs.leidenuniv.nl',
    description='BO4AutoML: Bayesian Optimization library AutoML',
    install_requires=requirements
)
