from setuptools import setup

version = __import__('collections_microoptimizations').__version__

setup(
    name='collections_microoptimizations',
    version=version,
    description='Collections Micro-optimizations',
    packages=['collections_microoptimizations'],
    zip_safe=False,
    include_package_data=True,
)
