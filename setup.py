from setuptools import setup

setup(
    name='opencv_draw_annotation',
    version='0.1.0',
    author='Seth Pipho',
    author_email='seth.pipho@gmail.com',
    packages=['opencv_draw_annotation'],
    scripts=[],
    url='https://github.com/SethPipho/opencv-draw-annotation',
    license='MIT',
    description='A library for formatting and drawing annotations (e.g. bounding boxes) on images using opencv',
    long_description=open('README.md').read(),
    install_requires=["opencv-python"],
)