from setuptools import setup, find_packages

setup(
    name="khmer_latin_name_transformer",
    version="0.0.1",
    description="",
    url="https://github.com/seanghay/khmer_latin_name_transformer",
    author="Seanghay Yath",
    author_email="seanghay.dev@gmail.com",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    python_requires=">3.5",
    packages=find_packages(),
    package_dir={"khmer_latin_name_transformer": "khmer_latin_name_transformer"},
    package_data={
        "khmer_latin_name_transformer": ["latin_km_names.fst", "km_latin_names.fst"]
    },
    include_package_data=True,
    install_requires=[
        "pynini",
    ],
)
