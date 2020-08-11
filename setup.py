from setuptools import setup,find_packages  

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='academia-tools',
    version='1.0.0',
    description='package of useful academia tools',
    url='https://github.com/JakeHattwell/Academia-Tools',
    author='Jake Hattwell',
    author_email='j.hattwell@uq.edu.au',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages('academia-tools'),
    install_requires=[
        'PyPDF2',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    scripts = ['bin/paper-scraper.py']
    )