#!/usr/bin/env python3

from setuptools import setup

setup(
    name='kitti2bag',
    version='1.5.1',
    description='Convert KITTI dataset to ROS bag file with support for odometry laser data sequences!',
    author='Tomas Krejci',
    author_email='tomas@krej.ci',
    maintainer='Jorge Diogo Ribeiro',
    maintainer_email='jorge.d.ribeiro@inesctec.pt',
    url='https://github.com/Thorfr123/kitti2bag',
    keywords = ['dataset', 'ros', 'rosbag', 'kitti'],
    packages=['kitti2bag'],
    entry_points = {
        'console_scripts': ['kitti2bag=kitti2bag.__main__:main'],
    },
    install_requires=['pykitti', 'progressbar2']
)