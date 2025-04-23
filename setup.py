from setuptools import setup, find_packages

setup(
    name='phonance',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    author='Vuong BUI',
    description='A Python library for finance calculations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vuong-buihv/phonance',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License'
    ],
    license='BSD-3-Clause',
)
