from setuptools import setup, find_packages

setup(
    name='PyInvest',
    version='1.0.1',
    packages=find_packages(),
    data_files=[("pyinvestconf", ['conf/pyinvest.json'])],
    install_requires=['requests', 'selenium'],
    author='Jeff Moorhead',
    author_email='Jeff.moorhead1@gmail.com',
    description='A Python wrapper for the TD Ameritrade REST API',
    scripts=['scripts/tdapositions', 'scripts/tdaorders', 'scripts/tda_allocations']
)
    
