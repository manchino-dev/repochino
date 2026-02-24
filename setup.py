from setuptools import setup, find_packages

setup(
    name='repochino',
    version='0.1.0',
    author='Your Name',
    author_email='youremail@example.com',
    description='A short description of the repochino project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/manchino-dev/repochino',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)