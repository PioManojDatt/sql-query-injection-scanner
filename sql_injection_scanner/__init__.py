"""
SQL Injection Vulnerability Scanner

A comprehensive tool to scan Python codebases for potential SQL injection vulnerabilities,
with support for multiple pattern detection methods and Excel report generation.

Features:
    - Detects unsafe f-strings, string concatenation, .format(), and % formatting in SQL queries
    - Risk level classification (HIGH, MEDIUM, LOW)
    - Excel report generation with color-coded findings
    - Configurable scanning patterns
    - Smart filtering for safe parameterized queries

Example:
    >>> from sql_injection_scanner import SQLInjectionScanner
    >>> scanner = SQLInjectionScanner('/path/to/project')
    >>> findings = scanner.scan()
    >>> scanner.generate_excel_report('report.xlsx')
"""

__version__ = "1.0.3"
__author__ = "PioManojDatt"
__email__ = "contact@PioManojDatt.com"
__url__ = "https://github.com/PioManojDatt/sql-query-injection-scanner"
__license__ = "MIT"

from .scanner import SQLInjectionScanner

__all__ = ["SQLInjectionScanner", "__version__"]
