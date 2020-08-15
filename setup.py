from setuptools import setup

setup(
    name='opencv_draw_annotation',
    version='0.1.0',
    author='Seth Pipho',
    author_email='seth.pipho@gmail.com',
    packages=['opencv_draw_annotation'],
    scripts=[],
    url='http://pypi.python.org/pypi/PackageName/',
    license='LICENSE',
    description='A library for formatting and drawing annotations, such as bounding boxes, text boxes, and trails',
    long_description=open('README.md').read(),
    install_requires=["opencv-python"],
)