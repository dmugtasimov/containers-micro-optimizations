from setuptools import setup

version = __import__('containers_micro_optimizations').__version__

setup(
    name='containers_micro_optimizations',
    version=version,
    description='Containers Micro-optimizations',
    packages=['containers_micro_optimizations'],
    zip_safe=False,
    include_package_data=True,
)
