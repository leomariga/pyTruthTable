import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyTruthTable", # Replace with your own username
    version="0.0.1",
    author="Leonardo Mariga",
    author_email="leomariga@gmail.com",
    description="A powerful python tool to create truth tables for logical analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://leomariga.github.io/pyTruthTable/",
    packages=setuptools.find_packages(),
    keywords='truth table python generation logic pandas dataframe',
    project_urls={
        'Documentation': 'https://leomariga.github.io/pyTruthTable/',
        'Source': 'https://github.com/leomariga/pyTruthTable',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
