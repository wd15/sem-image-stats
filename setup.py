#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='sem_image_analysis',
      version=0.0,
      description='SEM Image Analysis',
      author='Daniel Wheeler',
      author_email='david.wheeler@nist.gov',
      packages=find_packages(),
      data_files=['setup.cfg'])
