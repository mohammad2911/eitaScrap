from setuptools import setup, find_packages

setup(
    name="eitaa_scraper",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "beautifulsoup4",
        "pandas",
        "openpyxl"
    ],
    entry_points={
        "console_scripts": [
            "eitaa-scraper=main:main"
        ]
    },
)
