#!/usr/bin/env python3
"""Setup configuration for SQL Injection Scanner."""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="sql-injection-scanner",
    version="1.0.1",
    description="A comprehensive scanner for detecting SQL injection vulnerabilities in Python code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="PioManojDatt",
    author_email="contact@PioManojDatt.com",
    url="https://github.com/PioManojDatt/sql-query-injection-scanner",
    project_urls={
        "Bug Tracker": "https://github.com/PioManojDatt/sql-query-injection-scanner/issues",
        "Documentation": "https://github.com/PioManojDatt/sql-query-injection-scanner/blob/main/README.md",
        "Source Code": "https://github.com/PioManojDatt/sql-query-injection-scanner",
    },
    license="MIT",
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.6",
    install_requires=[
        "openpyxl>=3.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.12.0",
            "black>=21.0",
            "flake8>=3.9.0",
            "mypy>=0.910",
        ],
    },
    entry_points={
        "console_scripts": [
            "sql-injection-scanner=sql_injection_scanner.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Utilities",
    ],
    keywords="sql injection security scanner vulnerability detection",
    zip_safe=False,
)
