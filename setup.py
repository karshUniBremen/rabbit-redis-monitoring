import os
import re
from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


with open(os.path.join(os.path.dirname(__file__), 'monitoring', '__init__.py')) as f:
    version = re.search("__version__ = '([^']+)'", f.read()).group(1)


with open('requirements.txt') as reqs_f:
    reqs = reqs_f.read().strip().split('\n')


setup(
    name='monitoring',
    version=version,
    description='Monitors Redis server, RabbitMQ Broker, Network latency and bandwidth',
    url='https://github.com/karshUniBremen/rabbit-redis-monitoring',
    long_description=readme(),
    long_description_content_type='text/markdown',
    author='Karthik Shenoy Panambur, Shantanoo Desai',
    author_email='she@biba.uni-bremen.de, des@biba.uni-bremen.de',
    license='MIT License',
    packages=find_packages(),
    scripts=['bin/monitoring'],
    install_requires=reqs,
    include_data_package=True,
    zip_safe=False
)
